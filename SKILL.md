---
name: google-search-geo-seo
description: Audit, plan, implement, and validate SEO and GEO improvements using Google Search Central guidance. Use when Codex needs to review or modify a website, web app, repository, metadata, canonical URLs, robots.txt, sitemaps, structured data, JavaScript-rendered content, llms.txt files, answer-ready content, entity consistency, Search Console measurement plans, or generative AI search visibility. Also use for requests to explain how Google SEO relates to GEO/AEO, prioritize search issues, or turn a Google Search audit into concrete code and content changes.
---

# Google Search GEO and SEO

Apply Google Search Central principles to produce an evidence-based audit and, when requested, implement the fixes. Treat GEO for Google as an extension of SEO, not a separate ranking trick.

## Core Rules

1. Establish the intended production canonical domain before changing URLs.
2. Inspect the real repository and rendered/live output; do not infer implementation from filenames alone.
3. Use official Google Search documentation as the primary source. For current or changed guidance, browse official `developers.google.com/search` and `support.google.com/webmasters` pages.
4. Distinguish Google-confirmed requirements from recommendations and your own inference.
5. Treat `llms.txt` and machine-readable text pages as supplementary GEO surfaces, not Google ranking requirements.
6. Keep important content visible as crawlable text. Do not rely on images, canvas, animation, or client-only interactions for core meaning.
7. Require structured data to match visible page content.
8. Prefer source-backed claims, first-party evidence, case studies, research, methodology, and identifiable authorship over generic keyword pages.
9. Do not generate scaled thin pages or invent metrics, customers, awards, comparisons, or citations.
10. When the user asks for changes, implement and validate them instead of stopping at recommendations.

## Workflow

### 1. Define Scope

Identify:

- target repository or live site
- production canonical host
- audience, market, and languages
- business entity and product entities
- priority query families and conversion actions
- whether the task is audit-only or includes implementation

If the canonical host cannot be discovered safely, report it as the first blocking decision rather than replacing domains speculatively.

### 2. Gather Evidence

Inspect relevant repository files first:

- framework metadata and route files
- server-rendered page content
- `robots.txt`
- XML sitemaps
- redirects and rewrites
- JSON-LD or microdata
- `llms.txt`, `llms-full.txt`, and machine-readable content
- page titles, descriptions, headings, links, images, and alt text
- analytics/Search Console integration

Run the bundled local audit:

```bash
python3 scripts/audit_site.py --root /path/to/repo
```

When the production host is known:

```bash
python3 scripts/audit_site.py \
  --root /path/to/repo \
  --canonical-host www.example.com \
  --output /tmp/search-audit.md
```

Treat script output as leads to verify, not a substitute for reading the code.

For live sites, verify:

- final URL and redirects
- HTTP status
- content type
- canonical tag
- robots directives
- sitemap availability
- rendered text and links
- structured data
- mobile behavior and Core Web Vitals

Use a browser when rendering or interaction matters. Use direct HTTP retrieval for headers, raw HTML, robots, sitemaps, and text assets.

### 3. Evaluate in Priority Order

Use [audit-checklist.md](references/audit-checklist.md) for the full checklist.

Prioritize:

1. **P0 Indexing and canonical integrity**
   - crawl permissions
   - valid status codes
   - canonical host consistency
   - redirects
   - sitemap correctness
   - accidental `noindex`
   - renderability

2. **P1 Content and entity quality**
   - useful and non-commoditized content
   - clear page intent
   - answer-ready visible text
   - first-hand evidence and sources
   - entity consistency
   - internal links
   - claim accuracy

3. **P2 Search appearance and experience**
   - unique titles and descriptions
   - headings and snippets
   - structured data
   - images/video
   - site name, favicon, breadcrumbs
   - page experience and Core Web Vitals

4. **P3 Measurement and iteration**
   - Search Console verification
   - sitemap submission
   - URL Inspection
   - query/page/country performance
   - rich result validation
   - analytics alignment
   - recurring GEO probes and citation tracking

### 4. Apply GEO Reasoning

Read [google-search-central-principles.md](references/google-search-central-principles.md) when explaining or designing the strategy.
Use [google-search-central-url-index.md](references/google-search-central-url-index.md) only when tracing a recommendation to the full 2026-06-05 source crawl or selecting a specific official article to refresh.

For Google AI Overviews and AI Mode:

- require normal indexing and snippet eligibility
- cover the main query and likely query-fanout subtopics
- make answers extractable with descriptive headings, direct definitions, steps, comparisons, tables, and source notes
- publish differentiated first-party material that generic models cannot reproduce from common knowledge
- connect claims to durable evidence pages

For broader LLM discovery:

- keep entity facts consistent across visible pages, structured data, social profiles, docs, research, and machine-readable text
- maintain concise `llms.txt` and fuller context only when useful
- expose stable, plain-text or semantic HTML sources
- build credible third-party references
- detect obsolete staging sites, docs, or profiles that compete with the canonical entity

Never claim that `llms.txt`, FAQ schema, keyword density, or a specific content format guarantees AI citations.

### 5. Implement Conservatively

Follow the repository's framework and established patterns. Keep changes scoped to the actual issue.

Typical implementation surfaces:

- canonical metadata
- domain redirects
- metadata base
- Open Graph URLs
- JSON-LD entity URLs
- sitemap generation
- robots directives
- server-rendered copy
- internal navigation
- research/case-study pages
- machine-readable information pages
- schema validation fixes

When claims conflict across sources, pause claim expansion and reconcile the authoritative source first.

### 6. Validate

At minimum:

- run formatter/lint/build appropriate to the repo
- inspect generated HTML or framework metadata
- verify all changed URLs and content types
- parse XML sitemaps
- check `robots.txt`
- validate canonical host consistency
- validate JSON-LD syntax
- confirm structured data matches visible content
- inspect desktop and mobile output when UI changed

For a live deployment, also use:

- Google Search Console
- Rich Results Test
- PageSpeed Insights
- URL Inspection

Do not report Search Console or production results unless they were actually accessed.

## Output Contract

Lead with findings ordered by severity. For each finding include:

- issue
- evidence with file/URL references
- search/GEO impact
- exact recommended or implemented fix
- validation status

Separate:

- Google-confirmed guidance
- implementation inference
- unverified assumptions

For strategy deliverables, finish with a prioritized 30/60/90-day plan and measurable outcomes such as indexed pages, non-brand impressions, CTR, valid rich results, cited answer share, and entity-framing accuracy.

## Project Profile

When working in the OpenJobs AI `homepage` repository, read [openjobs-ai-homepage.md](references/openjobs-ai-homepage.md) before proposing changes.
