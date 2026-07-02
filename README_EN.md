# Google Search GEO & SEO

[中文](README.md)

A Codex skill for search engine optimization and generative engine optimization (GEO). It uses official Google Search Central guidance as its foundation and keeps broader industry GEO observations in a separate evidence layer. It can audit, plan, implement, and validate improvements for websites, web apps, and technical documentation.

The skill does not treat GEO as a separate ranking trick. For Google AI Overviews and AI Mode, normal crawling, indexing, snippet eligibility, content quality, and search experience remain the foundation.

## Capabilities

- Audit using the SEO three-pillar model: on-page content, technical infrastructure, and off-page brand/authority
- Trace failures to the correct search lifecycle stage — crawl → render → index → rank — before optimizing the wrong layer
- Audit canonicals, redirects, robots directives, sitemaps, HTTP status codes, and indexing policy
- Inspect server rendering, JavaScript content, crawlable links, and initial HTML
- Improve titles, descriptions, headings, internal links, Open Graph data, and structured data
- Check entity consistency across company, product, audience, category, and external profiles
- Make definitions, comparisons, procedures, and key facts understandable when retrieved independently
- Review `llms.txt`, plain-text information pages, and other machine-readable content
- Improve API documentation, developer guides, versioning, error behavior, and code examples
- Evaluate owned content, independent coverage, authentic reviews, and third-party mentions
- Plan multi-platform discovery strategy across Google, YouTube, Reddit, LinkedIn, TikTok, and AI tools
- Design growth and visibility KPIs: branded search demand, assisted conversions, traffic velocity
- Design measurement for AI citations, brand mentions, competitor share of voice, and sentiment
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
Use $google-search-geo-seo to create a 30/60/90-day plan for SEO, content, earned authority, multi-platform visibility, and AI discoverability.
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

- **P0**: crawling, indexing, status, canonical, redirect, rendering failures, and Search Console setup
- **P1**: content value, entity understanding, E-E-A-T, evidence quality, and answer accuracy
- **P2**: metadata, structured data, media, and page experience
- **P3**: multi-platform expansion, iterative measurement, AI probes, and long-term authority building

## SEO Learning Guide

