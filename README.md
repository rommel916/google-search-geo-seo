# Google Search GEO & SEO

[English](README_EN.md)

一个面向 Codex 的 SEO 与生成式引擎优化（GEO）skill。它以 Google Search Central 官方指南为基础，并将行业 GEO 观察作为单独证据层，用于审计、规划、实施和验证网站或技术文档的搜索优化。

这个 skill 不把 GEO 当作独立的排名技巧。对于 Google AI Overviews 和 AI Mode，正常的抓取、索引、摘要资格、内容质量和搜索体验仍然是基础。

## 主要能力

- 按 SEO 三大支柱审计：On-page 内容、Technical 技术、Off-page 品牌与权威
- 沿 crawl → render → index → rank 生命周期定位问题，而不是只改表层 metadata
- 审计 canonical、重定向、robots、sitemap、HTTP 状态和索引策略
- 检查服务端渲染、JavaScript 内容、可抓取链接和初始 HTML
- 优化标题、描述、H1、内部链接、Open Graph 和结构化数据
- 检查品牌、公司、产品、受众和分类等实体信息的一致性
- 将定义、比较、步骤和关键事实改写为可独立理解、便于检索的内容
- 审计 `llms.txt`、纯文本信息页和其他机器可读内容
- 优化 API 文档、开发者指南、版本说明、错误行为和代码示例
- 分析官网之外的自有内容、独立报道、真实评论和第三方提及
- 规划 Google、YouTube、Reddit、LinkedIn、TikTok 等多平台发现策略
- 设计增长与可见度 KPI：品牌搜索量、辅助转化、AI 引用率、跨渠道 referral
- 设计 AI 引用率、品牌提及率、竞品声量、语境和情感监测方案
- 在用户要求修改时直接实施，并运行构建、Lint、HTML、XML 和 JSON-LD 验证

## 证据分层

Skill 输出会明确区分：

1. **Google 官方确认**：来自 Google Search Central 的要求或说明
2. **同行评审学术研究**：Princeton GEO 论文、GEO-SFE 等经过同行评审的量化研究
3. **平台官方说明**：例如 OpenAI crawler 的具体用途
4. **行业或厂商观察**：例如 Search Engine Land、Semrush、Mintlify 的经验（注意来源立场）
5. **实施推断**：结合目标网站代码和实际输出得出的工程判断
6. **未验证假设**：当前无法确认、需要进一步获取数据的内容

`llms.txt`、FAQ schema、关键词密度或特定内容格式都不能保证获得 AI 引用。

## 技术文档 GEO

针对 API 和开发者文档，skill 会额外检查：

- 页面是否围绕一个清晰任务或概念
- 是否直接给出操作、命令、定义或结果
- 参数类型、默认值、范围、单位和边界行为
- HTTP 状态码、错误码、权限和安全说明
- 当前版本、预览功能、弃用和迁移信息
- 代码示例是否包含必要导入、请求参数和预期结果
- 文档、OpenAPI、SDK、导航和错误消息中的术语是否一致
- 旧版本页面是否正确使用版本 URL、canonical、重定向或 `noindex`

## AI Crawler 边界

不同 crawler 的用途不能混为一谈，须在 `robots.txt` 中逐一决策：

| Crawler | 所属系统 | 用途 |
|---------|---------|------|
| `OAI-SearchBot` | ChatGPT Search | ChatGPT 搜索结果的自动抓取 |
| `GPTBot` | OpenAI | 可能用于基础模型训练的抓取 |
| `ChatGPT-User` | ChatGPT | 用户触发的浏览访问，非自动爬虫 |
| `PerplexityBot` | Perplexity | Perplexity 答案检索抓取 |
| `ClaudeBot` | Anthropic | Claude 知识检索抓取 |
| `Googlebot` | Google Search | 覆盖 Google Search、AI Overviews、AI Mode |
| `Google-Extended` | Google（Gemini 训练） | **不**控制 Google Search 或 AI Overviews |

搜索检索、模型训练和用户触发访问是三类独立的策略决定，应分别配置。CDN 和 WAF 规则可能在 `robots.txt` 之外悄悄屏蔽爬虫，需确认基础设施层。

## 安装

使用 GitHub CLI：

```bash
mkdir -p ~/.codex/skills
gh repo clone rommel916/google-search-geo-seo ~/.codex/skills/google-search-geo-seo
```

如果目录已经存在：

```bash
git -C ~/.codex/skills/google-search-geo-seo pull
```

## 使用

在 Codex 中明确调用：

```text
使用 $google-search-geo-seo 审计这个网站，并直接修复优先级最高的 SEO/GEO 问题。
```

```text
使用 $google-search-geo-seo 检查这套 API 文档是否容易被 Google、ChatGPT 和 Perplexity 准确检索和引用。
```

