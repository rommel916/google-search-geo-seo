# Google Search GEO & SEO

[中文](README.md)

A Codex skill for search engine optimization and generative engine optimization (GEO). It uses official Google Search Central guidance as its foundation and keeps broader industry GEO observations in a separate evidence layer. It can audit, plan, implement, and validate improvements for websites and technical documentation.

The skill does not treat GEO as a separate ranking trick. For Google AI Overviews and AI Mode, normal crawling, indexing, snippet eligibility, content quality, and search experience remain the foundation.

## Capabilities

- Audit canonicals, redirects, robots directives, sitemaps, HTTP status codes, and indexing policy
- Inspect server rendering, JavaScript content, crawlable links, and initial HTML
- Improve titles, descriptions, headings, internal links, Open Graph data, and structured data
- Check entity consistency across company, product, audience, category, and external profiles
- Make definitions, comparisons, procedures, and key facts understandable when retrieved independently
- Review `llms.txt`, plain-text information pages, and other machine-readable content
- Improve API documentation, developer guides, versioning, error behavior, and code examples
- Evaluate owned content, independent coverage, authentic reviews, and third-party mentions
- Design measurement for citations, mentions, competitor share of voice, context, and sentiment
- Implement requested changes and validate builds, linting, HTML, XML, and JSON-LD

## Evidence Levels

The skill separates:

1. **Google-confirmed guidance**
2. **Official platform documentation**, such as crawler-specific behavior
3. **Industry or vendor observations**, including Search Engine Land, Semrush, and Mintlify
4. **Implementation inference** based on the target codebase and rendered output
5. **Unverified assumptions** that require additional access or data

`llms.txt`, FAQ schema, keyword density, or a specific content format cannot guarantee AI citations.

## Technical Documentation GEO

For API and developer documentation, the skill also checks:

- Whether each priority page serves one clear task or concept
- Whether the action, command, definition, or result appears early
- Parameter types, defaults, ranges, units, and boundary behavior
- HTTP status codes, errors, permissions, and security guidance
- Current, preview, deprecated, and migration information
- Required imports, request details, and expected results in code examples
- Terminology consistency across docs, OpenAPI, SDKs, navigation, and errors
- Intentional handling of old versions through versioned URLs, canonicals, redirects, or `noindex`

## AI Crawler Boundaries

Crawler purposes must be evaluated separately:

- `OAI-SearchBot`: automatic crawling for ChatGPT Search
- `GPTBot`: crawling that may be used to improve foundation models
- `ChatGPT-User`: user-triggered visits, not an automatic search crawler
- `Google-Extended`: controls certain Gemini training and grounding uses; it does not control inclusion or ranking in Google Search, AI Overviews, or AI Mode

Search retrieval, model training, and user-triggered access are separate policy decisions.

## Installation

Using GitHub CLI:

```bash
mkdir -p ~/.codex/skills
gh repo clone rommel916/google-search-geo-seo ~/.codex/skills/google-search-geo-seo
```

To update an existing installation:

```bash
git -C ~/.codex/skills/google-search-geo-seo pull
```

## Usage

Invoke it explicitly in Codex:

```text
Use $google-search-geo-seo to audit this website and implement the highest-priority SEO and GEO fixes.
```

```text
Use $google-search-geo-seo to check whether this API documentation can be accurately retrieved and cited by Google, ChatGPT, and Perplexity.
```

```text
Use $google-search-geo-seo to create a 30/60/90-day plan for SEO, content, earned authority, and AI visibility.
```

## Local Static Audit

```bash
python3 scripts/audit_site.py --root /path/to/repository
```

With the production canonical host:

```bash
python3 scripts/audit_site.py \
  --root /path/to/repository \
  --canonical-host www.example.com \
  --output /tmp/search-audit.md
```

The audit script provides investigation leads. It does not replace code review, build validation, live HTTP inspection, or Search Console.

## Priority Model

- **P0**: crawling, indexing, status, canonical, redirect, and rendering failures
- **P1**: content value, entity understanding, evidence, terminology, and answer accuracy
- **P2**: metadata, structured data, media, and page experience
- **P3**: content expansion, earned authority, AI probes, and ongoing measurement

## Repository Structure

```text
google-search-geo-seo/
├── README.md
├── README_EN.md
├── SKILL.md
├── agents/openai.yaml
├── scripts/audit_site.py
└── references/
    ├── audit-checklist.md
    ├── google-search-central-principles.md
    ├── google-search-central-url-index.md
    ├── industry-geo-visibility-principles.md
    ├── technical-documentation-geo.md
    └── openjobs-ai-homepage.md
```

## Validation

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
python3 -m py_compile scripts/audit_site.py
git diff --check
```

## Sources

- [Google Search Central documentation](https://developers.google.com/search/docs)
- [Google AI features and your website](https://developers.google.com/search/docs/appearance/ai-overviews)
- [OpenAI crawlers](https://platform.openai.com/docs/bots)
- [Search Engine Land GEO framework](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418)
- [Mintlify GEO guide](https://www.mintlify.com/docs/zh/guides/geo)