The following synthesizes two Search Engine Land guides: [What Is SEO](https://searchengineland.com/guide/what-is-seo) and [The Future of SEO](https://searchengineland.com/guide/future-of-seo).

### What SEO Is

**SEO (Search Engine Optimization)** is the practice of optimizing websites and digital content to increase visibility, traffic, and brand authority across search engines and AI search. It ensures brands are found accurately wherever people and AI retrieve information.

### Three Pillars

| Pillar | Role | Controllability |
|--------|------|-----------------|
| **On-page (content)** | Offense | Fully controllable |
| **Technical SEO** | Defense | Fully controllable |
| **Off-page (brand & authority)** | Audience | Influenceable, not fully controllable |

**On-page essentials:** keyword clusters, unique titles/meta/headings/URLs, internal links, E-E-A-T (experience, expertise, authoritativeness, trustworthiness), multimedia, and up-to-date accuracy.

**Technical essentials:** crawlable architecture, rendering visibility, canonical/noindex/sitemap management, Core Web Vitals, mobile parity, HTTPS, structured data that matches visible content.

**Off-page essentials:** high-quality backlinks (quality over quantity), brand mentions and branded search demand, PR, content marketing, reviews, and directory accuracy.

### How Search Engines Work

```
Crawl → Render → Index → Rank
```

Identify which stage is failing before optimizing the wrong layer.

### SEO Workflow

1. **Research** — audience, keywords, competitors, SERP intent
2. **Planning** — goals, KPIs, timelines, owners, budget
3. **Create and implement** — new content, page improvements, content pruning
4. **Monitor** — traffic drops, index loss, broken links, rendering failures
5. **Analyze and report** — compare periods, explain impact, reprioritize

SEO is ongoing. Meaningful results typically take 3–6 months; competitive keywords take longer.

### SEO vs SEM vs PPC

- **SEO** = organic (non-paid) search traffic
- **PPC** = pay-per-click advertising
- **SEM** = SEO + PPC combined

GEO extends SEO — it does not replace crawlability, content quality, or page experience.

### The Future of SEO: Growth & Visibility

The north star has shifted from rankings alone to **growth and visibility** across fragmented discovery surfaces.

Users now discover information through Google, YouTube, TikTok, Reddit, LinkedIn, Instagram, marketplaces, and generative AI tools. Key industry observations (Semrush 2025; treat as vendor data, verify before citing):

- AI search is projected to surpass traditional search by 2028
- ~90% of ChatGPT citations come from pages ranked position 20+; similar patterns in Perplexity and Google LLMs
- The average AI search visitor converts at ~4.4× the rate of the average organic visitor
- Reddit organic traffic grew 500%+ between Jan 2022 and Jan 2025

**Platform strategy:** choose the highest-impact channels for your audience — YouTube (titles, descriptions, chapters, Video Schema), Reddit (authentic community presence), LinkedIn (expert authorship, company profile, `sameAs` Schema), TikTok (keywords in scripts and captions).

**Audience-first strategy:** map intent by channel and moment; use behavioral segmentation and first-party data; apply attention mapping (heatmaps, watch time, scroll depth).

**Brand as visibility multiplier:** branded search volume, unlinked brand mentions, and share of voice in AI summaries compound SEO over time.

**AI-native content patterns:**

| Pattern | How |
|---------|-----|
| Question-aligned headings | Real user questions as H2/H3 with complete answers below |
| Data ingestion | Clear headings, concise answers, tables |
| Source architecture | Stable evidence pages with methodology and author attribution |
| Attribution strategy | Identifiable authors, `sameAs` links, earned references |

**New KPIs:** traffic velocity, assisted conversions, AI citation frequency, referral traffic by channel, competitor share of voice, branded search demand.

**UX matters:** driving traffic to a slow or misaligned landing page wastes SEO effort. Key pages must be fast, mobile-usable, intent-aligned, and set up to convert.

### Action Checklist

**Foundations:**
1. Verify indexing and crawl access in Search Console
2. Align each page with one search intent; outperform SERP competitors
3. Build keyword research → content clusters → internal linking workflow
4. Monitor continuously; prune underperforming content quarterly

**Growth and visibility:**
5. Map where your audience discovers information
6. Pick 1–2 non-Google platforms and cross-reference keyword research
7. Use question-aligned headings with complete first-paragraph answers
8. Track branded search, AI citations, and assisted conversions — not only rankings
9. Add author attribution, LinkedIn expert profiles, and `sameAs` Schema
10. Optimize landing-page UX so cross-channel traffic can convert

## Practical Tools

| Tool | Use |
|------|-----|
| [Google Search Console](https://search.google.com/search-console) | Monitor indexing, crawl errors, queries, CTR, and Core Web Vitals |
| [Ahrefs Backlink Checker](https://ahrefs.com/backlink-checker) | Quick backlink and referring-domain snapshot |
| [Google Trends](https://trends.google.com/trends/) | Compare keyword demand, seasonality, and related queries |
| [Semrush Keyword Magic Tool](https://www.semrush.com/analytics/keywordmagic/) | Keyword research, clustering, search volume, and difficulty |

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
    ├── geo-research-principles.md
    ├── google-search-central-principles.md
    ├── google-search-central-url-index.md
    ├── industry-geo-visibility-principles.md
    ├── seo-growth-visibility-principles.md
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
- [Princeton et al., GEO: Generative Engine Optimization (paper)](https://arxiv.org/html/2311.09735v3)
- [GEO-SFE: Structural Feature Engineering for GEO (paper)](https://arxiv.org/abs/2603.29979v1)
- [Search Engine Land: What Is SEO](https://searchengineland.com/guide/what-is-seo)
- [Search Engine Land: The Future of SEO](https://searchengineland.com/guide/future-of-seo)
- [Search Engine Land: Mastering GEO in 2026](https://searchengineland.com/mastering-generative-engine-optimization-in-2026-full-guide-469142)
- [Search Engine Land: How to write for AI search](https://searchengineland.com/ai-search-playbook-machine-readable-content-472412)
- [Search Engine Land: AI Overviews optimization guide](https://searchengineland.com/guide/how-to-optimize-for-ai-overviews)
- [Search Engine Land GEO framework](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418)
- [Mintlify GEO guide](https://www.mintlify.com/docs/zh/guides/geo)
