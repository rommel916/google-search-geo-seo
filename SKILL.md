---
name: google-search-geo-seo
description: >
  Audit, plan, implement, and validate SEO and GEO improvements for websites,
  web apps, documentation sites, and API references. Uses Google Search Central
  as the primary source plus labeled industry evidence from Search Engine Land
  and Semrush. Covers the full stack: technical foundations (crawl, render,
  index, canonical, Core Web Vitals, paginated list pages), on-page content and E-E-A-T, off-page
  authority and backlinks, structured data, llms.txt, multi-platform discovery
  (Google, YouTube, Reddit, LinkedIn, TikTok, AI Overviews, ChatGPT,
  Perplexity), GEO measurement (AI citations, brand mentions, share of voice,
  framing accuracy), growth KPIs (branded search demand, assisted conversions,
  traffic velocity), and landing-page UX. Use for audits, roadmaps, or direct
  implementation; also use to explain how classic SEO maps to GEO/AEO or
  growth-and-visibility strategy.
---

# Google Search GEO and SEO

Apply Google Search Central principles to produce an evidence-based audit and, when requested, implement the fixes. Treat GEO for Google as an extension of SEO, not a separate ranking trick.

Read [seo-growth-visibility-principles.md](references/seo-growth-visibility-principles.md) when framing strategy, prioritizing channels, defining KPIs, or explaining how classic SEO maps to growth and visibility across Google, social discovery surfaces, and AI tools.

## Strategic Frame

Use this operating model from industry guidance:

- **Three pillars**: on-page content, technical SEO, and off-page brand/authority
- **Search lifecycle**: crawl → render → index → rank; fix the failing stage before optimizing the wrong layer
- **Workflow**: research → plan → create/implement → monitor → analyze/report
- **North star**: growth and visibility across fragmented discovery surfaces, not rankings alone

SEO specialties such as ecommerce, enterprise, international, local, and news still sit on top of these pillars. Ranking factors overlap and change by query, device, locale, and intent; do not treat any fixed factor list as complete or permanent.

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
- priority query families, keyword clusters, and conversion actions
- discovery channels the audience actually uses: Google, YouTube, Reddit, LinkedIn, TikTok, Instagram, marketplaces, or named AI tools
- whether the target includes product documentation, API references, versioned docs, or developer examples
- target AI surfaces, such as Google AI Overviews/AI Mode, ChatGPT, Perplexity, or other named systems
- competitors and a repeatable prompt/query set for visibility measurement
- whether the task is audit-only or includes implementation
- baseline KPIs beyond rankings: branded search demand, assisted conversions, referral traffic by channel, and AI citation/framing where measurable

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
- first-party profiles and channels, such as LinkedIn, YouTube, TikTok, Reddit, GitHub, podcasts, webinars, and documentation
- earned sources, such as reviews, independent publications, directories, customer stories, and relevant community discussions
- documentation navigation/config, frontmatter, versioning, deprecation notices, OpenAPI sources, code samples, and generated reference pages when applicable

When research tools are available, use them to inform keyword, trend, backlink, and indexing evidence:

