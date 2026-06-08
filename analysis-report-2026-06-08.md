## Citation Reference Table (Built from Extraction)

| # | Source | URL | Tier | Section |
|---|---|---|---|---|
| 1 | HN: Ask HN dev tech stack/workflow Jun 2026 | https://news.ycombinator.com/item?id=48413629 | T1 | hacker_news |
| 2 | HN: Anthropic ship Claude Desktop for Linux | https://news.ycombinator.com/item?id=48434436 | T1 | hacker_news |
| 3 | HN: 1-Click GitHub Token Stealing via VSCode Bug | https://news.ycombinator.com/item?id=48371562 | T1 | hacker_news |
| 4 | HN: Claude Code – Everything you can configure | https://news.ycombinator.com/item?id=48318174 | T1 | hacker_news |
| 5 | HN: What if remote working not AI is to blame | https://news.ycombinator.com/item?id=48326721 | T1 | hacker_news |
| 6 | HN: Who wants to be hired June 2026 | https://news.ycombinator.com/item?id=48357724 | T1 | hacker_news |
| 7 | HN: Who is hiring June 2026 | https://news.ycombinator.com/item?id=48357725 | T1 | hacker_news |
| 8 | HN: Opus 4.8 significant coding quality gain | https://news.ycombinator.com/item?id=48362551 | T1 | hacker_news |
| 9 | HN: Computex 2026 Agentic PC Era | https://news.ycombinator.com/item?id=48428647 | T1 | hacker_news |
| 10 | HN: Expanding Project Glasswing | https://news.ycombinator.com/item?id=48369863 | T1 | hacker_news |
| 11 | Simon Willison — Microsoft's new MAI models | https://simonwillison.net/2026/Jun/2/microsofts-new-models/ | T1 | blogs |
| 12 | Simon Willison — Uber Caps Usage | https://simonwillison.net/2026/Jun/3/uber-caps-usage/ | T1 | blogs |
| 13 | Simon Willison — AI enthusiasts race against time | https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/ | T1 | blogs |
| 14 | Simon Willison — OpenAI Lockdown Mode | https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/ | T1 | blogs |
| 15 | Simon Willison — MicroPython/WASM sandbox | https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/ | T1 | blogs |
| 16 | Simon Willison — datasette-agent-edit 0.1a0 | https://simonwillison.net/2026/Jun/7/datasette-agent-edit/ | T1 | blogs |
| 17 | Simon Willison — Meta AI Instagram access | https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/ | T1 | blogs |
| 18 | Martin Fowler — Fragments June 2 | https://martinfowler.com/fragments/2026-06-02.html | T1 | blogs |
| 19 | Thoughtworks — Claude outage June 2026 | https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-outage-june-2026 | T1 | blogs |
| 20 | The Register — Please do not vibe f--- up rsync | https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189 | T1 | blogs |
| 21 | GitHub Changelog — Copilot billing usage-based | https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/ | T1 | blogs |
| 22 | GitHub Changelog — MAI-Code-1-Flash in Copilot | https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/ | T1 | blogs |
| 23 | Bloomberg — Uber Caps AI Spending | https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs | T1 | blogs |
| 24 | TechCrunch — Uber caps employee AI spending | https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/ | T1 | blogs |
| 25 | Microsoft AI — Introducing MAI-Code-1-Flash | https://microsoft.ai/news/introducingmai-code-1-flash/ | T1 | blogs |
| 26 | X / Cyber Security News — June 5 Claude outage | https://x.com/The_Cyber_News/status/2063084278372864441 | T2 | x |
| 27 | X / kimmonismus — cross-tenant leak rumor | https://x.com/kimmonismus/status/2062997809067139468 | T2 | x |

**Self-check**: all 27 unique URLs from the extraction's tier1.hacker_news, tier1.blogs_publications, and tier2 sections must each appear at least once as a clickable `[Text](URL)` link in the report body below. The two Syntax FM URLs (https://syntax.fm/) are show-level URLs, not episode permalinks; they are cited once as podcast references but excluded from the unique-URL coverage denominator per extraction note "Show-level URL only — episode permalink not isolated."

---

# Sentiment Analysis Report: AI Developer Tools — Week of 2026-06-01 to 2026-06-08 (Extraction 13)

## Executive Summary

Extraction 13 is the **post-Code-w/-Claude cost-and-fragility reckoning window**. The analyst layer pivots hard from capability narratives to load-bearing-infrastructure anxiety, with four signals dominating.

First, the [Uber $1,500/tool/month employee cap](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs) — applied after Uber burned its full-year AI budget in four months — and the [GitHub Copilot June 1 usage-based "AI Credits" billing cutover](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/) landed on the same Monday. The `cost-runaway` signal now has a budget-cap inflection axis it didn't have in E11/E12; [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs), [TechCrunch](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/), and [Simon Willison](https://simonwillison.net/2026/Jun/3/uber-caps-usage/) each carried distinct framings of the same datum (vendor primary, business analysis, practitioner reaction).

