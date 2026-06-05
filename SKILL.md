---
name: google-search-geo-seo
description: Audit, plan, implement, and validate SEO and GEO improvements using Google Search Central guidance plus clearly labeled industry evidence. Use when Codex needs to review or modify a website, web app, documentation site, API reference, repository, metadata, canonical URLs, robots.txt, sitemaps, structured data, JavaScript-rendered content, llms.txt files, answer-ready or extractable content, code examples, entity consistency, third-party brand presence, Search Console measurement plans, AI citations, mentions, sentiment, share of voice, or generative AI search visibility. Also use for requests to explain how Google SEO relates to GEO/AEO, prioritize search issues, or turn a search/GEO audit into concrete code, content, documentation, distribution, and measurement changes.
---

# Google Search GEO and SEO

Apply Google Search Central principles to produce an evidence-based audit and, when requested, implement the fixes. Treat GEO for Google as an extension of SEO, not a separate ranking trick.

## Core Rules

1. Establish the intended production canonical domain before changing URLs.
2. Inspect the real repository and rendered/live output; do not infer implementation from filenames alone.
3. Use official Google Search documentation as the primary source. For current or changed guidance, browse official `developers.google.com/search` and `support.google.com/webmasters` pages.
4. Distinguish Google-confirmed requirements, third-party observations, vendor claims, recommendations, and your own inference.
5. Treat `llms.txt` and machine-readable text pages as supplementary GEO surfaces, not Google ranking requirements.
6. Keep important content visible as crawlable text. Do not rely on images, canvas, animation, or client-only interactions for core meaning.
7. Require structured data to match visible page content.
8. Prefer source-backed claims, first-party evidence, case studies, research, methodology, and identifiable authorship over generic keyword pages.
9. Do not generate scaled thin pages or invent metrics, customers, awards, comparisons, or citations.
10. When the user asks for changes, implement and validate them instead of stopping at recommendations.
11. Treat GEO as probability and brand visibility work, not a stable rank that can be guaranteed.
12. Evaluate owned and earned presence beyond the website without manufacturing reviews, community posts, or third-party endorsements.

## Workflow

### 1. Define Scope

Identify:

- target repository or live site
- production canonical host
- audience, market, and languages
- business entity and product entities
- priority query families and conversion actions
- whether the target includes product documentation, API references, versioned docs, or developer examples
- target AI surfaces, such as Google AI Overviews/AI Mode, ChatGPT, Perplexity, or other named systems
- competitors and a repeatable prompt/query set for visibility measurement
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
- first-party profiles and channels, such as LinkedIn, YouTube, GitHub, podcasts, webinars, and documentation
- earned sources, such as reviews, independent publications, directories, customer stories, and relevant community discussions
- documentation navigation/config, frontmatter, versioning, deprecation notices, OpenAPI sources, code samples, and generated reference pages when applicable

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
   - self-contained passages with conclusions and definitions front-loaded
   - first-hand evidence and sources
   - entity consistency across owned and credible third-party sources
   - accurate category, audience, product, and expertise associations
   - terminology, version, limits, errors, and examples that match the product
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
   - competitor share of voice, mention context, and sentiment

### 4. Apply GEO Reasoning

Read [google-search-central-principles.md](references/google-search-central-principles.md) when explaining or designing the strategy.
Read [industry-geo-visibility-principles.md](references/industry-geo-visibility-principles.md) when the task includes broader AI platforms, content extractability, off-site brand presence, reputation, citations, mentions, or GEO measurement.
Read [technical-documentation-geo.md](references/technical-documentation-geo.md) when auditing or editing documentation, API references, developer guides, code examples, versioned docs, `llms.txt`, or AI crawler access.
Use [google-search-central-url-index.md](references/google-search-central-url-index.md) only when tracing a recommendation to the full 2026-06-05 source crawl or selecting a specific official article to refresh.

For Google AI Overviews and AI Mode:

- require normal indexing and snippet eligibility
- cover the main query and likely query-fanout subtopics
- make answers extractable with descriptive headings, direct definitions, steps, comparisons, tables, and source notes
- publish differentiated first-party material that generic models cannot reproduce from common knowledge
- connect claims to durable evidence pages

For broader LLM discovery:

- keep entity facts consistent across visible pages, structured data, social profiles, docs, research, and machine-readable text
- make definitions, explanations, comparisons, and key facts understandable when extracted without surrounding paragraphs
- use descriptive headings and put the direct answer or conclusion early
- maintain concise `llms.txt` and fuller context only when useful
- expose stable, plain-text or semantic HTML sources
- build substantive owned presence on relevant platforms and earn credible independent references
- distinguish retrieval-based visibility from slower, unobservable base-model training effects
- detect obsolete staging sites, docs, or profiles that compete with the canonical entity

Never claim that `llms.txt`, FAQ schema, keyword density, a specific content format, backlinks, reviews, or cross-platform publishing guarantees AI citations.

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
- answer-first definitions, comparisons, methodology, source notes, and evidence blocks
- documentation titles/descriptions, question-aligned headings, terminology, version notes, limits, error behavior, and runnable examples
- entity-aligned descriptions for owned profiles and documentation
- editorial plans for useful videos, research, expert commentary, webinars, and customer evidence
- ethical outreach or digital PR plans for independent coverage and reviews

When claims conflict across sources, pause claim expansion and reconcile the authoritative source first.
Do not create fake third-party activity. Recommend a channel or outreach workflow when implementation requires a real customer, reviewer, journalist, community member, or account owner.

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
- confirm important passages retain their meaning when read independently
- validate critical code examples, commands, parameters, limits, status codes, version statements, and deprecation guidance when documentation is in scope
- compare core entity descriptions across the website and available external profiles
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
- industry/vendor observations
- implementation inference
- unverified assumptions

For strategy deliverables, finish with a prioritized 30/60/90-day plan that covers technical foundations, owned content, earned authority, and measurement. Use outcomes such as indexed pages, non-brand impressions, CTR, valid rich results, citation frequency, mention rate, competitor share of voice, mention context, sentiment, source diversity, and entity-framing accuracy.

## Project Profile

When working in the OpenJobs AI `homepage` repository, read [openjobs-ai-homepage.md](references/openjobs-ai-homepage.md) before proposing changes.