- [Google Search Console](https://search.google.com/search-console)
- [Google Trends](https://trends.google.com/trends/)
- [Ahrefs Backlink Checker](https://ahrefs.com/backlink-checker)
- [Semrush Keyword Magic Tool](https://www.semrush.com/analytics/keywordmagic/)

Do not report tool output unless it was actually accessed.

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
   - crawl permissions — including AI crawlers: `OAI-SearchBot`, `GPTBot`, `PerplexityBot`, `ClaudeBot`
   - valid status codes
   - canonical host consistency
   - redirects
   - sitemap correctness
   - accidental `noindex`
   - paginated list URLs: self-referencing canonicals, crawlable next/previous links, and no blanket `noindex` on page 2+ that strands detail pages
   - renderability
   - Search Console property verified and sitemap submitted (without this, ongoing diagnosis is blind)

2. **P1 Content and entity quality**
   - useful and non-commoditized content
   - clear page intent and keyword-cluster coverage
   - answer-ready visible text using the AI inverted pyramid (direct answer first)
   - passages that pass the isolation test: named entities, self-contained meaning, verifiable specifics
   - first-hand evidence, statistics with scope and date, and expert attribution
   - E-E-A-T signals through authorship, experience, and credible references
   - entity consistency across owned and credible third-party sources
   - accurate category, audience, product, and expertise associations
   - terminology, version, limits, errors, and examples that match the product
   - internal links and topical content clusters
   - visible "last updated" dates on cornerstone and frequently-changing pages
   - claim accuracy

3. **P2 Search appearance and experience**
   - unique titles and descriptions
   - headings and snippets
   - structured data
   - images/video
   - site name, favicon, breadcrumbs
   - page experience and Core Web Vitals

4. **P3 Measurement and iteration**
   - URL Inspection for key pages
   - query/page/country performance in Search Console
   - rich result validation
   - analytics alignment and goal tracking
   - branded vs non-branded query separation
   - referral traffic from social and community discovery surfaces
   - assisted conversions and landing-page conversion quality
   - traffic velocity for new or refreshed content
   - recurring GEO probes and citation tracking using a stable, repeatable prompt set
   - Share of Model (SoM): brand mentions ÷ total tracked competitor mentions per platform and topic cluster
   - competitor share of voice, mention context, sentiment, and framing accuracy

### 4. Apply GEO Reasoning

Read [google-search-central-principles.md](references/google-search-central-principles.md) when explaining or designing the strategy.
Read [pagination-seo-principles.md](references/pagination-seo-principles.md) when auditing or implementing paginated archives, category lists, job boards, search results, blog indexes, or any `/page/2`-style URLs; clarify that indexed pagination is normal and is not automatically self-cannibalization when canonicals, titles, and crawl paths are correct.
Read [seo-growth-visibility-principles.md](references/seo-growth-visibility-principles.md) when framing multi-channel discovery, audience-first planning, brand visibility, growth KPIs, or the shift from rankings-only thinking.
Read [industry-geo-visibility-principles.md](references/industry-geo-visibility-principles.md) when the task includes broader AI platforms, content extractability, off-site brand presence, reputation, citations, mentions, or GEO measurement.
Read [geo-research-principles.md](references/geo-research-principles.md) when optimizing content for AI citation: apply the three-level structural model, AI inverted pyramid, anchorable statements, passage isolation test, content freshness, AI crawler access, schema priority, SoM measurement, and AI Overviews keyword targeting.
Read [technical-documentation-geo.md](references/technical-documentation-geo.md) when auditing or editing documentation, API references, developer guides, code examples, versioned docs, `llms.txt`, or AI crawler access.
Use [google-search-central-url-index.md](references/google-search-central-url-index.md) only when tracing a recommendation to the full 2026-06-05 source crawl or selecting a specific official article to refresh.

For Google AI Overviews and AI Mode:

- require normal indexing and snippet eligibility
- cover the main query and likely query-fanout subtopics
- apply the AI inverted pyramid: open with a 40–60 word direct answer, follow with context, structured evidence, and a follow-up heading
- make each passage pass the isolation test: it must name all entities and answer its own question without surrounding context
- publish differentiated first-party material that generic models cannot reproduce from common knowledge
- connect claims to durable evidence pages with visible timestamps
- use question-aligned H2/H3 headings; target 3–5 word informational queries with low-to-medium difficulty

For broader LLM discovery:

- keep entity facts consistent across visible pages, structured data, social profiles, docs, research, and machine-readable text
- write anchorable statements: named entity + stated relationship + preserved conditions + verifiable specifics
- use descriptive headings and put the direct answer or conclusion early
- apply three-level structure: macro (document architecture), meso (information chunking), micro (visual emphasis)
- maintain concise `llms.txt` and fuller context only when useful
- expose stable, plain-text or semantic HTML sources
- verify `robots.txt` allows key AI crawlers: `OAI-SearchBot`, `GPTBot`, `PerplexityBot`, `ClaudeBot`; evaluate each separately against its actual purpose
- build substantive owned presence on relevant platforms and earn credible independent references
- coordinate insights across Google, YouTube, Reddit, LinkedIn, and other channels the audience actually uses
- distinguish retrieval-based visibility from slower, unobservable base-model training effects
- detect obsolete staging sites, docs, or profiles that compete with the canonical entity
- refresh cornerstone content regularly and include visible "last updated" timestamps

For multi-platform visibility:

- do not require one owner to operate every channel; recommend the highest-impact surfaces for the audience
- map keyword/topic research across Google and at least one additional discovery channel when justified
- treat Reddit participation, LinkedIn authorship, and YouTube explainers as both distribution and corroboration, not spammy republishing
- ensure landing pages receiving cross-channel traffic are fast, mobile-usable, and aligned with intent

Never claim that `llms.txt`, FAQ schema, keyword density, a specific content format, backlinks, reviews, or cross-platform publishing guarantees AI citations.

### 5. Implement Conservatively

Follow the repository's framework and established patterns. Keep changes scoped to the actual issue.

Typical implementation surfaces:

- canonical metadata
- paginated list templates: per-page self-referencing canonicals, unique titles, crawlable `<a href>` pagination, and sitemap inclusion where indexable
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
- landing-page UX fixes that improve conversion for SEO and cross-channel traffic

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

For strategy deliverables, finish with a prioritized 30/60/90-day plan that covers technical foundations, owned content, earned authority, multi-platform distribution where justified, landing-page UX, and measurement. Use outcomes such as indexed pages, non-brand impressions, CTR, valid rich results, branded search demand, referral traffic by channel, assisted conversions, traffic velocity, citation frequency, mention rate, competitor share of voice, mention context, sentiment, source diversity, and entity-framing accuracy.

## Project Profile

When working in the OpenJobs AI `homepage` repository, read [openjobs-ai-homepage.md](references/openjobs-ai-homepage.md) before proposing changes.