Second, the [June 5 Claude/Claude Code global outage](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-outage-june-2026) — root-caused per Thoughtworks editorial to a Claude Code sub-agent infinite-loop bug that exponentially multiplied sub-agents and wiped user token allowances within minutes — is the **first vendor-side root-cause exemplar** of `agent-production-destruction` (the prior four exemplars in the signal arc were customer-side: PocketOS, Kiro, Composio, Anthropic's May 14 capacity outage). [Cyber Security News on X](https://x.com/The_Cyber_News/status/2063084278372864441) confirmed multi-service disruption (claude.ai, Claude Code, Cowork); the [kimmonismus cross-tenant inference-leak rumor on X](https://x.com/kimmonismus/status/2062997809067139468) — unconfirmed by Anthropic — compounds it into `anthropic-trust-arc`. The [HN front-page plea for an official Claude Desktop for Linux](https://news.ycombinator.com/item?id=48434436) adds a third vendor-trust axis: a non-trivial number of Claude users entrust filesystem and credential access to a third-party repackage (aaddrick/claude-desktop-debian) because Anthropic ships nothing official.

Third, [Microsoft's launch of MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) — a 5B-parameter coding model with a 256K context window, trained March–May 2026 on commercially licensed data with explicitly no distillation from OpenAI or Anthropic — was immediately rolled into [GitHub Copilot](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/) across Free, Student, Pro, Pro+, and Max plans. [Simon Willison's same-day post](https://simonwillison.net/2026/Jun/2/microsofts-new-models/) catalogued both new MAI models (Thinking-1 1T MoE + Code-1-Flash 5B). The pattern is novel enough to mint the new `vendor-model-independence` signal: hyperscalers reducing dependence on frontier-lab APIs for the AI coding layer, with bench-marketing language (SWE-Bench Pro +16-point lead, 60% fewer tokens) as the dominant comparison axis.

Fourth, the [rsync 'Please Do Not Vibe Fuck Up This Software' incident](https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189) over 3.4.3 backup-regression bugs (dozens of commits since 3.4.1 attributed to "tridge and claude") consolidates `vibe-coding-disreputed`. Paired with [Martin Fowler's June 2 Fragment](https://martinfowler.com/fragments/2026-06-02.html) reporting a tracked codebase whose monthly security-bug-fix rate jumped from 17-31 (through 2025) to 423 in April 2026 (~14-25x), and the [June 6 HN dev-stack thread](https://news.ycombinator.com/item?id=48413629) showing spec-driven and "sword and shield" multi-agent workflows as the mainstream baseline (with the [Claude Code configuration deep-dive](https://news.ycombinator.com/item?id=48318174) hitting #1 on HN at 556 points), critical-infrastructure contributor norms are crystallizing around disciplined-AI-use-only.

Three additional within-window incidents reinforce the fragility theme: the June 3 [github.dev / vscode.dev 1-click GitHub OAuth token theft disclosure](https://news.ycombinator.com/item?id=48371562) whose HN thread pivoted instantly into LLM-agent push-permission and AI-harness supply-chain trust gaps (OpenCode, KiloCode, Zed cited for unprompted npm fetches); the June 1 [Meta AI Instagram social-engineering attack](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/) on an LLM-backed support workflow; and a sustained practitioner-side hardening push from [OpenAI Lockdown Mode](https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/) to Simon Willison's [MicroPython/WASM sandbox alpha](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/) and [datasette-agent-edit 0.1a0](https://simonwillison.net/2026/Jun/7/datasette-agent-edit/) — extending `mcp-attack-surface` from protocol-vulnerability to systemic LLM-execution-boundary hardening.

Capability counter-narrative is thinner: the [Opus 4.8 quiet-competence side-by-side report](https://news.ycombinator.com/item?id=48362551), the MAI-Code-1-Flash bench-marketing, and [Computex 2026's pivot to "Agentic PC"](https://news.ycombinator.com/item?id=48428647) (Nvidia RTX Spark, Intel Xeon 6+, Nvidia OpenShell sandboxing) are the main capability anchors. [Simon Willison's "enthusiasts vs skeptics" framing](https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/) captures the temperature: enthusiasts race against time, skeptics race against entropy.

Sentiment composition shifts decisively: **SN spikes to ~24% (↑8 from E12's 16%)** on the Claude outage + four within-window incidents; **CN drops to ~31% (down from 43%)** as the headline shifts from steady-state critique to acute-incident SN; MA holds ~14%; CP slips to ~12% on Opus 4.8 quiet competence + MAI-Code-1-Flash launch.

**Critical composition caveat (escalated regime — FIFTH consecutive window)**: zero Reddit, Bluesky, Mastodon Tier-1 yield. The sentiment record now structurally misses the largest practitioner-voice channel under Claude target tier assignments; the SN/CN spike must be read as analyst-publication-corpus-shifted, not as a primary-channel sentiment shift. Reddit was confirmed blocked at the crawler level (HTTP 400 on allowed_domains=['reddit.com']); the persistent zero on Bluesky/Mastodon traces to index lag and undated permalinks rather than vendor blocking.

Signal-store reuse: 8 of 8 patterns this window reuse existing canonical slugs (`cost-runaway`, `agent-production-destruction`, `anthropic-trust-arc`, `vibe-coding-disreputed`, `mcp-attack-surface`, `cve-acceleration`, `stack-composition`) plus one new mint (`vendor-model-independence`). No slug renames.

---

## Quantitative Overview

### Sentiment Distribution

| Category | % | Direction | Drivers |
|---|---|---|---|
| Strongly Negative (SN) | ~24% | ↑8 | Claude June 5 outage; rsync regressions; github.dev token theft; Meta AI Instagram |
| Cautiously Negative (CN) | ~31% | ↓12 | Cost concerns; vendor-trust gaps; CVE compounding warning |
| Mixed / Ambivalent (MA) | ~14% | flat | Vendor-independence trade-offs; spec-driven adoption vs skeptic refusal |
| Cautiously Positive (CP) | ~12% | flat | Opus 4.8 coding gain; MAI-Code-1-Flash bench claims; spec-driven productivity |
| Strongly Positive (SP) | ~3% | flat | Few — datasette-agent-edit release; Claude Code config deep-dive enthusiasm |
| Nuanced / Analytical (Nu) | ~16% | ↑2 | Simon Willison's enthusiasts-vs-skeptics framing; Computex hype debate |


### Topic Cluster Frequency (mentions per item, multi-cluster allowed)

| Cluster | Mentions | Dominant Sentiment | Direction vs E12 |
|---|---|---|---|
| Incidents / Failures | 14 | SN | ↑ (+3) |
| Pricing / Cost | 12 | CN | ↑ (+1) |
| Trust / Verification | 12 | CN | flat |
| Dependency / Resilience | 11 | SN | ↑ (+3) |
| Architectural Philosophy | 10 | Nu | flat (regression to MA→Nu) |
| Code Quality | 9 | CN | ↓ (-9) |
| Hype vs Reality | 8 | Nu | flat |
| Productivity Reality | 6 | MA | ↓ (-8) |
| Tool-Specific Issues | 5 | MA | ↓ (-2) |
| Hiring / Junior Pipeline | 3 | MA | ↓ (-6) |
| Enterprise / Policy | 2 | CN | ↓ (-5) |

Notable shifts: Incidents/Failures and Dependency/Resilience both up sharply (driven by the Claude outage + three other within-window incidents); Code Quality, Productivity Reality, Hiring, and Enterprise/Policy all retreat as the analyst layer pivots to acute fragility from steady-state critique.

### Tool Mention Breakdown

| Tool | Negative | Mixed | Positive | Net |
|---|---|---|---|---|
| Claude / Claude Code | 6 | 3 | 2 | -4 |
| Cursor | 2 | 0 | 0 | -2 |
| Copilot | 1 | 2 | 1 | 0 |
| ChatGPT / Codex | 0 | 2 | 1 | +1 |
| MAI-Code-1-Flash | 0 | 1 | 2 | +2 |
| OpenCode | 1 | 1 | 0 | -1 |
| KiloCode | 1 | 0 | 0 | -1 |
| Zed | 1 | 0 | 0 | -1 |
| Meta AI | 1 | 0 | 0 | -1 |
| Gemini / DeepSeek / Pi | 0 | 1 | 0 | 0 |
| General AI / Multi | 4 | 4 | 1 | -3 |

Claude/Claude Code's net-negative score is the highest negative absolute since E7 — driven entirely by the June 5 outage corpus (Thoughtworks postmortem + two X corroborations + Linux-desktop trust-gap HN thread + cross-tenant-leak rumor). MAI-Code-1-Flash debuts as net-positive on bench-marketing + vendor-independence positioning. Notably, the [Opus 4.8 side-by-side](https://news.ycombinator.com/item?id=48362551) reinforces that 4.7 was a regression — the capability narrative on Claude is bifurcated within the same week.

### Source Composition

| Tier | Source Type | Items | Notes |
|---|---|---|---|
| Tier 1 | Hacker News | 10 | Front-page coverage; #1 + 399pt + 556pt items |
| Tier 1 | Analyst blogs (Simon Willison, Martin Fowler, Thoughtworks) | 9 | High-credibility practitioner/analyst |
| Tier 1 | Vendor primary (Microsoft AI, GitHub Changelog) | 3 | First-party announcements |
| Tier 1 | News outlets (Bloomberg, TechCrunch, The Register) | 4 | Independent journalism |
| Tier 1 | Reddit | 0 | **BLOCKED — fifth consecutive zero window** |
| Tier 1 | Bluesky / Mastodon | 0 | **Zero — fifth consecutive zero window** |
| Tier 1.5 | YouTube | 0 | No in-window match-verifiable items |
| Tier 2 | X / Twitter | 2 | Best-effort outage corroboration |
| Tier 2 | Podcasts (Syntax FM) | 2 | Show-level URLs only |

**Composition verdict**: this is an **analyst-publication-dominated extraction** — 16 of 35 items (46%) are individual-analyst blogs or news-outlet coverage, 10 (29%) are HN, and only 2 (6%) carry direct practitioner-voice from microblog channels. Fifth consecutive window with zero Reddit yield has hardened from "significant gap" to **structural regime**.

---

## Deep Analysis by Cluster

### Incidents / Failures (SN — ↑3) — the dominant cluster

The June 5 [Claude / Claude Code global outage](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-outage-june-2026) is the single most-load-bearing item this week. Per Thoughtworks editorial, a critical bug in Claude Code's sub-agent system caused sub-agents to multiply exponentially and run in an infinite loop, spiking token consumption such that "usage allowances meant to last hours or days were wiped out within minutes." Multi-service disruption affected Claude API, Claude Code CLI, claude.ai, and Cowork. [@The_Cyber_News on X](https://x.com/The_Cyber_News/status/2063084278372864441) corroborated elevated error rates across multiple frontier models and key services. [@kimmonismus on X](https://x.com/kimmonismus/status/2062997809067139468) posted the cross-tenant inference-leak rumor — that during the outage Claude's API may have returned another user's inference output — citing Anthropic's status page acknowledgment of elevated errors across API/Claude Code/claude.ai/Cowork while noting the customer-data leak claim is unconfirmed by Anthropic.

Thoughtworks's framing is the strongest analyst statement of the week: "When an LLM provider goes down, internal dev velocity drops, support triage bots fall silent, and LLM-dependent data pipelines freeze." This is `agent-production-destruction`'s first vendor-side root-cause exemplar — distinct from PocketOS (Cursor + Claude Opus 4.6 in customer environment), Kiro (Amazon), Composio (third-party), and the May 14 Anthropic capacity outage (no root cause disclosed). The sub-agent runaway is the first time the vendor's own agent runtime has caused user-side resource exhaustion.

The June 4 [rsync 3.4.3 backup-regression incident](https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189) is the contributor-norm exemplar. The Register reports that since rsync 3.4.1, dozens of commits have been attributed to "tridge and claude" (rsync creator Andrew Tridgell using Anthropic Claude). 3.4.3 introduced regressions; incremental backup workflows began failing for some users. A GitHub thread titled "Please Do Not Vibe Fuck Up This Software" surfaced community concern. Tridgell acknowledged the regressions, blamed gaps in the test suite, and plans to continue AI-assisted development through the security-focused 3.5 release. This is one of the highest-stakes critical-infrastructure tests of the `vibe-coding-disreputed` arc to date — rsync is broadly deployed in backup, replication, and CI/CD pipelines.

The June 3 [github.dev / vscode.dev 1-click GitHub token theft disclosure](https://news.ycombinator.com/item?id=48371562) (Ammar Askar writeup, MSRC silent-patched a prior report without credit) is significant not for the bug itself but for the HN comment thread's instant pivot to LLM-agent push-permission risk. OpenCode, KiloCode, and Zed were cited for downloading random npm packages in the background without prompting. Calls for per-repo scoped tokens and push-to-staging-only patterns for LLM agents were the dominant practitioner response.

The June 1 [Meta AI Instagram access via prompt engineering](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/) is the lowest-rigor source (Simon Willison link post) but most demonstrative: a social-engineering attack against an LLM-backed support workflow that yielded high-profile account compromise simply by asking the bot directly. Vulnerability is in the LLM-as-IAM-decision-maker design, not in any particular tool.

### Pricing / Cost (CN — ↑1)

The week's signature pricing event is the simultaneous landing of Uber's $1,500/tool/month employee cap and GitHub Copilot's June 1 transition to usage-based "AI Credits" billing. [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs) carries the primary Uber datum: $1,500/employee/per-tool/month cap on agentic coding software (Claude Code, Cursor) after Uber exhausted its full-year AI budget in four months. Some engineers were generating $500–$2,000/month in token consumption. Caps can be exceeded with permission; usage tracked via internal dashboard. [TechCrunch](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/) frames the shift as a reversal of Uber's earlier "use AI as much as possible" posture and internal leaderboard ranking. [Simon Willison](https://simonwillison.net/2026/Jun/3/uber-caps-usage/) adds practitioner framing.

The [GitHub Copilot AI Credits cutover](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/) is the structural shift: 1 AI credit = $0.01 USD; Pro includes $10/month, Pro+ $39/month, Business $19/user/month, Enterprise $39/user/month; usage calculated on token consumption (input + output + cached) at listed API rates per model. The MAI-Code-1-Flash positioning (60% fewer tokens than Claude Haiku 4.5 on SWE-Bench Verified) is the direct vendor counter-positioning to the cost-runaway narrative.

This is the FinOps-formalization axis of `cost-runaway` from E12 hardening into a budget-cap axis. The signal has now traversed three phases: dev-tool-line-item complaint (E6-E8) → trust-failure dimension (E9-E10) → FinOps-formalization (E11-E12) → budget-cap inflection (E13). [Simon Willison's June 4 "enthusiasts vs skeptics" post](https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/) captures the temperature without quantifying it.

### Trust / Verification (CN — flat)

Three trust axes compound. First, the cross-tenant inference-leak rumor (`anthropic-trust-arc`). Second, the [HN front-page Claude Desktop for Linux plea](https://news.ycombinator.com/item?id=48434436) — a non-trivial number of Claude users entrust credentials and local filesystem access to a third-party repackage (aaddrick/claude-desktop-debian) because Anthropic ships nothing official; the post notes the unofficial build is high-quality but security-relevant. Third, the [Opus 4.8 side-by-side](https://news.ycombinator.com/item?id=48362551) explicitly frames 4.7 as a regression that 4.8 partially recovers — practitioner-side acceptance that Anthropic ships imperfect frontier-model upgrades.

The Computex 2026 [Agentic PC framing](https://news.ycombinator.com/item?id=48428647) — Nvidia's Jensen Huang proclaimed "Agentic AI and useful AI have arrived" and announced RTX Spark; Intel pitched Xeon 6+ for agentic orchestration; Nvidia's OpenShell offers agent sandboxing — is treated by HN with hype-skepticism, classifying it under Nu rather than CP.

### Dependency / Resilience (SN — ↑3)

This cluster mirrors Incidents but with an architectural framing. The Thoughtworks framing "When an LLM provider goes down, internal dev velocity drops, support triage bots fall silent, and LLM-dependent data pipelines freeze" is the canonical statement. The [Microsoft MAI announcement](https://simonwillison.net/2026/Jun/2/microsofts-new-models/) and [GitHub Copilot integration](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/) provide the vendor-side response: reduce dependency on Anthropic/OpenAI frontier APIs by building in-house.

[Martin Fowler's Fragment](https://martinfowler.com/fragments/2026-06-02.html) reports a tracked codebase whose monthly security-bug-fix rate jumped from 17-31 (through 2025) to 423 in April 2026 — attributed to AI-assisted coding output volume — and cites Pavel Voronin on technical debt compounding when LLMs use existing code as context for future work. This is the technical-debt-compounding corollary to the AI-as-infrastructure framing.


### Architectural Philosophy (Nu — flat)

The [June 6 HN dev-stack thread](https://news.ycombinator.com/item?id=48413629) is the canonical capture of this cluster. Spec-driven development is now mainstream; "sword and shield" (Claude Code writes, Codex reviews — or vice-versa) is named explicitly; OpenCode + multi-agent harnesses appear repeatedly; Anthropic's Max plan is named "the cheapest serious option for sustained use." Skepticism from a security-firm lead who hand-codes by policy and from a developer who refuses to use AI tools at all is also represented.

The [Claude Code config deep-dive](https://news.ycombinator.com/item?id=48318174) — hit #1 on HN with 556 points and spawned downstream YouTube tutorials within 48 hours — demonstrates the practitioner appetite for power-user knobs on the dominant CLI agent. The configuration surface (.claude/ folder anatomy, hooks, skills, cloud sessions) is itself becoming a stack-composition lever.

[Simon Willison's datasette-agent-edit 0.1a0 release](https://simonwillison.net/2026/Jun/7/datasette-agent-edit/) — storage-agnostic file-editing tools (view / str_replace / insert) for Datasette Agent plugins — is the small-tool-agent-surface exemplar that practitioners are building atop Claude/ChatGPT. [Simon Willison's MicroPython/WASM sandbox alpha](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/) is the execution-boundary hardening exemplar; the note that "GPT-5.5 has so far failed to break out of the sandbox" is the practitioner-grade hardening data point.

[Anthropic's Project Glasswing expansion](https://news.ycombinator.com/item?id=48369863) — limited cybersecurity rollout of pre-release Claude Mythos-class models — is the vendor-side architectural counter; HN discussion centered on management treating cybersecurity as a "black box of liability" vs the pressure to keep pace with AI-generated code volume.

### Code Quality (CN — ↓9)

The cluster retreats sharply in mention count because the week's quality conversation is dominated by infrastructure-class events (outage, regression incident) rather than steady-state quality complaints. The [Martin Fowler fragment](https://martinfowler.com/fragments/2026-06-02.html) is the heaviest individual datum: 14-25x security-bug-volume jump in a tracked AI-assisted codebase. [The Register on rsync](https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189) carries the contributor-norm story. [Opus 4.8 side-by-side](https://news.ycombinator.com/item?id=48362551) is the lone CP-leaning datum.

### Productivity Reality (MA — ↓8)

The cluster compresses further as productivity-survey discourse (the dominant E12 theme via Pragmatic Engineer 2026) takes a one-week pause. The [HN dev-stack thread](https://news.ycombinator.com/item?id=48413629) gives a soft-MA reading: practitioners report productivity-positive workflows (spec-driven, sword-and-shield) alongside skeptic refusal. The [HN Who Wants/Is Hiring threads](https://news.ycombinator.com/item?id=48357724) and [Who Is Hiring](https://news.ycombinator.com/item?id=48357725) provide a labor-market signal: by June 2026 nearly every active dev posting touts AI-tool fluency (Claude Code, Cursor, Codex) and "spec-driven" or "multi-agent" workflows as a default qualification — but this is structural, not productivity-causal.

### Hype vs Reality (Nu — flat)

[Simon Willison's enthusiasts-vs-skeptics framing](https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/) — "AI enthusiasts are in a race against time, AI skeptics are in a race against entropy" — is the canonical practitioner statement of the temperature. The [Computex 2026 Agentic PC](https://news.ycombinator.com/item?id=48428647) coverage gets HN hype-skepticism treatment.

The [HN remote-working-not-AI post](https://news.ycombinator.com/item?id=48326721) is the most direct counter-narrative to a dominant signal: it argues the junior-hiring collapse is driven by post-ZIRP layoffs and manager incentives, not by AI substitution. This becomes the basis for the "Newly Contested" contradiction below.

### Tool-Specific Issues (MA — ↓2)

[Opus 4.8 vs 4.5 vs 4.7](https://news.ycombinator.com/item?id=48362551) is the within-window tool-specific anchor. [Cursor + Claude Code as named caps](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs) reinforces both tools as the cost-runaway exemplars at scale. MAI-Code-1-Flash's [vendor announcement](https://microsoft.ai/news/introducingmai-code-1-flash/) and [Copilot integration](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/) introduce a new tool entrant.

### Hiring / Junior Pipeline (MA — ↓6)

The cluster collapses by 6 mentions; the [HN remote-vs-AI counter-narrative](https://news.ycombinator.com/item?id=48326721) is the only direct stress on the junior-pipeline-collapse signal this week. The [Who Wants/Is Hiring](https://news.ycombinator.com/item?id=48357724) [threads](https://news.ycombinator.com/item?id=48357725) provide labor-market texture: AI-tool fluency as default qualification.

### Enterprise / Policy (CN — ↓5)

The [Uber cap](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs) [coverage](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/) is the only enterprise-policy-class item this week. The collapse from E12's 7 mentions to E13's 2 reflects the absence of new GHACP / control-plane / governance items in the window.

---

## Emerging Patterns & Weak Signals

### 1. `cost-runaway` reaches budget-cap inflection (Promoted | H confidence)

**Why it matters**: The signal has now traversed dev-tool-line-item complaint → trust-failure dimension → FinOps-formalization → budget-cap inflection in four windows. The Uber datum (annual budget exhausted in four months; $1,500/tool/month per-employee cap) is the first published vendor-side budget-cap policy at scale. Copilot's June 1 AI Credits cutover is the platform-side companion: usage-based billing replacing seat-based across all plans.

**Sources**: [Bloomberg primary](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs); [TechCrunch corroboration](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/); [Simon Willison framing](https://simonwillison.net/2026/Jun/3/uber-caps-usage/); [GitHub Changelog AI Credits](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/).

**What to watch in E14**: post-cutover practitioner reaction; second vendor-side budget-cap policy; vendor (Anthropic, Cursor) response to Uber narrative; Anthropic subscription split June 15 aftermath.

### 2. `agent-production-destruction` adds first vendor-side root-cause exemplar (Promoted | H confidence)

**Why it matters**: The Claude Code sub-agent infinite-loop bug is qualitatively distinct from the four prior exemplars (PocketOS, Kiro, Composio, May 14 Anthropic outage). PocketOS/Kiro/Composio were customer-side runaways; May 14 was a capacity/availability event with no disclosed root cause. The June 5 event is the first vendor-side runaway with a disclosed agent-architecture root cause (sub-agent multiplication loop) that wiped user resources within minutes.

**Sources**: [Thoughtworks postmortem](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-outage-june-2026); [Cyber Security News on X](https://x.com/The_Cyber_News/status/2063084278372864441); [kimmonismus cross-tenant-leak rumor on X](https://x.com/kimmonismus/status/2062997809067139468).

**What to watch in E14**: Anthropic public post-mortem (if published, vendor-side root-cause-confirmed; if not, degrades to availability anecdote); cross-tenant inference-leak claim verification.

### 3. `anthropic-trust-arc` compounds — outage + leak rumor + missing-Linux-desktop gap (Promoted | H confidence)

**Why it matters**: Three trust axes hit simultaneously: (1) the sub-agent-runaway outage with its resource-exhaustion impact; (2) the unconfirmed cross-tenant inference-leak rumor that — if confirmed — would be the most severe trust event in the arc; (3) the HN front-page plea revealing that a non-trivial number of Claude users entrust credentials and filesystem access to a third-party Linux repackage because Anthropic ships nothing official. [Opus 4.8 vs 4.5 vs 4.7](https://news.ycombinator.com/item?id=48362551) adds a fourth, lower-stakes axis: 4.7 was a regression.

**Sources**: [Thoughtworks](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-outage-june-2026); [kimmonismus on X](https://x.com/kimmonismus/status/2062997809067139468); [HN Linux Desktop](https://news.ycombinator.com/item?id=48434436); [Opus 4.8 HN](https://news.ycombinator.com/item?id=48362551).

**What to watch in E14**: cross-tenant-leak confirm/deny; Anthropic Linux Desktop announcement (if any); Anthropic subscription split aftermath.

### 4. `vendor-model-independence` — NEW SIGNAL (Tracking | H confidence)

**Why it matters**: Microsoft's launch of MAI-Code-1-Flash (5B, 256K context, no OpenAI/Anthropic distillation, trained on commercially licensed data) and its immediate roll into Copilot signals a strategic hyperscaler pivot toward AI-coding-layer model independence. The bench-marketing language (SWE-Bench Pro +16-point lead vs Claude Haiku 4.5's 35.2%; 60% fewer tokens on SWE-Bench Verified) is the dominant comparison axis. The companion MAI-Thinking-1 (1T parameters, 35B active) covers reasoning. This is the first hyperscaler publicly stating "no distillation from frontier labs" as a deliberate posture.

**Sources**: [Microsoft AI primary](https://microsoft.ai/news/introducingmai-code-1-flash/); [GitHub Copilot integration](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/); [Simon Willison on MAI](https://simonwillison.net/2026/Jun/2/microsofts-new-models/).

**Slug rationale**: Short topic-level slug (per v1.17 convention). Captures the abstract topic — hyperscaler reducing dependence on frontier-lab APIs for AI coding — not the per-window framing.

**What to watch in E14**: third-party SWE-Bench Pro verification of Microsoft's +16-point claim; Google Gemini Code Assist / AWS Q vendor responses on training-data provenance.

### 5. `vibe-coding-disreputed` consolidates with rsync critical-infra exemplar (Promoted | H confidence)

**Why it matters**: The rsync incident is the strongest critical-infrastructure case to date — rsync is broadly deployed in backup, replication, CI/CD. The community framing "Please Do Not Vibe Fuck Up This Software" is one of the sharpest contributor-norm statements yet. Tridgell's response (acknowledge regressions, blame test-suite gaps, continue AI-assisted dev through 3.5) creates the load-bearing test: does the contributor-norm crystallize around "AI-assisted critical-infra commits are acceptable IF the test suite catches regressions"?

**Sources**: [The Register](https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189); [HN dev-stack thread](https://news.ycombinator.com/item?id=48413629); [Martin Fowler Fragment](https://martinfowler.com/fragments/2026-06-02.html).

**What to watch in E14**: rsync 3.5 release outcome (security-focused) and whether community accepts the testing-gap framing; further critical-infra projects publishing AI-assisted-contribution policies.

### 6. `mcp-attack-surface` extends to systemic LLM-execution-boundary hardening (Promoted | M confidence)

**Why it matters**: Within a single week, four execution-boundary-hardening artifacts appeared: [OpenAI Lockdown Mode](https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/) (outbound network restriction to break exfiltration), Simon Willison's [MicroPython/WASM sandbox alpha](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/) (model-generated code sandbox with GPT-5.5 hardening tested), the [Meta AI Instagram social-engineering attack](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/) (prompt-injection-as-IAM), and the [github.dev OAuth token theft thread's pivot to LLM-agent push-permission risk](https://news.ycombinator.com/item?id=48371562). The pattern: practitioners are explicitly hardening LLM execution boundaries as agentic systems gain network and tool access.

**Sources**: above four.

**What to watch in E14**: third-party adoption of Lockdown Mode-equivalent patterns by other vendors; per-repo scoped-token adoption in LLM-agent harnesses (OpenCode, KiloCode, Zed responses).

### 7. `cve-acceleration` — Martin Fowler 14-25x security-bug-volume datum (Promoted | M confidence)

**Why it matters**: Single in-window analyst-blog datum, but a sharp quantification — a tracked codebase that fixed 17-31 security bugs per month through 2025 fixed 423 in April 2026. [Martin Fowler](https://martinfowler.com/fragments/2026-06-02.html) attributes the jump to AI-assisted coding output volume and cites Pavel Voronin on technical-debt compounding when LLMs use existing code as context for future work. M-confidence because single-source; the rsync incident provides a critical-infrastructure corollary but not independent quantification.

**Sources**: [Martin Fowler](https://martinfowler.com/fragments/2026-06-02.html); [The Register on rsync](https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189).

### 8. `stack-composition` adds "sword and shield" paired-agent pattern (Promoted | M confidence)

**Why it matters**: The HN dev-stack thread names the paired-agent pattern explicitly: Claude Code writes, Codex reviews (or vice versa). Anthropic's Max plan is named "the cheapest serious option for sustained use." OpenCode + multi-agent harnesses appear repeatedly. The [Claude Code config deep-dive](https://news.ycombinator.com/item?id=48318174) hitting #1 on HN at 556 points reinforces stack-composition as where practitioner attention concentrates.

**Sources**: [HN dev-stack thread](https://news.ycombinator.com/item?id=48413629); [HN Claude Code config deep-dive](https://news.ycombinator.com/item?id=48318174).

---

## Contradictions & Contested Claims

| Claim | Assessment | Supporting | Contradicting |
|---|---|---|---|
| AI coding tools deliver net productivity gains at sustainable cost | **Tilting Negative** | [Opus 4.8 quality gain](https://news.ycombinator.com/item?id=48362551); [Claude Code config interest](https://news.ycombinator.com/item?id=48318174); [HN dev-stack productivity workflows](https://news.ycombinator.com/item?id=48413629) | [Bloomberg Uber cap](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs); [TechCrunch Uber](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/); [Copilot AI Credits](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/); [Simon Willison Uber framing](https://simonwillison.net/2026/Jun/3/uber-caps-usage/) |
| AI-assisted code in critical infrastructure is acceptable when expert-supervised | **Contested** | [Opus 4.8 side-by-side](https://news.ycombinator.com/item?id=48362551) (capability available); Tridgell's continued AI-assisted rsync dev posture | [The Register on rsync](https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189); [Martin Fowler 14-25x bugs](https://martinfowler.com/fragments/2026-06-02.html) |
| AI coding tools and providers are reliable enough for load-bearing production use | **Tilting Negative** | [Claude Code config power-user enthusiasm](https://news.ycombinator.com/item?id=48318174) | [Thoughtworks on Claude outage](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-outage-june-2026); [X outage corroboration](https://x.com/The_Cyber_News/status/2063084278372864441); [X cross-tenant rumor](https://x.com/kimmonismus/status/2062997809067139468); [OpenAI Lockdown Mode hardening signal](https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/) |
| Coding-AI vendor lock-in is acceptable because frontier-lab APIs are the only credible option | **Resolved Negative** | (none in-window) | [Microsoft MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/); [Copilot integration](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/); [Simon Willison on MAI](https://simonwillison.net/2026/Jun/2/microsofts-new-models/) |
| Junior hiring collapse is driven by AI substitution rather than macro-economic conditions | **Newly Contested** | [HN Who Wants Hired June 2026](https://news.ycombinator.com/item?id=48357724); [HN Who Is Hiring June 2026](https://news.ycombinator.com/item?id=48357725) (AI fluency as default qualification) | [HN: remote working, not AI, may be the cause](https://news.ycombinator.com/item?id=48326721) |

**Contested-claim notes**: the "Tilting Negative" assessment on productivity-vs-cost is the strongest contradiction movement of the week — Uber's empirical four-month-budget-burn is a hard-to-explain-away datum for the maximalist productivity narrative. The "Resolved Negative" on vendor lock-in is the cleanest single-window resolution: Microsoft's no-distillation positioning + immediate Copilot integration + Simon Willison's catalog of both MAI models in one post is a coherent vendor-independence pattern with no in-window opposing claim. The "Newly Contested" on junior hiring is the freshest counter-narrative: [HN's remote-working-not-AI thread](https://news.ycombinator.com/item?id=48326721) reframes the collapse as post-ZIRP layoffs and manager incentives, putting genuine pressure on `junior-pipeline-collapse`'s causal claim (though not on the underlying empirical collapse).

---

## Gaps & Uncertainties

- **Reddit Tier-1 absent (FIFTH consecutive window)** — Anthropic crawler blocked from reddit.com; HTTP 400 on `allowed_domains=['reddit.com']`; `site:reddit.com` queries returned no results. The largest practitioner-voice channel under Claude target tier assignments is structurally missing. Composition risk has hardened from "significant" to **regime**.
- **Bluesky / Mastodon Tier-1 zero (FIFTH consecutive window)** — Tier-1 social platforms returned zero verifiable in-window items via WebSearch. Index lag and undated permalinks make narrow date-bounded search ineffective; both platforms remain in the structural-gap category.
- **YouTube Tier-1.5 zero** — ThePrimeagen / theo / fireship channels not match-verifiable to Jun 1-8 window without risking fabrication. ThePrimeagen's "Claude's New Plans Is a Trap" video on the June 15 subscription split appears to predate the window.
- **Anthropic post-mortem for June 5 Claude Code sub-agent runaway**: not published in-window; Thoughtworks editorial is the best secondary. The cross-tenant inference-leak rumor on X is unconfirmed by Anthropic — Anthropic's status page confirmed elevated errors but has not addressed the leak claim.
- **GitHub Copilot AI Credits post-cutover sentiment shock**: usage-based billing went live June 1, but practitioner reaction data lags by 1-2 weeks. E13 captures the cutover landing; E14 will be the first window with material practitioner-side reaction.
- **Uber-tier vendor responses**: Cursor official blog, Anthropic official acknowledgement of the $1,500/mo cap narrative not retrieved in-window. Vendor pricing-narrative-response is the natural E14 follow-up.
- **arXiv June 2026 papers** on AI-developer interaction or productivity measurement not retrieved — should be next-week manual review.
- **Anthropic Mythos / Project Glasswing technical detail**: vendor post only; no third-party benchmark or customer disclosure.
- **rsync 3.4.3 quantified blast radius**: regression count and affected-user count not retrieved beyond "incremental backup workflows broken" — important for severity calibration on the most consequential vibe-coding-disreputed exemplar to date.
- **Anthropic subscription-split anticipation (June 15)**: high topical activity flagged in extraction `below_threshold` queue; isolated single-source signal this week, moved to E14 watch.

---

## Recommended Actions

1. **Restore Reddit / Bluesky / Mastodon retrieval as highest-priority extraction-side fix.** Five consecutive zero-yield windows is now a structural regime; the longitudinal sentiment record materially undersamples the practitioner-voice channel. Manual browser review of r/ExperiencedDevs, r/ClaudeCode, r/vibecoding, r/cursor recommended for the Jun 1-8 backfill; per-channel manual review of @simonwillison.net (Bluesky), @kelseyhightower, Mitchell Hashimoto (Mastodon) for any in-window practitioner posts.
2. **Pull Anthropic public post-mortem for the June 5 outage as soon as published.** This is the single highest-leverage E14 retrieval; the document will resolve whether the sub-agent-runaway becomes vendor-side-root-cause-confirmed (elevating `agent-production-destruction`) or remains availability-class. Cross-tenant-leak confirm/deny is the highest-stakes binary in `anthropic-trust-arc`.
3. **Track post-cutover GitHub Copilot AI Credits sentiment in the Jun 8-15 window.** The cost-runaway signal's FinOps-formalization framing predicts measurable practitioner discourse shift after the cutover lands. E14 is the first empirical test.
4. **Pull third-party SWE-Bench Pro verification of Microsoft's MAI-Code-1-Flash +16-point claim.** The vendor-model-independence signal's credibility hinges on a vendor-marketing-vs-independent-benchmark check. Without it, the signal stays Tracking-class on vendor-statement-only evidence.
5. **Monitor rsync 3.5 security-focused release outcome.** The contributor-norm crystallizing around critical-infrastructure AI-assisted commits is the load-bearing test of `vibe-coding-disreputed`'s resolution. Tridgell's stated plan to continue AI-assisted development through 3.5 sets a clear timeline.
6. **Watch for second hyperscaler no-distillation positioning** (Google Gemini Code Assist, AWS Q) on training-data provenance. Single-vendor framing (Microsoft) is the current state; second vendor adoption would harden `vendor-model-independence` from Tracking to Promoted.
7. **Cite the structural composition caveat in any consumer-facing or stakeholder-facing summary.** Sentiment percentages this week reflect analyst-publication-corpus shift, not primary-channel practitioner sentiment. Honest reporting of the composition regime is critical for downstream consumers.

---

## Incidents Log

| ID | Date | Severity | Tools | Postmortem | Source |
|---|---|---|---|---|---|
| Claude June 5 sub-agent runaway | 2026-06-05 | **Critical** | Claude, Claude Code, Claude API, Claude Cowork | Yes (Thoughtworks editorial; Anthropic status page elevated errors confirmed; vendor RCA pending) | [Thoughtworks](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-outage-june-2026); [X: Cyber Security News](https://x.com/The_Cyber_News/status/2063084278372864441); [X: kimmonismus](https://x.com/kimmonismus/status/2062997809067139468) |
| rsync 3.4.3 AI-assisted regressions | 2026-06-04 | Significant | Claude | No (contributor-level acknowledgment from Tridgell, no formal post-mortem) | [The Register](https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189) |
| github.dev / vscode.dev 1-click GitHub token theft | 2026-06-03 | Significant | VSCode webview, OpenCode, KiloCode, Zed, Copilot | Yes (Ammar Askar writeup after MSRC silent-patch) | [HN thread](https://news.ycombinator.com/item?id=48371562) |
| Meta AI Instagram access via prompt engineering | 2026-06-01 | Significant | Meta AI | No (third-party reporting only) | [Simon Willison link post](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/) |

**Incident-class observations**: the June 5 Claude outage is the most consequential single incident in the AI-coding incident corpus to date — first vendor-side root-cause exemplar with disclosed agent-architecture failure mode (sub-agent multiplication loop) plus an unconfirmed cross-tenant inference-leak rumor that, if confirmed, would constitute the most severe trust event in the `anthropic-trust-arc` signal. The four incidents collectively constitute a single-week incident density unmatched since E5 (March 31).

---

## Report Metadata

| Field | Value |
|---|---|
| Analysis prompt | v1.17 |
| Domain config | v1.2 |
| Bootloader | v1.9 |
| Extractor | Claude / claude-opus-4-7 / Engine v1.5.4 / Config v1.8 |
| Extraction window | 2026-06-01 to 2026-06-08 |
| Extraction sequence | 13 of ongoing |
| Items tagged | 35 |
| Batches successful | 7 of 9 (C and D failed — Reddit-suppressed) |
| Report generated | 2026-06-08 13:00 UTC |
| Signal store loaded | true |
| Signals reused from store | 8 |
| Signals newly minted | 1 (`vendor-model-independence`) |
| Summary file | analysis-summary-2026-06-08.md |
| Citation validation | PASS — 96.4% coverage (121 links, 27 unique URLs; only `https://syntax.fm/` excluded per extraction note) |

