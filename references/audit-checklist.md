# SEO and GEO Audit Checklist

Use this checklist after inspecting the implementation. Mark each item as confirmed, failed, not applicable, or not verified.

## P0: Crawl, Index, Canonical

- Production canonical host is explicitly known.
- HTTP and HTTPS behavior is intentional.
- Apex and `www` variants redirect consistently.
- Staging/dev hosts are blocked, authenticated, noindexed, or canonicalized appropriately.
- Important URLs return `200`.
- Removed URLs return `404`, `410`, or redirect intentionally.
- No soft-404 behavior.
- `robots.txt` is reachable and syntactically valid.
- Important pages and resources are not blocked.
- Non-search application routes are handled intentionally.
- Important pages do not contain accidental `noindex`.
- Canonical tags are absolute and self-consistent.
- Canonical tags, redirects, internal links, Open Graph URLs, JSON-LD URLs, and sitemaps use the same host.
- Sitemaps contain only canonical, indexable URLs.
- Sitemap URLs return success with the expected content type.
- Sitemap `lastmod` values reflect meaningful changes.
- Search Console property is verified.
- Sitemaps are submitted and processing errors reviewed.

## P1: Rendering and Site Architecture

- Main content is present in server-rendered or reliably rendered HTML.
- Critical links use `<a href>`.
- Navigation exposes priority pages.
- Orphan pages are identified.
- Anchor text is descriptive.
- URL paths are stable and readable.
- Pagination/infinite scroll has crawlable URL states if applicable.
- Lazy-loaded content is testable and not interaction-only.
- Mobile content has parity with desktop.
- Status codes remain meaningful through framework routing.

## P1: Content and Entity

- Each page has one primary user intent.
- The first screen clearly identifies the brand/product/topic.
- A direct definition or answer appears early.
- H1 is unique and descriptive.
- H2/H3 sections cover real subquestions.
- Content contains original evidence, examples, methodology, research, or experience.
- Authors/reviewers and dates are present where credibility depends on them.
- Claims can be traced to a public or internal authoritative source.
- Exact metrics include scope, denominator, time range, and methodology where needed.
- Customer names, logos, awards, and partnerships are authorized.
- Brand name, product name, category, audience, and core description are consistent across sources.
- Old docs, staging sites, profiles, and third-party listings do not contradict the canonical entity.
- Content avoids thin keyword variants and generic AI summaries.

## P2: Page Metadata

- Every indexable page has a unique title.
- Important pages have unique descriptions.
- Titles and descriptions match visible content.
- Titles avoid keyword stuffing and excessive boilerplate.
- Metadata is valid inside `<head>`.
- Open Graph and social metadata use canonical URLs and working images.
- `html lang` matches the content language.
- Localized pages have correct alternate annotations.

## P2: Structured Data

- JSON-LD parses.
- Types are supported and relevant.
- Organization URL, logo, contact, and sameAs are correct.
- WebSite name and URL are consistent.
- SoftwareApplication facts match the product page.
- FAQ markup matches visible FAQs.
- Article markup includes truthful author/date/headline/image data.
- Breadcrumb markup matches visible hierarchy.
- No unsupported ratings, reviews, prices, or claims.
- Rich Results Test has been run for eligible types.

## P2: Images, Video, Experience

- Meaningful images have useful alt text.
- Decorative images use empty alt text where appropriate.
- Width/height or aspect ratio prevents layout shift.
- Important information is not embedded only in images.
- Video has a crawlable landing page and supporting text when search visibility matters.
- Core Web Vitals are checked.
- Intrusive interstitials do not block primary content.
- Mobile viewport and text sizing are usable.

## GEO Readiness

- Core entity definition is concise and consistent.
- Priority buyer questions have direct answers.
- Related subquestions anticipated by query fanout are covered.
- Comparisons state criteria and limits fairly.
- Evidence pages are stable and linkable.
- Research/case studies include methods and dates.
- Machine-readable text pages are optional supplements, not the only source.
- `llms.txt` uses canonical URLs and only verified facts.
- Third-party profiles and references reinforce the same entity.
- GEO probes record exact query, model, date, brand mention, rank, framing, and cited sources.
- Missing model coverage is disclosed.

## Measurement

- Baseline recorded before major changes.
- Branded and non-branded queries separated.
- Query clusters mapped to landing pages.
- Impressions, clicks, CTR, position, conversions, and indexed pages tracked.
- Rich result validity tracked.
- Crawl/index errors reviewed after releases.
- GEO visibility and citation share tracked separately from Google SEO.

## Suggested Prioritization

- **P0:** blocks crawling/indexing or splits canonical signals.
- **P1:** materially weakens relevance, evidence, entity understanding, or discovery.
- **P2:** improves appearance, CTR, rich results, and experience.
- **P3:** expansion, experimentation, and long-term authority building.

