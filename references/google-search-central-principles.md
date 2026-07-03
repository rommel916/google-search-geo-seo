# Google Search Central Principles

This reference distills the Google Search Central material read on 2026-06-05. It is a working synthesis, not a copy of the source articles. Refresh official documentation when the user asks for current guidance or when implementation depends on a potentially changed rule.

## Source Coverage

- 236 links extracted from the Chinese Google Search documentation index.
- 235 links successfully retrieved.
- All 186 links under `https://developers.google.com/search/docs` successfully retrieved.
- One non-core podcast aggregation link returned HTTP 429.

## Primary Sources

- Search documentation index: https://developers.google.com/search/docs?hl=zh-cn
- Search Essentials: https://developers.google.com/search/docs/essentials?hl=zh-cn
- SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=zh-cn
- Helpful content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=zh-cn
- Generative AI content: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content?hl=zh-cn
- Generative AI search optimization: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=zh-cn
- AI features: https://developers.google.com/search/docs/appearance/ai-features?hl=zh-cn
- Crawlable links: https://developers.google.com/search/docs/crawling-indexing/links-crawlable?hl=zh-cn
- Sitemap creation: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=zh-cn
- Robots introduction: https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=zh-cn
- Canonicalization: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls?hl=zh-cn
- JavaScript SEO: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics?hl=zh-cn
- Title links: https://developers.google.com/search/docs/appearance/title-link?hl=zh-cn
- Snippets and descriptions: https://developers.google.com/search/docs/appearance/snippet?hl=zh-cn
- Structured data introduction: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data?hl=zh-cn
- Structured data policies: https://developers.google.com/search/docs/appearance/structured-data/sd-policies?hl=zh-cn
- Search Console: https://developers.google.com/search/docs/monitor-debug/search-console-start?hl=zh-cn
- Search Console and Analytics: https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console?hl=zh-cn
- Google Trends: https://developers.google.com/search/docs/monitor-debug/trends-start?hl=zh-cn

## Foundational Model

Google Search works through discovery, crawling, rendering, indexing, ranking, and presentation. Improvements must preserve that chain.

The core requirements are:

- Googlebot can access the URL and required resources.
- The server returns a meaningful HTTP status.
- The page contains indexable content.
- The page complies with spam policies.
- Canonical signals are coherent.

Meeting requirements does not guarantee indexing or ranking.

## GEO and AI Search

Google explicitly frames GEO/AEO for its generative search experiences as SEO. AI Overviews and AI Mode use Google's search index, ranking systems, retrieval, and query fanout.

Practical consequences:

- A page must be indexed and eligible for snippets before it can be used as an AI supporting link.
- There is no separate Google AI schema or secret technical requirement.
- Normal SEO remains necessary: crawl access, internal links, visible text, page experience, structured data consistency, and useful content.
- Query fanout rewards broad but coherent topical coverage around the user's main question and related subquestions.
- Unique first-party experience, research, examples, and perspective are more defensible than generic summaries.

## Content Quality

Prefer content that:

- serves an existing or clearly defined audience
- answers a real task or decision
- demonstrates first-hand expertise
- provides original information, research, analysis, or evidence
- has a clear purpose and satisfying conclusion
- identifies authors, sources, methods, and update dates where relevant
- adds substantial value beyond summarizing other pages

Avoid:

- scaled content with little original value
- thin keyword variants
- misleading freshness
- unsupported superlatives or exact metrics
- titles designed mainly for clicks
- content produced for search engines without a real user purpose

AI-assisted content is acceptable when accurate, useful, relevant, and reviewed. Automation does not excuse low quality.

## Crawling and Indexing

- Use crawlable `<a href>` links with descriptive anchor text.
- Use `robots.txt` to control crawling, not to remove indexed URLs.
- Use `noindex` when a reachable page should not be indexed.
- Keep sitemaps at stable URLs and include canonical URLs intended for search.
- Use absolute URLs in sitemaps.
- Use redirects as a strong canonical signal.
- Use `rel="canonical"` as a strong canonical signal.
- Treat sitemap inclusion as a weaker supporting canonical signal.
- Keep canonical tags, redirects, internal links, and sitemaps aligned.
- Return real `404`/`410` statuses for missing content rather than soft-404 pages.

### Pagination

- Give each page in a paginated sequence a **unique URL** and a **self-referencing canonical**. Do not set page 1 as the canonical for the whole sequence.
- Link pages sequentially with crawlable `<a href>` links; consider linking every page back to page 1.
- Use distinct titles for paginated URLs; avoid identical titles across the sequence.
- Do not rely on URL fragments (`#page=2`) as the only pagination state.
- Indexed pagination is normal; later pages are often crawl paths to deeper items, not duplicate homepages.
- Avoid legacy patterns that `noindex` all page-2+ URLs or block `/page/` in `robots.txt` unless there is a documented reason.
- Treat filter/sort/facet parameter URLs separately from true pagination.

See [pagination-seo-principles.md](pagination-seo-principles.md) for audit procedure and evidence labels.

## JavaScript

Google can render JavaScript, but rendering is a separate queued stage. Keep critical content and links available in initial or server-rendered HTML when practical.

Use:

- unique titles and descriptions
- meaningful status codes
- History API for routable views
- correct canonical injection
- crawlable links
- testable lazy loading

Do not hide core meaning exclusively in canvas, animation, hover states, or interactions.

## Search Appearance

### Titles

- Give every indexable page a unique, concise, descriptive title.
- Avoid keyword repetition and long boilerplate.
- Make the main visible heading consistent with page intent.
- Keep brand text concise.

### Descriptions and Snippets

- Google usually creates snippets from page content.
- Write unique descriptions for important pages.
- Summarize the actual page rather than stuffing keywords.
- Ensure the visible text contains the answer you want search systems to extract.

### Structured Data

Structured data helps Google understand entities and may enable rich results. It does not guarantee them.

- Use supported types relevant to the page.
- Prefer JSON-LD when suitable.
- Match all marked-up facts to visible content.
- Do not mark hidden, misleading, or fabricated content.
- Validate syntax and eligibility.

Common SaaS/company types:

- `Organization`
- `WebSite`
- `SoftwareApplication`
- `Article`
- `BreadcrumbList`
- `FAQPage` only when the visible page and current eligibility justify it

## International Sites

- Use separate URLs for materially translated/localized pages.
- Use correct `hreflang` annotations for alternates.
- Keep canonical and hreflang relationships coherent.
- Do not rely only on cookies, geolocation, or browser language to expose localized content.

## Measurement

Search Console is the source for:

- indexing and crawl issues
- sitemap processing
- impressions, clicks, CTR, and position
- query, page, device, country, and search appearance dimensions

Combine Search Console with analytics to understand what happens before and after the search click. Evaluate changes over weeks, not hours, unless the issue is a clear technical outage.

