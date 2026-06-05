#!/usr/bin/env python3
"""Run a conservative static SEO/GEO audit against a local web repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse


TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".json",
    ".md",
    ".mjs",
    ".scss",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
SKIP_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".output",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "vendor",
}
CONTENT_ROOTS = {"app", "blog", "content", "docs", "pages", "public", "src"}
SKIP_FILENAMES = {
    "bun.lock",
    "composer.lock",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
}
URL_RE = re.compile(r"https?://[^\s\"'<>),]+")
HOST_RE = re.compile(r"^[a-z0-9.-]+$", re.I)
METRIC_RE = re.compile(
    r"(?<![\w.])(?:\d+(?:\.\d+)?\s*(?:%|x|\+)|(?:one|two|three|four|five|six|seven|eight|nine|ten)[- ](?:fold|times))",
    re.I,
)
SCHEMA_TYPE_RE = re.compile(r"[\"']@type[\"']\s*:\s*[\"']([^\"']+)[\"']")
CANONICAL_HINT_RE = re.compile(
    r"(?:metadataBase|canonical|rel=[\"']canonical[\"']|openGraph|siteUrl|baseUrl)",
    re.I,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit canonical, robots, sitemap, llms, schema, and claim signals."
    )
    parser.add_argument("--root", required=True, help="Repository root")
    parser.add_argument(
        "--canonical-host",
        help="Expected production host, for example www.example.com",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format",
    )
    parser.add_argument("--output", help="Write output to this file")
    parser.add_argument(
        "--max-file-bytes",
        type=int,
        default=2_000_000,
        help="Skip text files larger than this size",
    )
    return parser.parse_args()


def iter_text_files(root: Path, max_file_bytes: int):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILENAMES:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            if path.stat().st_size > max_file_bytes:
                continue
            yield path
        except OSError:
            continue


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def host_from_url(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


def base_domain(host: str) -> str:
    parts = host.lower().strip(".").split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def clean_url(url: str) -> str:
    return url.rstrip("`*_.,;:")


def is_web_content_file(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return bool(rel.parts and rel.parts[0] in CONTENT_ROOTS)


def is_metric_candidate(line: str) -> bool:
    style_markers = (
        "background:",
        "background-image:",
        "background-size:",
        "border-radius:",
        "height:",
        "left:",
        "line-height:",
        "opacity:",
        "right:",
        "top:",
        "transform:",
        "width:",
        "rgba(",
        "linear-gradient(",
        "translate",
    )
    lowered = line.lower()
    attribute_markers = (
        "classname=",
        "height=",
        "samplerate:",
        "style=",
        "width=",
    )
    stripped = line.strip()
    if stripped.startswith(("//", "/*", "*", "{/*")):
        return False
    if re.search(r"\b(?:height|width)\s*=", lowered):
        return False
    if re.search(r"\b(?:backgroundsize|scale-\d+)\b", lowered):
        return False
    return not any(marker in lowered for marker in style_markers + attribute_markers)


def is_environment_host(host: str) -> bool:
    return bool(
        re.search(
            r"(?:^|[-.])(?:dev|development|localhost|qa|stage|staging|test)(?:[-.]|$)",
            host.lower(),
        )
    )


def discover_artifact(root: Path, name: str) -> list[Path]:
    candidates = [root / name, root / "public" / name, root / "static" / name]
    return [path for path in candidates if path.is_file()]


def parse_sitemap(path: Path) -> tuple[list[str], str | None]:
    try:
        tree = ET.parse(path)
    except (ET.ParseError, OSError) as exc:
        return [], str(exc)
    urls = []
    for element in tree.getroot().iter():
        if element.tag.endswith("loc") and element.text:
            urls.append(element.text.strip())
    return urls, None


def local_target_exists(root: Path, url: str) -> bool | None:
    path = urlparse(url).path
    if not path or path == "/":
        return any(
            candidate.is_file()
            for candidate in (
                root / "app" / "page.tsx",
                root / "pages" / "index.tsx",
                root / "public" / "index.html",
                root / "index.html",
            )
        )
    public_target = root / "public" / path.lstrip("/")
    if public_target.is_file():
        return True
    route = path.strip("/")
    route_candidates = (
        root / "app" / route / "page.tsx",
        root / "app" / route / "page.jsx",
        root / "pages" / f"{route}.tsx",
        root / "pages" / f"{route}.jsx",
        root / "public" / route / "index.html",
    )
    if any(candidate.is_file() for candidate in route_candidates):
        return True
    if "[" in route or ":" in route:
        return None
    return False


def scan_repository(root: Path, max_file_bytes: int) -> dict:
    files = list(iter_text_files(root, max_file_bytes))
    url_signals = defaultdict(list)
    schema_types = Counter()
    metrics = []
    metadata_files = set()
    title_files = set()
    description_files = set()
    lang_values = Counter()

    for path in files:
        text = read_text(path)
        rel = relative(path, root)
        if not text:
            continue

        web_content = is_web_content_file(path, root)
        relative_parts = set(path.relative_to(root).parts)

        if web_content and path.suffix.lower() != ".md" and CANONICAL_HINT_RE.search(text):
            metadata_files.add(rel)
            for lineno, line in enumerate(text.splitlines(), 1):
                if CANONICAL_HINT_RE.search(line):
                    for url in URL_RE.findall(line):
                        url_signals["metadata"].append(
                            {"url": clean_url(url), "file": rel, "line": lineno}
                        )

        for lineno, line in enumerate(text.splitlines(), 1):
            if web_content:
                for url in URL_RE.findall(line):
                    cleaned = clean_url(url)
                    host = host_from_url(cleaned)
                    if host and is_environment_host(host):
                        url_signals["environment-host"].append(
                            {"url": cleaned, "file": rel, "line": lineno}
                        )
            if re.search(r"\btitle\b", line, re.I):
                title_files.add(rel)
            if re.search(r"\bdescription\b", line, re.I):
                description_files.add(rel)
            if (
                web_content
                and "assets" not in relative_parts
                and path.suffix.lower() not in {".css", ".json", ".scss"}
                and len(metrics) < 80
                and METRIC_RE.search(line)
                and is_metric_candidate(line)
            ):
                metrics.append(
                    {
                        "file": rel,
                        "line": lineno,
                        "text": " ".join(line.strip().split())[:220],
                    }
                )

        for schema_type in SCHEMA_TYPE_RE.findall(text):
            schema_types[schema_type] += 1

        for lang in re.findall(r"<html[^>]+\blang=[\"']([^\"']+)", text, re.I):
            lang_values[lang] += 1

    return {
        "files_scanned": len(files),
        "metadata_files": sorted(metadata_files),
        "title_files": sorted(title_files),
        "description_files": sorted(description_files),
        "schema_types": dict(schema_types),
        "metrics": metrics,
        "lang_values": dict(lang_values),
        "url_signals": dict(url_signals),
    }


def build_audit(root: Path, expected_host: str | None, max_file_bytes: int) -> dict:
    if expected_host:
        expected_host = expected_host.lower().strip()
        if "://" in expected_host:
            expected_host = host_from_url(expected_host)
        if not expected_host or not HOST_RE.match(expected_host):
            raise ValueError("--canonical-host must be a hostname, not a path")

    scan = scan_repository(root, max_file_bytes)
    artifacts = {}
    findings = []
    signals = []
    seen_signals = set()
    for kind, kind_signals in scan["url_signals"].items():
        for signal in kind_signals:
            key = (kind, signal["url"], signal["file"], signal["line"])
            if key in seen_signals:
                continue
            seen_signals.add(key)
            signals.append({**signal, "kind": kind})
    sitemap_entries = []

    for name in ("robots.txt", "sitemap.xml", "homepage-sitemap.xml", "llms.txt", "llms-full.txt"):
        paths = discover_artifact(root, name)
        artifacts[name] = [relative(path, root) for path in paths]
        if not paths:
            severity = "P1" if name in {"robots.txt", "sitemap.xml"} else "INFO"
            findings.append(
                {
                    "severity": severity,
                    "issue": f"{name} not found in common locations",
                    "evidence": str(root),
                }
            )
        for path in paths:
            text = read_text(path)
            if name == "robots.txt":
                for lineno, line in enumerate(text.splitlines(), 1):
                    if line.strip().lower().startswith("sitemap:"):
                        url = line.split(":", 1)[1].strip()
                        signals.append(
                            {
                                "kind": "robots-sitemap",
                                "url": url,
                                "file": relative(path, root),
                                "line": lineno,
                            }
                        )
                    if line.strip().lower() == "disallow: /":
                        findings.append(
                            {
                                "severity": "P0",
                                "issue": "robots.txt blocks the entire site",
                                "evidence": f"{relative(path, root)}:{lineno}",
                            }
                        )
            elif name.endswith("sitemap.xml") or name == "sitemap.xml":
                urls, error = parse_sitemap(path)
                if error:
                    findings.append(
                        {
                            "severity": "P0",
                            "issue": f"Invalid XML in {name}",
                            "evidence": f"{relative(path, root)}: {error}",
                        }
                    )
                for url in urls:
                    entry = {
                        "url": url,
                        "file": relative(path, root),
                        "host": host_from_url(url),
                        "local_target_exists": local_target_exists(root, url),
                    }
                    sitemap_entries.append(entry)
                    signals.append(
                        {
                            "kind": "sitemap",
                            "url": url,
                            "file": relative(path, root),
                            "line": None,
                        }
                    )
            elif name in {"llms.txt", "llms-full.txt"}:
                for lineno, line in enumerate(text.splitlines(), 1):
                    for url in URL_RE.findall(line):
                        signals.append(
                            {
                                "kind": "llms",
                                "url": clean_url(url),
                                "file": relative(path, root),
                                "line": lineno,
                            }
                        )

    for signal in signals:
        signal["host"] = host_from_url(signal["url"])

    signal_hosts = Counter(
        signal["host"] for signal in signals if signal.get("host")
    )
    canonical_hosts = Counter(
        signal["host"]
        for signal in signals
        if signal.get("host")
        and signal["kind"] in {"environment-host", "metadata", "robots-sitemap", "sitemap"}
    )

    if expected_host:
        expected_base = base_domain(expected_host)
        mismatches = []
        seen_mismatches = set()
        for signal in signals:
            mismatch_key = (signal["url"], signal["file"], signal.get("line"))
            if mismatch_key in seen_mismatches:
                continue
            if (
                signal.get("host")
                and signal["kind"]
                in {"environment-host", "metadata", "robots-sitemap", "sitemap", "llms"}
                and signal["host"] != expected_host
                and (
                    signal["kind"]
                    in {"environment-host", "metadata", "robots-sitemap", "sitemap"}
                    or base_domain(signal["host"]) == expected_base
                )
            ):
                seen_mismatches.add(mismatch_key)
                mismatches.append(signal)
        for mismatch in mismatches[:40]:
            line = f":{mismatch['line']}" if mismatch.get("line") else ""
            findings.append(
                {
                    "severity": "P0",
                    "issue": f"Host differs from expected canonical host {expected_host}",
                    "evidence": f"{mismatch['file']}{line} -> {mismatch['url']}",
                }
            )
    elif len(canonical_hosts) > 1:
        findings.append(
            {
                "severity": "P0",
                "issue": "Multiple hosts appear in canonical, sitemap, or robots signals",
                "evidence": ", ".join(
                    f"{host} ({count})" for host, count in canonical_hosts.most_common()
                ),
            }
        )

    missing_local = [
        entry for entry in sitemap_entries if entry["local_target_exists"] is False
    ]
    for entry in missing_local[:30]:
        findings.append(
            {
                "severity": "INFO",
                "issue": "Sitemap URL has no obvious matching local route or public file; verify deployment routing",
                "evidence": f"{entry['file']} -> {entry['url']}",
            }
        )

    if not scan["schema_types"]:
        findings.append(
            {
                "severity": "P2",
                "issue": "No JSON-LD @type values detected",
                "evidence": "Static scan of repository text files",
            }
        )

    severity_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3, "INFO": 4}
    findings.sort(key=lambda item: severity_order.get(item["severity"], 9))

    return {
        "root": str(root),
        "expected_canonical_host": expected_host,
        "summary": {
            "files_scanned": scan["files_scanned"],
            "findings": Counter(item["severity"] for item in findings),
            "signal_hosts": dict(signal_hosts),
            "sitemap_urls": len(sitemap_entries),
            "quantified_claim_lines": len(scan["metrics"]),
        },
        "findings": findings,
        "artifacts": artifacts,
        "signals": signals,
        "sitemap_entries": sitemap_entries,
        "schema_types": scan["schema_types"],
        "lang_values": scan["lang_values"],
        "metadata_files": scan["metadata_files"],
        "quantified_claims": scan["metrics"],
        "limitations": [
            "Static repository scan only; live HTTP behavior is not tested.",
            "Framework-generated metadata may require a build or rendered HTML inspection.",
            "Quantified claims are flagged for source review, not judged as false.",
            "External URLs in llms files may be legitimate; review host mismatches manually.",
        ],
    }


def render_markdown(audit: dict) -> str:
    summary = audit["summary"]
    lines = [
        "# Google Search GEO/SEO Static Audit",
        "",
        f"- Root: `{audit['root']}`",
        f"- Expected canonical host: `{audit['expected_canonical_host'] or 'not provided'}`",
        f"- Text files scanned: {summary['files_scanned']}",
        f"- Sitemap URLs found: {summary['sitemap_urls']}",
        f"- Quantified claim lines flagged: {summary['quantified_claim_lines']}",
        "",
        "## Findings",
        "",
    ]
    if not audit["findings"]:
        lines.append("- No deterministic static findings. Continue with rendered and live checks.")
    else:
        for finding in audit["findings"]:
            lines.append(
                f"- **{finding['severity']}** {finding['issue']}  \n"
                f"  Evidence: `{finding['evidence']}`"
            )

    lines.extend(["", "## Discovered Artifacts", ""])
    for name, paths in audit["artifacts"].items():
        value = ", ".join(f"`{path}`" for path in paths) if paths else "not found"
        lines.append(f"- {name}: {value}")

    lines.extend(["", "## Signal Hosts", ""])
    hosts = summary["signal_hosts"]
    if hosts:
        for host, count in sorted(hosts.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"- `{host}`: {count}")
    else:
        lines.append("- No absolute URL hosts detected in audited signals.")

    lines.extend(["", "## Structured Data Types", ""])
    if audit["schema_types"]:
        for schema_type, count in sorted(audit["schema_types"].items()):
            lines.append(f"- `{schema_type}`: {count}")
    else:
        lines.append("- None detected.")

    lines.extend(["", "## Quantified Claims to Source-Check", ""])
    if audit["quantified_claims"]:
        for claim in audit["quantified_claims"][:40]:
            lines.append(
                f"- `{claim['file']}:{claim['line']}`: {claim['text']}"
            )
    else:
        lines.append("- None detected.")

    lines.extend(["", "## Limitations", ""])
    for limitation in audit["limitations"]:
        lines.append(f"- {limitation}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        print(f"error: repository root does not exist: {root}", file=sys.stderr)
        return 2
    try:
        audit = build_audit(root, args.canonical_host, args.max_file_bytes)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    output = (
        json.dumps(audit, ensure_ascii=False, indent=2)
        if args.format == "json"
        else render_markdown(audit)
    )
    if args.output:
        output_path = Path(args.output).expanduser()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output + ("\n" if not output.endswith("\n") else ""), encoding="utf-8")
        print(output_path)
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