```text
使用 $google-search-geo-seo 制定 30/60/90 天的 SEO、内容、多平台分发、第三方声誉和 AI 可见度方案，包含 Share of Model 追踪设计。
```

## 本地静态审计

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

## 优先级

- **P0**：抓取、索引、状态码、canonical、重定向、渲染问题，以及 AI 爬虫访问权限和 Search Console 配置
- **P1**：内容价值、E-E-A-T 信号、实体清晰度、答案可提取性、内容新鲜度
- **P2**：标题、摘要、结构化数据、图片/视频、页面体验与 Core Web Vitals
- **P3**：多平台扩展、迭代测量、AI 引用探测（含 SoM 追踪）、长期权威建设

## 仓库结构

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

## 验证

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
python3 -m py_compile scripts/audit_site.py
git diff --check
```

## SEO 学习指南

以下内容整理自 Search Engine Land 的两篇指南：[What Is SEO](https://searchengineland.com/guide/what-is-seo) 与 [The Future of SEO](https://searchengineland.com/guide/future-of-seo)。第一篇讲基础框架，第二篇讲 AI 时代的演进。

### SEO 是什么

**SEO（Search Engine Optimization）** 是优化网站与数字内容，在搜索引擎和 AI 搜索中提升可见度、流量与品牌权威性的实践。它不只是做 Google 排名，而是让品牌在人们和 AI 获取信息的各个触点都能被准确找到。

### 三大支柱

| 支柱 | 角色 | 可控性 |
|------|------|--------|
| **On-page（内容优化）** | 进攻 | 完全可控 |
| **Technical SEO（技术优化）** | 防守 | 完全可控 |
| **Off-page（品牌与权威）** | 粉丝/口碑 | 可影响，不可完全控制 |

**On-page 要点：**

- 对齐搜索意图，提供比 SERP 竞品更有用的内容
- 关键词集群（如 "what is SEO"、"seo meaning" 同页覆盖）
- Title、Meta、H1–H6、内链、URL、图片 alt、Open Graph
- E-E-A-T：经验、专业、权威、可信

**Technical 要点：**

- 可爬取、可渲染、可索引
- 站点架构、Core Web Vitals、移动优先、HTTPS
- Canonical、noindex、sitemap、结构化数据（Schema）

**Off-page 要点：**

- 高质量外链（质量 > 数量）
- 品牌提及、品牌搜索量、口碑管理
- PR、内容营销、社媒、目录与评价

### 搜索引擎如何工作

```
爬取 (Crawl) → 渲染 (Render) → 索引 (Index) → 排名 (Rank)
```

SEO 的本质，是在每个阶段提供正确信号。

### SEO 工作流程

1. **Research** — 受众、关键词、竞品、SERP 分析
2. **Planning** — 目标、KPI、预算、团队
3. **Create & Implement** — 新内容、优化旧页、内容修剪（pruning）
4. **Monitor** — 流量骤降、索引丢失、链接失效
5. **Analyze & Report** — 用数据驱动迭代

SEO 不是一次性项目，而是持续运营。通常 3–6 个月才见明显效果。

### 与 SEM / PPC / GEO 的关系

- **SEM（搜索营销）** = SEO（自然流量）+ PPC（付费流量）
- **GEO（生成式引擎优化）** = SEO 的延伸，不是替代

### SEO 的未来：增长与可见度

旧模式是关键词排名 + 蓝色链接点击；新模式是 **Growth & Visibility（增长与可见度）**。SEO 从业者正在变成「增长与可见度专家」——不只盯 Google 排名，而是驱动品牌在碎片化发现生态中的整体表现。

**搜索不再只发生在 Google：**

| 平台 | 用途 |
|------|------|
| Google | 传统搜索，仍占主导但份额持续变化 |
| TikTok | 视觉灵感、趋势、产品发现 |
| YouTube | 深度教程，且视频常出现在 Google SERP |
| Reddit | 真实社区意见，SERP 曝光显著增长 |
| LinkedIn | B2B 权威、E-E-A-T、文章可排名 Google |
| Instagram | 产品发现、品牌验证 |
| ChatGPT / Perplexity | 对话式摘要，减少点击 |

**行业观察（Semrush 2025 研究）：**

- AI 搜索有望在 2028 年超过传统搜索
- 零点击搜索增多（AI 直接在 SERP 给答案）
- ChatGPT 约 90% 引用的是排名 20 位以后的页面
- AI 搜索访客的转化价值约为普通自然搜索访客的 4.4 倍

不必只 obsession 第一名；深度内容、品牌权威、多平台布局同样重要。

### 多平台策略

不必精通所有平台，但要战略性地选择目标受众所在的渠道：

- **TikTok**：关键词放在视频脚本、字幕、标注
- **YouTube**：单独做 YouTube + Google 关键词研究；加章节、Video Schema
- **Reddit**：在相关 subreddit 建立品牌存在感
- **LinkedIn**：个人 + 公司双轨；用 `sameAs` Schema 关联实体

小团队选 1–2 个高影响渠道做深；大品牌跨平台协调，把各渠道洞察互相反哺。

### 受众优先，而非关键词优先

- **行为细分**：按动作分群，而非人口统计
- **注意力地图**：热图、视频完播率、滚动深度
- **意图驱动**：同一个人在不同平台意图不同
- **第一方数据**：隐私收紧后，自有行为数据更重要

### 品牌 = 可见度倍增器

E-E-A-T 已从 SEO checklist 升级为品牌战略。可量化的新指标包括：品牌搜索量增长、无链接品牌提及、AI 摘要中的声量份额、跨渠道一致性带来的复利效应。

### AI 原生内容策略

生成式引擎在**段落级别**评估内容，而非页面整体。一个结构清晰的段落即可赢得引用，无需全站跻身排名前十。

#### 三层内容结构（GEO-SFE 研究，2026）

跨六个生成式引擎的研究发现，独立于语义内容的结构优化可带来约 17% 的引用率提升：

| 层级 | 对应内容 | 做法 |
|------|---------|------|
| **宏观结构**（文档架构） | 每页一个主题，先答后述 | 首屏直接命名主题并回答核心问题 |
| **中观结构**（信息分块） | 每块一个完整想法 | TL;DR 摘要紧跟标题；表格用于对比 |
| **微观结构**（视觉强调） | 关键事实加粗、列表、编号步骤 | 代码块声明语言；格式规范统一 |

#### AI 倒金字塔写作模式

LLM 优先从段落开头和结尾提取观点，把核心答案前置：

1. **直接答案**（40–60 词）：用明确实体和动词的陈述句，不用代词和被动语态
2. **上下文与限定条件**：资格限制、例外、权衡
3. **结构化证据**：带来源和日期的数据、表格、编号步骤
4. **后续对齐**：把下一个逻辑问题设为明确的 H2/H3 标题

#### 锚定陈述（Anchorable Statements）

每条重要声明应能被 AI 单独引用，包含四要素：

- **命名实体**：写「Notion 团队版」而非「该方案」
- **明确关系**：用清晰动词描述实体间关系
- **保留条件**：使声明准确成立的上下文（如适用范围、时间）
- **可验证细节**：具体数字或事实，而非营销语言

#### 段落孤立测试

发布前对每个意图被 AI 引用的段落自问：脱离上下文读时，是否命名了所有实体？是否完整回答了自身的问题？是否可独立核实？三问中有一个「否」就需要修改。

#### 内容新鲜度

- 重点页面显示可见的「最后更新」日期
- 产品行为、定价、流程或统计数据变化时及时更新
- 核心内容至少每季度刷新；过期数据加上原始日期标注
- 不要留下无日期的统计数字

#### 其他有效模式

| 模式 | 做法 |
|------|------|
| 引用循环（Citation Loops） | 提供值得转述、有归因的内容 |
| 来源架构（Source Architecture） | 稳定的证据页面 + 方法论 + 作者信息 |
| 归因策略（Attribution Strategy） | 署名作者、`sameAs` Schema、争取被提及时带链接 |
| Schema 优先级 | FAQPage、Article（含 dateModified）、Organization、HowTo |

Google 对 AI 搜索的建议与经典 SEO 一致：独特有价值的内容、良好体验、可访问性、结构化数据与可见内容一致。

### GEO 研究亮点（学术论文）

以下来自 Princeton、GEO-SFE 等同行评审研究，使用前请核查原始数据：

- **Princeton GEO 论文（2023）**：引入 GEO 正式框架，通过 GEO-bench 验证「引用来源、添加统计数据、加入专家引语」等策略可提升 AI 可见度 30–40%
- **GEO-SFE 论文（2026）**：首个结构化 GEO 框架，在 6 个生成式引擎中验证三层结构优化带来稳定 17.3% 引用率提升、18.5% 感知质量提升
- **AgenticGEO**：单一提示词优化容易过拟合；需用多样查询跨引擎测试，策略要能适应引擎行为变化
- **领域差异性**：优化策略在不同垂类（健康 vs 科技 vs 创意）效果存在显著差异，需分领域测试而非套用统一战术

### 新 KPI 体系

旧 KPI：排名从第 8 到第 3。新 KPI 包括：

- **Share of Model（SoM）**：在定义查询集中，品牌提及次数 ÷ 所有追踪竞品提及总数，分平台统计
- **流量速度**（Traffic Velocity）：内容多快获得动能
- **辅助转化**（Assisted Conversions）：内容在漏斗中的预热作用
- **AI 引用率**：内容被 AI 答案引用的频率，含引用情感与描述准确性
- **AI 来源流量**：通过 GA4 归因追踪来自 AI 搜索的访问与转化
- **品牌查询 CTR**：社媒热度带来的品牌搜索点击
- **跨渠道增长贡献**：SEO 对整体营收的归因

### UX 成为 SEO 增长策略

过去 SEO 负责把流量送到网站；现在如果落地页体验差、不转化，SEO 等于白做。优秀落地页应视觉吸引、加载快、易用、对齐意图，且移动端同样优秀。

### 可立即落地的行动清单

**基础：**

1. 确保站点可爬取、可索引（Search Console 检查）
2. 每页对齐一个搜索意图，内容优于 SERP 竞品
3. 建立关键词研究 → 内容规划 → 内链集群流程
4. 持续监控 + 每季度内容修剪

**进阶：**

5. 画出目标受众的「发现路径地图」（他们在哪搜、什么阶段、用什么设备）
6. 选 1–2 个社媒/视频平台，与 Google SEO 关键词研究交叉验证
7. 用 AI 倒金字塔写作：问题作标题，首段 40-60 词直接答案，再展开证据
8. 对高优先级段落做孤立测试：脱离上下文仍能完整、准确表达
9. 核心页面加「最后更新」时间戳，产品或数据变化时及时刷新
10. 检查 `robots.txt` 对 PerplexityBot、ClaudeBot、OAI-SearchBot 的策略
11. 追踪 SoM（模型声量份额）、AI 引用情感、辅助转化，不只看排名
12. 投资作者署名、LinkedIn 专家档案、`sameAs` Schema
13. 优化落地页 UX，确保流量能转化

### 与本 Skill 的衔接

本 skill 与上述框架一致：**GEO 是 SEO 延伸，不是独立技巧**。重点仍是可爬取文本、结构化数据、E-E-A-T、实体一致性；额外关注 AI 引用概率、品牌声量、跨平台可见度。

深度参考文档：

- [`references/geo-research-principles.md`](references/geo-research-principles.md) — 学术论文（Princeton GEO、GEO-SFE）与2026实践：三层结构、AI倒金字塔、锚定陈述、段落孤立测试、AI爬虫矩阵、SoM度量
- [`references/seo-growth-visibility-principles.md`](references/seo-growth-visibility-principles.md) — 三大支柱、多平台策略、增长 KPI、AI 内容策略
- [`references/industry-geo-visibility-principles.md`](references/industry-geo-visibility-principles.md) — GEO 五原则、AI 可见度度量方法
- [`references/audit-checklist.md`](references/audit-checklist.md) — 完整审计清单，含 P0–P3 优先级说明

## 实用工具

以下工具覆盖索引监控、外链分析、趋势洞察和关键词研究，适合配合本 skill 的审计与优化流程使用。

| 工具 | 用途 |
|------|------|
| [Google Search Console](https://search.google.com/search-console) | 监控索引状态、抓取错误、搜索表现与 Core Web Vitals |
| [Ahrefs Backlink Checker](https://ahrefs.com/backlink-checker) | 免费查看任意域名的外链概况与引用域数量 |
| [Google Trends](https://trends.google.com/trends/) | 对比关键词热度趋势、地域分布与相关查询 |
| [Semrush Keyword Magic Tool](https://www.semrush.com/analytics/keywordmagic/) | 关键词研究、聚类、搜索量与 SERP 难度分析 |

## 资料来源

- [Google Search Central 文档](https://developers.google.com/search/docs)
- [Google AI 功能和网站](https://developers.google.com/search/docs/appearance/ai-overviews)
- [OpenAI Crawlers](https://platform.openai.com/docs/bots)
- [Princeton et al., GEO: Generative Engine Optimization（论文）](https://arxiv.org/html/2311.09735v3)
- [GEO-SFE: Structural Feature Engineering for GEO（论文）](https://arxiv.org/abs/2603.29979v1)
- [Search Engine Land：What Is SEO](https://searchengineland.com/guide/what-is-seo)
- [Search Engine Land：The Future of SEO](https://searchengineland.com/guide/future-of-seo)
- [Search Engine Land：Mastering GEO in 2026](https://searchengineland.com/mastering-generative-engine-optimization-in-2026-full-guide-469142)
- [Search Engine Land：How to write for AI search](https://searchengineland.com/ai-search-playbook-machine-readable-content-472412)
- [Search Engine Land：AI Overviews optimization guide](https://searchengineland.com/guide/how-to-optimize-for-ai-overviews)
- [Search Engine Land GEO 框架](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418)
- [Mintlify GEO 指南](https://www.mintlify.com/docs/zh/guides/geo)
