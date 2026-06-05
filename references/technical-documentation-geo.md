# Technical Documentation GEO

Use this reference when the target is product documentation, an API reference, a developer portal, SDK guides, versioned docs, or code-heavy educational content.

## Source and Evidence Status

Vendor guide reviewed:

- Mintlify, "GEO guide: Optimize docs for AI search and answer engines"
- Chinese page: https://www.mintlify.com/docs/zh/guides/geo
- Machine-readable page: https://www.mintlify.com/docs/zh/guides/geo.md
- Reviewed: 2026-06-05

Mintlify's content-writing recommendations are useful operating heuristics. Mintlify-specific configuration such as `docs.json`, automatic `llms.txt`, Content-Signal directives, and `mint score` applies only to Mintlify projects.

Cross-check crawler and Google claims against:

- Google AI features: https://developers.google.com/search/docs/appearance/ai-overviews
- Google common crawlers: https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers
- OpenAI crawlers: https://platform.openai.com/docs/bots

## Documentation Content Rules

### Lead With the Answer

Start task-oriented sections with the action, command, definition, or result. Put prerequisites and caveats immediately after the direct answer when they materially affect correctness or safety.

Do not remove necessary warnings merely to make content concise.

### Match Real Developer Intent

Use headings that clearly identify the task or question, such as:

- How do I authenticate API requests?
- What happens when the rate limit is exceeded?
- How do I migrate from API v1 to v2?

Question wording is a useful retrieval heuristic, not a documented ranking requirement. Use descriptive topic headings when they are clearer for readers.

Keep one primary task or intent per page when practical. Split pages when unrelated workflows, products, or versions create ambiguity.

### Be Specific and Verifiable

For parameters, configuration, APIs, and operational behavior, include:

- exact accepted values, types, defaults, and ranges
- units and time windows
- boundary and failure behavior
- HTTP status or error codes
- version availability and deprecation state
- prerequisites and permissions
- complete examples and expected results

Treat vague superlatives as marketing copy, not reference documentation.

### Keep Terminology Stable

Use one canonical name for each concept. Explicitly define aliases only when the product genuinely uses them.

Check consistency across:

- navigation and page titles
- visible prose
- code identifiers
- OpenAPI descriptions
- SDK names
- error messages
- changelogs and migration guides

Do not silently use "API key", "access token", and "API token" as synonyms if they represent different credentials.

## Structure and Parsing

- Use a logical heading hierarchy without meaningless level jumps.
- Keep important explanations self-contained and use explicit nouns instead of context-dependent pronouns.
- Label fenced code blocks with the correct language.
- Include textual explanations for diagrams and screenshots that contain essential information.
- Write useful alt text, but do not claim all AI systems are unable to process images; multimodal capability and retrieval access vary.
- Use concise page titles and descriptions that state the task and relevant product or version.
- Keep critical content in semantic or server-rendered text rather than interaction-only UI.

## Code Example Quality

Do not optimize merely for the presence of code blocks. Validate important examples.

Check:

- syntax and formatting
- current package, API, and SDK versions
- required imports and setup
- placeholder naming and secret handling
- endpoint, method, headers, and request body
- expected response or observable result
- error-handling path
- consistency with the prose and source specification

When execution is feasible and safe, run representative examples or test commands. Otherwise disclose that the example was statically reviewed only.

## Indexing and Version Control

- Include public, current, useful documentation in navigation and crawlable internal links.
- Do not automatically expose private, draft, customer-specific, or unsafe operational content merely to increase AI visibility.
- Handle old versions intentionally with stable version URLs, accurate version labels, migration links, canonicals, redirects, or `noindex` as appropriate.
- Keep removed or unsupported behavior from competing with current guidance.
- Ensure generated API reference pages have stable URLs and useful descriptions rather than thin parameter dumps.

Framework-specific indexing settings must not be presented as general web standards.

## `llms.txt`

Treat `llms.txt` as an optional, emerging convention that can summarize and link to canonical documentation.

- Keep canonical URLs and verified descriptions.
- Do not use it as the only navigation or discovery mechanism.
- Do not describe it as a Google requirement or a formal replacement for XML sitemaps.
- Google states that no special AI text file or markup is required for AI Overviews or AI Mode.
- Verify whether the documentation platform generates it automatically before editing generated output.

## AI Crawler Controls

Review each crawler according to its actual purpose. Do not use "allow AI agents" as a single undifferentiated setting.

### OpenAI

- `OAI-SearchBot`: controls automatic crawling for ChatGPT search results.
- `GPTBot`: controls crawling that may be used to improve generative AI foundation models.
- `ChatGPT-User`: performs some user-triggered visits; it is not an automatic search crawler, is not used to determine Search inclusion, and robots.txt rules may not apply in the same way.

Allowing search crawling does not require allowing model-training crawling. Make the policy decision explicitly.

### Google

- Google Search and its AI features use normal Google Search crawling and indexing controls.
- `Google-Extended` controls certain uses for Gemini model training and grounding outside Google Search.
- `Google-Extended` does not control inclusion or ranking in Google Search, AI Overviews, or AI Mode.

### Other Providers

Verify current official documentation for Anthropic, Perplexity, and any other named provider before changing crawler rules. User-agent names and behavior can change.

Test the deployed `robots.txt`, CDN, WAF, and server logs. A permissive robots rule does not help if infrastructure blocks the crawler.

## Documentation GEO Testing

Create a stable test set from real developer tasks. Record:

- exact question
- platform/model and browsing or search mode
- date, locale, and authentication state
- whether the correct documentation page is cited
- whether the answer uses the current product version
- whether commands and code are correct
- whether limits, errors, and security guidance are accurate
- whether the recommended method is the supported method
- competing or obsolete sources cited

An incorrect AI answer can indicate ambiguous, missing, contradictory, stale, or inaccessible documentation. It can also result from retrieval failure, model behavior, user context, or hallucination. Diagnose before rewriting.

Do not promise a fixed improvement window. Crawling, indexing, retrieval, authority, and platform updates operate on different schedules.

## Implementation Priority

1. Fix inaccessible, blocked, stale, contradictory, or version-confused documentation.
2. Correct unsafe or non-working code examples.
3. Add direct answers, exact behavior, and complete examples to priority tasks.
4. Normalize terminology, metadata, headings, and navigation.
5. Add optional machine-readable indexes when they supplement canonical documentation.
6. Run repeated AI citation and answer-accuracy tests.
