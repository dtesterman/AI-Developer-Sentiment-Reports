# Longitudinal Trend Report: 2026-03-20 – 2026-06-08 (Extractions 1 – 13)

## Executive Summary

Across thirteen consecutive weekly extractions spanning 80 days (~634 sentiment-tagged items including E10's supplemental pass and E13's revised 37-item Chrome-augmented corpus), the AI coding tools discourse has executed a clear regime-shift sequence from "is the code any good?" (E1–E3) → "is the agent safe?" (E4–E7) → "is the harness right?" (E8–E9) → "who governs the gate?" (E10) → "who pays the review cost?" (E11) → "who pays the cognitive cost of being unable to work without?" (E12 — `ai-dependency-trap` mint) → and now in **E13 to "is the infrastructure load-bearing AND who pays?"** — a simultaneous fragility-and-tokenomics-reckoning week that lands [Microsoft Copilot's June 1 outage](https://windowsnews.ai/article/microsoft-copilot-outage-june-1-2026-reliability-and-ai-workflow-risk.421251) on the very day [GitHub Copilot's usage-based "AI Credits" billing transition](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) launched, followed 24 hours later by the [June 2 Anthropic Claude outage on Opus 4.6 affecting API / Console / claude.ai / Claude Code](https://status.claude.com/) — corroborated by [TechRadar's Downdetector breakdown (60% Claude Chat, 24% mobile, 8% Claude Code)](https://www.techradar.com/news/live/claude-outage-june-2026) and framed by [Thoughtworks editorial](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-outage-june-2026) as the canonical "AI's increasing status as infrastructure" statement.

E13 mints one new signal — `ai-as-infrastructure` — anchored on the 48-hour dual-vendor outage window plus practitioner amplification including the [510-point HN front-page demand for an official Claude Desktop for Linux](https://news.ycombinator.com/item?id=48434436) and [fasterthanli.me's Anthropic install-footprint critique](https://bsky.app/profile/fasterthanli.me/post/3mnjumq6yis2o). The signal is distinct from `agent-production-destruction` (which is about agent-runtime runaway in production) and from `anthropic-trust-arc` (which is about Anthropic-specific vendor trust): `ai-as-infrastructure` is a multi-vendor availability-class framing that reframes vendor-tool reliability from productivity preference to SRE-class concern.

The most consequential E13 macro-shift is `cost-runaway` graduating from FinOps-formalization (E11–E12 framing) into **sector-wide pricing-model realignment**. [GitHub Copilot moved all plans to usage-based billing on June 1](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/); within five days, [Cursor responded by CUTTING prices and adding enterprise spend controls](https://thenewstack.io/cursor-pricing-token-billing/) — explicitly framed by The New Stack as a "tokenomics reckoning." [Simon Willison reported Uber caps coding agents at $1,500/month per employee per tool](https://bsky.app/profile/simonwillison.net/post/3mnf2w4ctnc2n), the first concrete enterprise spend cap in the public record this cycle. [Kilo.ai's "The GitHub Copilot Bill Came Due"](https://blog.kilo.ai/p/the-github-copilot-bill-came-due) codifies the engineering-leader response pattern ("predict, cap, alert"); [Ask HN: "Copilot pricing exploding"](https://news.ycombinator.com/item?id=48444008) confirms the vocabulary; [Show HN: Cost.dev (YC W21)](https://cost.dev/) is the tooling-side response; and [Abhishek Shankar's "The AI Coding Bill Is a Headcount Problem in Disguise"](https://abhishek-shankar.com/posts/ai-coding-bill-headcount-problem) reframes pricing pressure as org-design problem. The cost-runaway signal has now traversed dev-tool-line-item complaint (E6–E8) → trust-failure dimension (E9–E10) → FinOps-formalization (E11–E12) → **sector-pricing realignment + cost-as-headcount** (E13) — four discrete phases over eight windows, the longest signal arc in the program.

`anthropic-trust-arc` reaches 7 windows (E4–E8 + E12–E13) and compounds in E13 across three axes simultaneously: the [June 2 Opus 4.6 outage](https://status.claude.com/), the [HN Linux-desktop trust gap](https://news.ycombinator.com/item?id=48434436), and [fasterthanli.me's UX papercuts critique](https://bsky.app/profile/fasterthanli.me/post/3mnelaurqak2c). `vibe-coding-disreputed` reaches 5 windows with both a cautionary tale and a legitimization counterweight in the same week: the [rsync 'Please Do Not Vibe Fuck Up This Software' incident](https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189) is the OSS-maintainer-policy exemplar; [Wes McKinney's MotherDuck "Vibe Coding Is Dangerous, Agentic Engineering Isn't"](https://motherduck.com/blog/vibe-coding-dangerous-agentic-engineering-wes-mckinney/) explicitly codifies the terminological split; and [CNBC reports Supabase raised $500M at a $10.5B valuation on a "vibe-coding tailwind"](https://www.cnbc.com/2026/06/04/database-startup-supabase-raises-500-million-10point5-billion-valuation.html). The signal evolves toward a terminological-bifurcation framing rather than a uniform-disrepute framing.

A separate emerging Microsoft trust deficit pattern compounds in window — [Kotaku/404 Media reported a leaked Microsoft strategy framing Copilot as designed for "addictive" engagement](https://kotaku.com/microsoft-ai-scout-addictive-satya-nadella-404-media-copilot-2000702924), landing on the same week as the billing transition AND the Copilot outage. The capability expansion that GitHub also shipped this week — [larger context windows + configurable reasoning levels](https://github.blog/changelog/2026-06-04-larger-context-windows-and-configurable-reasoning-levels-for-github-copilot/) and the [Copilot Agent Tasks REST API GA](https://github.blog/changelog/2026-06-04-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max/) — is increasingly read through the "addictive" framing. Held this window pending second confirming window before minting `microsoft-trust-arc`.

A disciplined-adoption counter-camp gains coherence: [Show HN: Lathe — LLMs to learn a new domain, not skip past it (363 pts)](https://news.ycombinator.com/item?id=48433756) is the explicit counter-design to `cognitive-debt-deskilling`; [Launch HN: Hyper (YC P26) company brain for agentic dev (78 pts)](https://news.ycombinator.com/item?id=48387095) is the org-knowledge-for-agents pattern; [the NBER working paper on productivity effects across generations of AI coding tools](https://www.nber.org/system/files/working_papers/w35275/w35275.pdf) is the academic-grade datum; and [VentureBeat's "Agentic AI solved coding and exposed every other problem in software engineering"](https://venturebeat.com/technology/agentic-ai-solved-coding-and-exposed-every-other-problem-in-software-engineering) reframes the productivity discussion away from raw code generation. [The New Stack's six-month Claude Code vs Cursor vs Codex vs Antigravity retrospective](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/) and [Clay Nicholson's Claude Code wrapper](https://claynicholson.com/blog/khlawde-code) anchor the disciplined-stack-composition end.

Sentiment composition shifts decisively from E12: **SN spikes to 24% (↑8 from E12's 16%)** on the dual outage + rsync regression + Microsoft "addictive" leak + fasterthanli.me critique; **CN drops to 31% (↓12 from 43%)** as the headline shifts from steady-state critique to acute fragility; MA holds 14% flat; CP slips to 12% on the disciplined-adoption camp's quieter signals. **Critical composition caveat (escalated regime — FIFTH consecutive zero-Reddit window)**: the Chrome-augmented supplemental pass restored 6 Bluesky items + 1 Mastodon item, but Reddit remains hard-blocked at the plugin safety layer. The SN/CN spike must be read as analyst-publication-corpus-weighted with partial practitioner-voice restoration.

**Highest-priority next-window watch**: Anthropic public post-mortem for the June 2 Opus 4.6 outage; Microsoft Copilot post-mortem for the June 1 outage; Copilot AI Credits week-2 practitioner reaction; Reddit retrieval restoration (config v1.9 demotion or interactive-Chrome pattern).

---

## Source Composition Audit

| Window | Items | Reddit | HN | Blogs/Pubs | Bluesky | Mastodon | YouTube | X/Twitter | Incidents |
|--------|------:|-------:|---:|-----------:|--------:|---------:|--------:|----------:|----------:|
| E1 (3/20–25) | 50 | yes | yes | yes | - | - | - | - | 6 |
| E2 (3/23–30) | 53 | yes | yes | yes | yes | - | yes | - | 4 |
| E3 (3/28–31) | 19 | partial | yes | yes | - | - | yes | - | 7 |
| E4 (3/30–4/6) | 44 | yes | yes | yes | yes | - | yes | yes | 5 |
| E5 (4/6–13) | 53 | yes | yes | yes | yes | - | yes | yes | 5 |
| E6 (4/13–20) | 61 | yes | yes | yes | yes | yes | yes | yes | 5 |
| E7 (4/20–27) | 58 | yes | yes | yes | yes | yes | yes | yes | 8 |
| E8 (4/27–5/4) | 48 | yes (browser) | yes | yes | partial | zero | yes | yes | 10 |
| E9 (5/4–11) | 50 | yes (Grok proxy) | yes | yes | yes | yes | partial (T2) | yes | 7 |
| E10 (5/11–18) | 70 | metadata via Grok relay (suppl) | yes | yes | yes (suppl) | zero | partial (T2) | partial | 9 |
| E11 (5/18–25) | 42 | **zero** | yes (1) | yes (41) | **zero** | **zero** | zero | partial (1) | 6 |
| E12 (5/25–6/1) | 49 | **zero** | yes (5) | yes (32) | **zero** | **zero** | yes (5) | **zero** | 7 |
| E13 (6/1–6/8) | **37** | **zero** | yes (20) | yes (15) | **yes (6)** | partial (1) | yes (5, T1.5) | zero | 4 |

**Composition anomalies (E13-specific, revised after Chrome-augmented supplemental pass):**

- **FIFTH consecutive zero-Reddit window.** Chrome plugin safety layer hard-blocks www.reddit.com navigation AND cross-origin fetch. The structural-composition regime has now persisted through five consecutive weeks.
- **Bluesky restored to 6 Tier-1 items** (Simon Willison ×3, Kelsey Hightower, fasterthanli.me ×2) — first non-zero Bluesky window since E10. The supplemental Chrome pass live-queried `public.api.bsky.app`.
- **Mastodon partial (1 item, off-topic)**: federated server discovery remains the bottleneck. Need broader handle list across hachyderm.io and infosec-exchange.com.
- **HN posts a program-high 20-item yield** (E12: 5; E11: 1). HN dominated Tier-1 this week with 510 / 363 / 78 / 67-point items, plus Ask/Show/Launch HN diversity.
- **YouTube returns at 5 Tier-1.5 items** — all from Theo - t3.gg (62k–65k view range). ThePrimeagen and Fireship had no in-window AI uploads.
- **X / Twitter not attempted** this pass — Chrome plugin safety likely blocks; fxtwitter / nitter proxy fallback not implemented.

**Composition verdict (full program through E13)**: pre-E9 (E1–E8) remains the stable mid-window-composition cohort. E9–E10 are the "Grok-proxy / browser rescue" cohort. **E11–E13 is the structurally-shifted cohort**, but E13's Chrome-augmented pass partially restored Bluesky coverage. The five-window Reddit gap remains the dominant methodological caveat; the longitudinal record requires explicit retrospective re-weighting for E11–E13 comparisons against E1–E10.

---

## Sentiment Trajectory

| Window | SP | CP | MA | CN | SN | Nu | Direction (vs prev) |
|--------|---:|---:|---:|---:|---:|---:|---------------------|
| E1 | 2% | 18% | 18% | 26% | 20% | 16% | — |
| E2 | 4% | 15% | 19% | 28% | 30% | 4% | SN↑ (technical-risk surge) |
| E3 | 0% | 16% | 5% | 16% | 63% | 0% | SN↑↑ (small-corpus, incident-heavy) |
| E4 | 2% | 20% | 14% | 18% | 41% | 5% | SN↓ as discourse broadens |
| E5 | 4% | 13% | 17% | 11% | 43% | 11% | SN stable; Nu rising |
| E6 | 3% | 13% | 10% | 34% | 13% | 26% | **Major shift**: SN→CN; Nu doubles |
| E7 | 0% | 9% | 41% | 19% | 17% | 7% | MA peak (postmortem season) |
| E8 | 0% | 6% | 19% | 44% | 17% | 15% | CN series high (vendor-trust collapse) |
| E9 | 6% | 8% | 18% | 30% | 16% | 22% | **CN retreat**; SP off floor (CC announcement) |
| E10 | 2% | 10% | 12% | 42% | 18% | 16% | **CN re-climb** toward E8 high; SP retreats |
| E11 | 2% | 12% | 12% | 43% | 14% | 17% | CN holds at structural-risk floor; SN cools; CP recovers |
| E12 | 2% | 12% | 12% | **43%** | 16% | 14% | CN flat; SN ticks up on new May incidents |
| E13 | **3%** | 12% | 14% | **31%** | **24%** | 16% | **CN drops 12, SN spikes 8** — acute-incident + tokenomics-reckoning shift |

**Composition-adjusted reading**: E13's CN→SN shift of ~12 points is the sharpest single-window movement since the E5→E6 SN→CN transition. The shift is driven by the dual outage (Microsoft Copilot June 1 + Anthropic Claude June 2) + rsync regression + Microsoft "addictive" leak — four within-window acute-incident-class items. Without Reddit primary-channel practitioner voice (fifth consecutive zero window), the trajectory must be read as analyst-corpus + restored-Bluesky weighted rather than as a community-wide sentiment regime change. The structural CN floor (~30–43% across E6–E13) is the more durable signal of the program's settled state.

---

## Cluster Momentum

| Cluster | E10 | E11 | E12 | E13 | Trajectory | Signal Strength |
|---|---:|---:|---:|---:|---|---|
| Pricing / Cost | 6 | 10 | 11 | **14** | ↑↑ four-window monotonic; sector realignment | Emerging Consensus |
| Dependency / Resilience | 5 | 4 | 8 | **12** | ↑↑ program-high | Emerging Consensus |
| Incidents / Failures | 12 | 8 | 11 | 11 | flat at high; dual-outage anchor | Emerging Consensus |
| Architectural Philosophy | 14 | 16 | 16 | 10 | ↓ small reset; Nu-dominant | Active Debate |
| Tool-Specific Issues | 8 | 7 | 7 | 9 | ↑ retrospective + wrapper + GPT-5.2 deprecation | Growing Trend |
| Trust / Verification | 14 | 14 | 13 | 8 | ↓ acute-incident displacement | Growing Trend |
| Productivity Reality | 12 | 9 | 14 | 7 | ↓ post-Pragmatic Engineer week | Active Debate |
| Enterprise / Policy | 4 | 8 | 7 | 6 | ↑ Uber cap + Copilot enterprise billing | Active Debate |
| Code Quality | 18 | 17 | 18 | 5 | ↓↓ acute-incident displacement | Growing Trend |
| Hype vs Reality | 5 | 5 | 8 | 4 | ↓ small | Active Debate |
| Job Security / Hiring | 4 | 6 | 9 | 2 | ↓ E13 silent | Isolated Signal |
| Learning & Skill Development | 8 | 6 | 10 | 1 | ↓ Show HN: Lathe sole anchor | Isolated Signal |

**Momentum highlights**:

- **Pricing / Cost** posts its program-high mention rate (14 in a 37-item corpus = 38%) — the four-window monotonic E10→E11→E12→E13 trajectory (6 → 10 → 11 → 14) is the program's most durable rising trend. Signal Strength: Emerging Consensus.
- **Dependency / Resilience** posts its program-high (12) — direct corollary of the dual outage + Thoughtworks "AI as infrastructure" framing.
- **Incidents / Failures** stays at the prior-window's elevated level. The four anchors (Microsoft Copilot June 1, Anthropic June 2, rsync, Microsoft "addictive" leak) replace the prior framing.
- **Trust / Verification** declines as the trust conversation diffuses into Pricing/Cost and Dependency/Resilience clusters.
- **Code Quality and Productivity Reality both retreat sharply** — acute-incident-and-pricing coverage displaces steady-state discussion. Expect rebound in E14 as the analyst layer processes post-cutover billing data.

---

## Signal Evolution

| Signal | First Obs | Last Obs | Obs Count | Status | Trajectory | Latest Confidence | Recommended Action |
|---|---|---|---:|---|---|---|---|
| `cost-runaway` | E6 (4/20) | **E13 (6/08)** | **8** | Promoted | **Sector pricing realignment phase (Copilot up, Cursor down) + cost-as-headcount reframe** | H | Continue; track post-cutover sentiment shock E14 |
| `cve-acceleration` | E1 (3/25) | E12 (6/01) | 7 | Promoted | Quiet this window — no academic / analyst datum | M | Hold — likely E14 rebound when post-cutover code-quality data publishes |
| `mcp-attack-surface` | E1 (3/25) | E12 (6/01) | 7 | Promoted | Quiet this window | M | Hold |
| `anthropic-trust-arc` | E4 (4/06) | **E13 (6/08)** | **7** | Promoted | **Three-axis compound — outage + Linux desktop gap + UX papercuts** | M | Continue; outage post-mortem is highest-leverage E14 |
| `agent-production-destruction` | E4 (4/06) | E12 (6/01) | 5 | Promoted | Quiet this window — no in-window vendor-side runaway | H | Hold — adjacent to `ai-as-infrastructure` |
| `stack-composition` | E4 (4/06) | **E13 (6/08)** | **6** | Promoted | Six-month retrospective + wrapper + Hyper YC org-knowledge anchor | M | Continue |
| `vibe-coding-disreputed` | E1 (3/25) | **E13 (6/08)** | **5** | Promoted | **Critical-infra exemplar (rsync) + terminological-bifurcation codification (McKinney) + legitimization counterweight (Supabase)** | H | Continue; rsync 3.5 outcome is load-bearing test |
| `productivity-paradox` | E3 (3/31) | E12 (6/01) | 5 | Promoted | Quiet this window | H | Hold — E14 rebound expected on NBER paper + post-cutover data |
| `cognitive-debt-deskilling` | E2 (3/30) | **E13 (6/08)** | **5** | Promoted | **Disciplined-adoption counter-camp (Show HN: Lathe 363pts, NBER, VentureBeat)** | H | Continue |
| `ai-burnout-paradox` | E3 (3/31) | E5 (4/13) | 3 | Promoted | Dormant 7+ windows | H | Watchful — retire if not reactivated by E15 |
| `review-cost-inversion` | E9 (5/11) | E12 (6/01) | 4 | Promoted (E12) | Quiet this window | H | Hold — expect E14 rebound on post-cutover review-cost data |
| `junior-pipeline-collapse` | E2 (3/30) | E12 (6/01) | 3 | Promoted (E12) | Quiet this window | H | Hold |
| `delegation-gap-paradox` | E9 (5/11) | E12 (6/01) | 4 | Promoted (E12) | Quiet this window | H | Hold |
| `reset-year-narrative` | E7 (4/27) | E12 (6/01) | 3 | Promoted (E12) | Quiet this window | M | Hold |
| `agent-infrastructure-inflection` | E10 (5/18) | E12 (6/01) | 3 | Tracking | Quiet this window — but partly absorbed by new `ai-as-infrastructure` framing | H | Continue; consider merger candidate with `ai-as-infrastructure` |
| `ai-dependency-trap` | E12 (6/01) | E12 (6/01) | 1 | Tracking | Quiet this window | H | Hold — second observation needed for promotion |
| `ai-as-infrastructure` | **E13 (6/08)** | **E13 (6/08)** | **1** | **NEW Tracking** | Dual-vendor outage week + Thoughtworks canonical framing + 510-pt HN Linux desktop demand | H | Continue; second observation in E14 promotes |
| `cursor-xai-acquisition` | E6 (4/20) | E7 (4/27) | 2 | Tracking | Dormant 6 windows | M | Candidate retire |
| `enterprise-ai-controls` | E6 (4/20) | E6 (4/20) | 1 | Tracking | Dormant 7 windows | M | Candidate retire — folded into `cost-runaway` |
| `oss-maintainer-pushback` | E8 (5/04) | **E13 (6/08)** | **2** | Tracking | rsync row reactivates | M | Continue; second observation moves toward promotion |
| `senior-deskilling` | E7 (4/27) | E8 (5/04) | 2 | Tracking | Dormant 5 windows | H | Candidate folded into `cognitive-debt-deskilling` |
| `thoughtworks-radar-formalization` | E4 (4/06) | E12 (6/01) | 2 | Tracking | Picked back up E12 via Radar v34 | H | Continue |

**Confirmed trends (highest cross-window observation counts)**:

- **`cost-runaway` (8 obs across 8 of last 8 windows)** — the strongest continuing-observation rate in the program; longest multi-phase signal arc.
- **`anthropic-trust-arc` (7 obs)** — compounds again in E13.
- **`cve-acceleration` / `mcp-attack-surface` / `stack-composition` (7, 7, 6 obs)** — well-established maturity signals.
- **`vibe-coding-disreputed` / `cognitive-debt-deskilling` (5 each)** — reactivated in E13 with new anchors.

**Signal regime observation**: of the 22 signals tracked across the program, 7 appeared in E13 plus 1 new mint = 8 active. Consistent with E11's 36% active rate and lower than E12's 67% — reflects the E13 narrowness on dual-outage + tokenomics-reckoning displacing steady-state discussion.

---

## Cross-Extraction Contradictions

| Claim | First Position | Current Position | Evolution | Assessment |
|---|---|---|---|---|
| AI coding tools deliver net productivity gains at sustainable cost | E1: Cautious-Positive | **E13: Tilting Negative** (Uber cap + Copilot AI Credits + Cursor cut + Kilo.ai playbook + cost-as-headcount reframe) | Sector pricing realignment tilts decisively against sustainable-cost claim | **Tilting Negative** |
| AI-assisted code in critical infrastructure is acceptable when expert-supervised | E2: Cautious-Positive (early Tridgell adoption news) | **E13: Contested** (rsync 3.4.3 regressions vs Wes McKinney's disciplined-engineering framing) | OSS-maintainer-policy row puts the question into formal dispute | **Contested** |
| AI coding tools and providers are reliable enough for load-bearing production use | E2–E4: Mixed/Ambivalent | **E13: Tilting Negative** (Microsoft Copilot June 1 + Anthropic Claude June 2 dual outage; Thoughtworks framing; HN Linux-desktop demand) | Dual-vendor 48h outage + practitioner amplification tilt strongly negative | **Tilting Negative** |
| Vibe coding is uniformly dangerous | E11: Trending Confirmed | **E13: Newly Contested** (Supabase $10.5B valuation on "vibe-coding tailwind" vs Wes McKinney terminological split) | Capital-side legitimization counterweight against critical-infra cautionary tale | **Newly Contested** |
| Microsoft AI product strategy operates in users' interests | Implicit through E12 | **E13: Tilting Negative** (Kotaku "addictive" leak + Copilot outage on billing-cutover day + GPT-5.2 deprecation churn) | First multi-axis Microsoft trust deficit framing in the program | **Tilting Negative — single-window single-vendor; promote in E14 if confirms** |
| AI-coding cost is a manageable per-seat expense | E1: Confirmed | E12: Trending Negative → **E13: Resolved Negative** (Uber + Copilot AI Credits + Cursor token billing convergence) | Per-seat-billing era is over; usage-based is the new default | **Resolved Negative** |
| AI-generated code is no more vulnerable than human-written code | E1: Trending Contested | E12: Resolved Negative | Stable resolution; E13 quiet (no in-window academic datum) | **Resolved Negative (stable)** |
| MCP attack surface is theoretical / vendor-disputed only | E1: Trending Contested | E12: Resolved Negative | Stable resolution; E13 quiet | **Resolved Negative (stable)** |

**Newly resolved**: cost-per-seat (Resolved Negative E13).
**Newly contested**: vibe-coding uniformly dangerous (E13 Supabase counterweight); Microsoft AI strategy in users' interests (E13 — first multi-axis Microsoft trust deficit).
**Tilting movements**: AI productivity-vs-cost (Tilting Negative E13); load-bearing reliability (Tilting Negative E13).

---

## Vocabulary & Framing Drift

| Term | First Appeared | Frequency Trend | Significance |
|---|---|---|---|
| "Vibe coding" (failure mode) | E1 | Stable high through E13 with "Vibe Fuck Up" escalation in rsync row | Critical-infra contributor norm using the term as cautionary label |
| "AI dependency trap" | E12 | Reinforced E13 (Uber cap + HN skeptic framing) | Behavioral lock-in framing distinct from cognitive-debt |
| "Cognitive debt" | E2 | E12 Thoughtworks Radar v34 Trial; quiet E13 | Institutional formalization established |
| "Harness engineering" | E12 | Quiet E13 | Vendor-prescription label; await E14 spread |
| "AI Slop" | E11 | Echo E12; reactivated E13 via Simon Willison HN-slop-tolerance critique | Critic-side framing of AI-generated-content volume |
| "Stack composition" (operator framing) | E4 | Reinforced E13 (six-month retrospective + Clay Nicholson wrapper + Hyper YC) | Multi-tool composition now mainstream |
| **"Tokenomics reckoning"** | **E13 NEW** | Single observation (The New Stack) | Sector-wide pricing-model-shift framing — distinct from per-vendor pricing complaints |
| **"AI Credits" (GitHub billing unit)** | **E13 NEW** | Single observation | New billing unit for usage-based-billing era (1 credit = $0.01) |
| **"Bill Came Due" (engineering-leader framing)** | **E13 NEW** | Single observation (Kilo.ai) | Practitioner anticipation of the cost-runaway tail |
| **"Pricing exploding"** | **E13 NEW** | Single observation (Ask HN) | Dominant practitioner-complaint vocabulary in window |
| **"Cost-as-headcount"** | **E13 NEW** | Single observation (Abhishek Shankar) | Reframes agentic AI spend as developer-equivalent budget line |
| **"Agentic engineering" (vs vibe coding)** | **E13 NEW** | Single observation (Wes McKinney) | Discipline-marker terminological split |
| **"Vibe-coding tailwind"** | **E13 NEW** | Single observation (CNBC) | Investor-narrative framing for capital legitimization |
| **"AI as infrastructure"** | **E13 NEW** | Single observation (Thoughtworks) | Canonical multi-vendor availability-class framing |
| **"More Prompts = Worse Code"** | **E13 NEW** | Single observation (Theo - t3.gg) | Counter to "more agent turns = better" assumption |
| **"Addictive Copilot"** | **E13 NEW** | Single observation (Kotaku/404 Media) | Microsoft strategy-leak framing — dark-pattern accusation |
| **"Macro-delegation"** | **E13 NEW** | Single observation (GitHub CPO interview) | Vendor-side agentic future-of-work framing |

The E13 vocabulary explosion (10 new terms) is the largest single-window vocabulary expansion in the program — driven by the simultaneous sector-pricing event + dual outage week. Most are framing terms rather than technical terms, suggesting a maturing discourse layer rather than novel technical capability emergence.

---

## Gaps & Uncertainties

- **Reddit Tier-1 absent (FIFTH consecutive window)** — Chrome plugin safety layer hard-blocks www.reddit.com navigation AND cross-origin fetch. Structural-composition regime hardened.
- **Mastodon yield very low** (1 off-topic item) — federated server discovery is the bottleneck; broader handle list needed.
- **YouTube depth shallow** — Theo - t3.gg dominated 5 of 5 items.
- **X / Twitter not attempted** this pass — Chrome plugin safety likely blocks; would need fxtwitter / nitter fallback strategy.
- **Anthropic post-mortem for June 2 outage** not published in-window; status page timeline only.
- **Microsoft Copilot post-mortem** not published in-window; likely-authentication-failure framing only.
- **NBER paper w35275 substantive findings** not extracted this pass — high-value disciplined-adoption-camp evidence pending review.
- **Anthropic / Cursor official responses** to the Uber $1,500/mo cap narrative not retrieved in-window.
- **Microsoft trust deficit single-vendor single-window** — second confirming window required before minting `microsoft-trust-arc`.
- **Below-threshold pattern**: self-hosted alternatives accelerating (local-MCP, local Copilot via Lemonade Show HN posts) — no concentrated thread yet.

---

## Watch List for Next Extraction

- **Anthropic public post-mortem for the June 2 Opus 4.6 outage**. *Highest priority.* Resolves whether `ai-as-infrastructure` is vendor-side-root-cause-confirmed.
- **Microsoft Copilot post-mortem for the June 1 outage**. *Highest priority.* Authentication-failure-vs-other root cause has implications for Microsoft trust deficit framing.
- **GitHub Copilot AI Credits post-cutover practitioner reaction (Jun 8–15)**. *Highest priority.* First empirical test of cost-runaway's sector-pricing-realignment phase.
- **Reddit / Bluesky / Mastodon retrieval restoration**. *Highest priority.* Five-consecutive-window structural-regime gap (Bluesky partially restored in E13 via Chrome supplemental pass).
- **Cursor enterprise spend controls detail** — what governance primitives ship matters for how the cost-as-headcount framing lands at procurement teams. High priority.
- **Anthropic / Cursor vendor responses to Uber $1,500/mo cap narrative**. High priority — pricing-narrative-response is the natural follow-up.
- **rsync 3.5 security-focused release outcome**. High priority — contributor-norm crystallization test of `vibe-coding-disreputed` resolution.
- **NBER paper w35275 substantive findings** — quantitative summary needed for next-window analysis. High priority.
- **Microsoft trust-deficit second window confirm** — if a second axis surfaces in E14, mint `microsoft-trust-arc` as new signal. Medium priority.
- **Theo transcripts** — "I didn't expect this from Anthropic" (same-day) and "More Prompts = Worse Code?" — both high-engagement practitioner takes on in-window themes. Medium priority.

---

## Longitudinal Report Metadata

| Field | Value |
|-------|-------|
| Longitudinal prompt | v1.3 |
| Domain config | v1.2 |
| Bootloader | v1.9 |
| Report generated | 2026-06-08 15:45 UTC |
| Input mode | summaries (--from-summaries) |
| Extractions covered | E1 through E13 |
| Date range | 2026-03-20 – 2026-06-08 (80 days) |
| Total tagged items | ~634 (sum across summaries; E13 revised to 37-item Chrome-augmented corpus) |
| Tracked signals | 22 unique signal_ids across the program; 12 Promoted, 6 Tracking, 4 candidate retire-or-merge |
| NEW signals this window | `ai-as-infrastructure` |
| Escalated signals this window | none — all four E12 promotions hold; `ai-dependency-trap` at 1 obs E12; `oss-maintainer-pushback` reactivated at 2 obs (rsync) |
| Confirmed trends | `cost-runaway` (8 obs, sector pricing realignment), `anthropic-trust-arc` (7 obs, three-axis compound), `cve-acceleration` / `mcp-attack-surface` (7 obs each), `stack-composition` (6 obs), `cognitive-debt-deskilling` / `vibe-coding-disreputed` (5 obs each, both reactivated E13) |
| Resolved contradictions | "AI-coding cost is manageable per-seat expense" (Resolved Negative E13); prior resolutions hold |
| Newly contested claims | "Vibe coding is uniformly dangerous" (Newly Contested E13 — Supabase counterweight); "Microsoft AI strategy operates in users' interests" (Tilting Negative E13 — first multi-axis trust deficit framing); "Load-bearing AI reliability acceptable" (Tilting Negative E13); "AI productivity gains under longitudinal measurement" (Tilting Negative E13) |
