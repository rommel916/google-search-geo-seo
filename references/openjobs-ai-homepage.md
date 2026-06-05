# OpenJobs AI Homepage Profile

Use this profile only for `/Users/shixiaowen/Desktop/homepage`. Re-read the repository before relying on it because the implementation may have changed.

## Durable Project Constraints

- Prefer direct implementation in the active checkout when changes are requested.
- Keep GEO content faithful to source one-pagers; do not invent claims or team facts.
- Employer-side recruiting is the canonical homepage framing.
- OpenJobs AI is the company/platform entity.
- Mira is the autonomous AI recruiter/product entity.
- Preserve plain-text GEO routes under `public/information/*.txt` unless the user explicitly asks to restore HTML GEO pages.
- Keep `llms.txt` and `llms-full.txt` aligned with visible content and source materials.
- Treat user-selected competitors as authoritative in comparison work.
- Do not add build-time GEO generation hooks unless requested.

## Known SEO/GEO Surfaces

- `app/layout.tsx`
- `app/page.tsx`
- route metadata under `app/*/page.tsx`
- homepage JSON-LD
- `public/robots.txt`
- `public/sitemap.xml`
- `public/homepage-sitemap.xml`
- `public/llms.txt`
- `public/llms-full.txt`
- `public/information/*.txt`
- `public/information/use-cases/*.txt`
- `next.config.ts`

## Baseline Observed on 2026-06-05

- Multiple canonical and machine-readable surfaces used `https://www-dev.openjobs-ai.com`.
- Other routes and links used `https://www.openjobs-ai.com`.
- This host inconsistency was the highest-priority technical finding, but the final production canonical host still must be confirmed before replacement.
- The homepage already contained server-rendered text and JSON-LD for `Organization`, `WebSite`, `SoftwareApplication`, and `FAQPage`.
- Existing text assets covered AI recruiting platform, autonomous AI recruiter, Mira, AI recruiting agent, startup hiring, recruiter productivity, and research.
- Homepage and text assets contained multiple quantitative claims. Reconcile each claim against the current authoritative source before expanding or reusing it.

## Validation Notes

- Default system Node may be too old for current `pnpm`; prefer `/Users/shixiaowen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node` in `PATH`.
- A stale `.next/lock` or running Next process can block builds.
- If Next infers the wrong workspace root, `turbopack.root = process.cwd()` has been a known fix, but revalidate before adding it.
- Git push may trigger a Husky pre-push production build.

## Recommended Audit Order

1. Confirm production canonical host.
2. Scan all metadata, JSON-LD, sitemap, robots, llms, legal, footer, and internal links for host drift.
3. Verify all sitemap and information URLs exist and return the intended content type.
4. Reconcile homepage claims with current one-pagers.
5. Validate visible FAQ content against FAQ structured data.
6. Check internal links to about, pricing, research, use cases, and evidence.
7. Run build and inspect rendered desktop/mobile output.

