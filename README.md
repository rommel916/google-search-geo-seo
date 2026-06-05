# Google Search GEO & SEO

[中文](#中文) | [English](#english)

## 中文

一个面向 Codex 的 SEO 与生成式引擎优化（GEO）skill。它以 Google Search Central 官方指南为基础，并将行业 GEO 观察作为单独证据层，用于审计、规划、实施和验证网站或技术文档的搜索优化。

这个 skill 不把 GEO 当作独立的排名技巧。对于 Google AI Overviews 和 AI Mode，正常的抓取、索引、摘要资格、内容质量和搜索体验仍然是基础。

### 主要能力

- 审计 canonical、重定向、robots、sitemap、HTTP 状态和索引策略
- 检查服务端渲染、JavaScript 内容、可抓取链接和初始 HTML
- 优化标题、描述、H1、内部链接、Open Graph 和结构化数据
- 检查品牌、公司、产品、受众和分类等实体信息的一致性
- 将定义、比较、步骤和关键事实改写为可独立理解、便于检索的内容
- 审计 `llms.txt`、纯文本信息页和其他机器可读内容
- 优化 API 文档、开发者指南、版本说明、错误行为和代码示例
- 分析官网之外的自有内容、独立报道、真实评论和第三方提及
- 设计 AI 引用率、品牌提及率、竞品声量、语境和情感监测方案
- 在用户要求修改时直接实施，并运行构建、Lint、HTML、XML 和 JSON-LD 验证

### 证据分层

Skill 输出会明确区分：

1. **Google 官方确认**：来自 Google Search Central 的要求或说明
2. **平台官方说明**：例如 OpenAI crawler 的具体用途
3. **行业或厂商观察**：例如 Search Engine Land、Semrush、Mintlify 的经验
4. **实施推断**：结合目标网站代码和实际输出得出的工程判断
5. **未验证假设**：当前无法确认、需要进一步获取数据的内容

`llms.txt`、FAQ schema、关键词密度或特定内容格式都不能保证获得 AI 引用。

### 技术文档 GEO

针对 API 和开发者文档，skill 会额外检查：

- 页面是否围绕一个清晰任务或概念
- 是否直接给出操作、命令、定义或结果
- 参数类型、默认值、范围、单位和边界行为
- HTTP 状态码、错误码、权限和安全说明
- 当前版本、预览功能、弃用和迁移信息
- 代码示例是否包含必要导入、请求参数和预期结果
- 文档、OpenAPI、SDK、导航和错误消息中的术语是否一致
- 旧版本页面是否正确使用版本 URL、canonical、重定向或 `noindex`

### AI Crawler 边界

不同 crawler 的用途不能混为一谈：

- `OAI-SearchBot`：用于 ChatGPT Search 的自动搜索抓取
- `GPTBot`：用于可能参与基础模型改进的抓取
- `ChatGPT-User`：用户触发的访问，不是自动搜索 crawler
- `Google-Extended`：控制部分 Gemini 训练和 grounding 用途，不控制 Google Search、AI Overviews 或 AI Mode 的收录与排名

是否允许搜索抓取、模型训练或用户触发访问，应根据业务和内容政策分别决定。

### 安装

使用 GitHub CLI：

```bash
mkdir -p ~/.codex/skills
gh repo clone rommel916/google-search-geo-seo ~/.codex/skills/google-search-geo-seo
```

如果目录已经存在：

```bash
git -C ~/.codex/skills/google-search-geo-seo pull
```

### 使用

在 Codex 中明确调用：

```text
使用 $google-search-geo-seo 审计这个网站，并直接修复优先级最高的 SEO/GEO 问题。
```

```text
使用 $google-search-geo-seo 检查这套 API 文档是否容易被 Google、ChatGPT 和 Perplexity 准确检索和引用。
```

```text
使用 $google-search-geo-seo 制定 30/60/90 天的 SEO、内容、第三方声誉和 AI 可见度方案。
```

### 本地静态审计

```bash
python3 scripts/audit_site.py --root /path/to/repository
```

指定生产 canonical host：

```bash
python3 scripts/audit_site.py \
  --root /path/to/repository \
  --canonical-host www.example.com \
  --output /tmp/search-audit.md
```

审计脚本用于发现线索，不能替代代码阅读、构建验证、真实 HTTP 检查或 Search Console。

### 优先级

- **P0**：抓取、索引、状态码、canonical、重定向和渲染问题
- **P1**：内容价值、实体理解、来源、术语和答案准确性
- **P2**：标题、摘要、结构化数据、图片、视频和页面体验
- **P3**：内容扩展、第三方声誉、AI 探测和持续测量

### 仓库结构

```text
google-search-geo-seo/
├── README.md
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

### 验证

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
python3 -m py_compile scripts/audit_site.py
git diff --check
```

## English

A Codex skill for search engine optimization and generative engine optimization (GEO). It uses official Google Search Central guidance as its foundation and keeps broader industry GEO observations in a separate evidence layer. It can audit, plan, implement, and validate improvements for websites and technical documentation.

The skill does not treat GEO as a separate ranking trick. For Google AI Overviews and AI Mode, normal crawling, indexing, snippet eligibility, content quality, and search experience remain the foundation.

### Capabilities

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

### Evidence Levels

The skill separates:

1. **Google-confirmed guidance**
2. **Official platform documentation**, such as crawler-specific behavior
3. **Industry or vendor observations**, including Search Engine Land, Semrush, and Mintlify
4. **Implementation inference** based on the target codebase and rendered output
5. **Unverified assumptions** that require additional access or data

`llms.txt`, FAQ schema, keyword density, or a specific content format cannot guarantee AI citations.

### Technical Documentation GEO

For API and developer documentation, the skill also checks:

- Whether each priority page serves one clear task or concept
- Whether the action, command, definition, or result appears early
- Parameter types, defaults, ranges, units, and boundary behavior
- HTTP status codes, errors, permissions, and security guidance
- Current, preview, deprecated, and migration information
- Required imports, request details, and expected results in code examples
- Terminology consistency across docs, OpenAPI, SDKs, navigation, and errors
- Intentional handling of old versions through versioned URLs, canonicals, redirects, or `noindex`

### AI Crawler Boundaries

Crawler purposes must be evaluated separately:

- `OAI-SearchBot`: automatic crawling for ChatGPT Search
- `GPTBot`: crawling that may be used to improve foundation models
- `ChatGPT-User`: user-triggered visits, not an automatic search crawler
- `Google-Extended`: controls certain Gemini training and grounding uses; it does not control inclusion or ranking in Google Search, AI Overviews, or AI Mode

Search retrieval, model training, and user-triggered access are separate policy decisions.

### Installation

Using GitHub CLI:

```bash
mkdir -p ~/.codex/skills
gh repo clone rommel916/google-search-geo-seo ~/.codex/skills/google-search-geo-seo
```

To update an existing installation:

```bash
git -C ~/.codex/skills/google-search-geo-seo pull
```

### Usage

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

### Local Static Audit

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

### Priority Model

- **P0**: crawling, indexing, status, canonical, redirect, and rendering failures
- **P1**: content value, entity understanding, evidence, terminology, and answer accuracy
- **P2**: metadata, structured data, media, and page experience
- **P3**: content expansion, earned authority, AI probes, and ongoing measurement

### Repository Structure

```text
google-search-geo-seo/
├── README.md
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

### Validation

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
python3 -m py_compile scripts/audit_site.py
git diff --check
```

## 资料来源 / Sources

- [Google Search Central documentation](https://developers.google.com/search/docs)
- [Google AI features and your website](https://developers.google.com/search/docs/appearance/ai-overviews)
- [OpenAI crawlers](https://platform.openai.com/docs/bots)
- [Search Engine Land GEO framework](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418)
- [Mintlify GEO guide](https://www.mintlify.com/docs/zh/guides/geo)
