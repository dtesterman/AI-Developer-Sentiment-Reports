# Longitudinal Trend Report: 2026-03-20 – 2026-06-08 (Extractions 1 – 13)

## Executive Summary

Across thirteen consecutive weekly extractions spanning 80 days (~632 sentiment-tagged items including E10's supplemental pass and E13's 35-item analyst-shifted corpus), the AI coding tools discourse has executed a clear regime-shift sequence from "is the code any good?" (E1–E3) → "is the agent safe?" (E4–E7) → "is the harness right?" (E8–E9) → "who governs the gate?" (E10) → "who pays the review cost?" (E11) → "who pays the cognitive cost of being unable to work without?" (E12 — `ai-dependency-trap` mint) → and now in **E13 to "is the infrastructure load-bearing?"** — a fragility-and-cost reckoning week that lands the [June 5 Claude / Claude Code global outage](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-outage-june-2026) (Claude Code sub-agent infinite-loop bug exponentially multiplying sub-agents and wiping user token allowances within minutes — the **first vendor-side root-cause exemplar** of `agent-production-destruction`), simultaneously with [Uber's $1,500/tool/month employee cap after burning the full-year AI budget in four months](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs) and [GitHub Copilot's June 1 transition to usage-based "AI Credits" billing](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/) on the same Monday.

E13 mints one new signal — `vendor-model-independence` — anchored on [Microsoft's MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) (5B parameters, 256K context, explicitly no OpenAI/Anthropic distillation) and its same-day rollout into [GitHub Copilot](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/), with [Simon Willison's commentary](https://simonwillison.net/2026/Jun/2/microsofts-new-models/) framing both new MAI models (Thinking-1 1T MoE + Code-1-Flash 5B). The signal is distinct from `stack-composition` (practitioner-side multi-tool composition) and `cost-runaway` (price/value response) — it is the **vendor-side hyperscaler reduction in dependency on frontier-lab APIs** for AI coding. Bench-marketing language (SWE-Bench Pro +16-point lead vs Claude Haiku 4.5's 35.2%, 60% fewer tokens on SWE-Bench Verified) is the dominant comparison axis.

The most consequential E13 institutional event is the Thoughtworks-editorial framing "When an LLM provider goes down, internal dev velocity drops, support triage bots fall silent, and LLM-dependent data pipelines freeze" — the canonical statement of AI-as-infrastructure that the program has been building toward since E2's first incident exemplars. `agent-production-destruction` now has five exemplars across two sub-classes: customer-side runaway (PocketOS, Kiro, Composio) and vendor-side availability + sub-agent root-cause (May 14 capacity outage, June 5 sub-agent runaway). `anthropic-trust-arc` reaches 7 windows (E4–E8 + E12–E13) and compounds in E13 across three axes simultaneously: outage + unconfirmed [cross-tenant inference-leak rumor](https://x.com/kimmonismus/status/2062997809067139468) + [HN front-page Claude-Desktop-for-Linux trust gap](https://news.ycombinator.com/item?id=48434436).

The third E13 macro-shift is `cost-runaway` graduating from FinOps-formalization (E11–E12 framing) into **budget-cap inflection** — the Uber datum is the first published vendor-side budget-cap policy at scale. The signal has now traversed dev-tool-line-item complaint (E6–E8) → trust-failure dimension (E9–E10) → FinOps-formalization (E11–E12) → budget-cap inflection (E13) — four discrete phases over eight windows, the longest signal arc in the program.

`vibe-coding-disreputed` reaches 5 windows with the [rsync 'Please Do Not Vibe Fuck Up This Software' incident](https://www.theregister.com/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189) as its first critical-infrastructure exemplar — rsync 3.4.3 broke incremental backup workflows; dozens of commits since 3.4.1 attributed to "tridge and claude"; Tridgell acknowledged regressions, blamed test-suite gaps, and plans to continue AI-assisted dev through 3.5. Paired with [Martin Fowler's 14-25x security-bug-volume datum](https://martinfowler.com/fragments/2026-06-02.html) and the [June 6 HN dev-stack thread's spec-driven 'sword and shield' mainstream](https://news.ycombinator.com/item?id=48413629), the critical-infrastructure contributor norm is crystallizing.

`mcp-attack-surface` extends from protocol-class CVE arc (E1–E10) into systemic LLM-execution-boundary hardening (E13): [OpenAI Lockdown Mode](https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/), Simon Willison's [MicroPython/WASM sandbox alpha](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/) with GPT-5.5 hardening test, the [Meta AI Instagram prompt-engineering attack](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/), and the [github.dev OAuth token-theft HN thread's pivot to LLM-agent push-permission risk](https://news.ycombinator.com/item?id=48371562). The pattern in aggregate: practitioners are explicitly hardening LLM execution boundaries as agentic systems gain network and tool access.

Sentiment composition shifts decisively from E12: **SN spikes to 24% (↑8 from E12's 16%)** on the Claude outage + four within-window incidents; **CN drops to 31% (↓12 from 43%)** as the headline shifts from steady-state critique to acute-incident SN; MA holds 14% flat; CP slips 0 to 12% on [Opus 4.8 quiet-competence side-by-side](https://news.ycombinator.com/item?id=48362551) (notably framing 4.7 as a regression) + MAI-Code-1-Flash bench positioning. **Critical composition caveat (escalated regime — FIFTH consecutive zero-Reddit/Bluesky/Mastodon window)**: the SN spike must be read as analyst-publication-corpus-shifted, not as a primary-channel practitioner-sentiment shift. The five-window structural-regime gap is the most important methodological caveat in the full longitudinal record.

Two prior Tracking signals (`vendor-model-independence` minted at 1 obs E13; the `ai-dependency-trap` mint from E12 awaiting E13 corroboration — partially corroborated by Uber's cost-cap narrative and the [HN dev-stack thread's skeptic-vs-mainstream split](https://news.ycombinator.com/item?id=48413629)). **Highest-priority next-window watch**: Anthropic public post-mortem for the June 5 sub-agent runaway, cross-tenant-leak confirm/deny, Copilot AI Credits post-cutover sentiment, and the [Anthropic subscription split](https://news.ycombinator.com/item?id=48413629) June 15 aftermath.

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
| E13 (6/1–6/8) | **35** | **zero** | yes (10) | yes (16) | **zero** | **zero** | **zero** | partial (2) | 4 |

**Composition anomalies (E13-specific):**

- **FIFTH consecutive zero-Reddit window.** Confirmed at the crawler level (HTTP 400 on `allowed_domains=['reddit.com']`); no browser workaround or Grok proxy invoked this run. The structural-composition regime has now persisted through five consecutive weeks.
- **FIFTH consecutive zero-Bluesky / zero-Mastodon window.** Both Tier-1 social platforms returned zero verifiable in-window items via WebSearch. Index lag + undated permalinks remain the binding constraint.
- **YouTube regresses to zero yield** from E12's 5. ThePrimeagen's "Claude's New Plans Is a Trap" appears to predate the window; no Tier-1.5 video could be match-verified to Jun 1–8.
- **HN recovers strongly to 10-item yield** (E12: 5; E11: 1). HN is now the dominant practitioner-aggregator Tier-1 source, carrying 5 of E13's top-13 items (front-page outage, config deep-dive at 556pts, token-theft at 399pts, Opus 4.8 side-by-side, dev-stack thread).
- **Tier-1 blogs/publications at 16/35 items (46%)** — analyst-publication share remains high but HN proportion rises. Combined HN + blogs share is 26/35 = 74%; Tier-2 X/podcasts adds 4 items.
- **Lowest item count of any non-E3 window**: 35 items vs program mean ~50. The combination of Reddit/Bluesky/Mastodon/YouTube zero yields with a thin Tier-1.5 layer concentrates the corpus onto HN + analyst blogs + news outlets.

**Composition verdict (full program through E13)**: pre-E9 (E1–E8) is the stable mid-window-composition cohort with broad social-platform coverage. E9–E10 are the "Grok-proxy / browser rescue" cohort. **E11–E13 is the structurally-shifted cohort** (three consecutive unrescued zero-Reddit/Bluesky/Mastodon windows). The five-window stretch confirms the social-platform-Tier-1 retrieval pipeline is structurally failing in the standard automated configuration. **Re-affirmed regime annotation**: pre-E11 and E11–E13 should be weighted separately in any sentiment-trend arithmetic across the full program. E13 specifically is the smallest unrescued window in the cohort and most acutely composition-shifted.

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
| E13 | **3%** | 12% | 14% | **31%** | **24%** | 16% | **CN drops 12, SN spikes 8** — acute-incident shift; analyst-corpus composition caveat |

**Composition-adjusted reading**: E13's CN→SN shift of ~12 points is the sharpest single-window movement since E6's E5→E6 sentiment transition (SN→CN-driven by analyst layer). The CN→SN movement is driven by four within-window incidents (Claude outage, rsync, github.dev token theft, Meta AI), not by a regime shift in steady-state critique. Without primary-channel practitioner voice (zero Reddit/Bluesky/Mastodon for the fifth window), the trajectory must be read as "analyst-corpus emphasis on acute incident severity" rather than as a community-wide sentiment regime change. The CN→SN swing is consistent with the historic pattern that high-incident weeks pull mass from steady CN into acute SN; the structural CN floor (~30–43% across E6–E13) is the more durable signal of the program's settled state.

---

## Cluster Momentum

| Cluster | E10 | E11 | E12 | E13 | Trajectory | Signal Strength |
|---|---:|---:|---:|---:|---|---|
| Code Quality | 18 | 17 | 18 | 9 | ↓ acute-incident displacement | Emerging Consensus |
| Architectural Philosophy | 14 | 16 | 16 | 10 | ↓ small reset; Nu-dominant | Active Debate |
| Trust / Verification | 14 | 14 | 13 | 12 | flat | Emerging Consensus |
| Review Burden | 9 | 14 | 12 | 4 (was implicit) | ↓ this window's silent cluster | Growing Trend |
| Productivity Reality | 12 | 9 | 14 | 6 | ↓ post-Pragmatic Engineer week | Active Debate |
| Pricing / Cost | 6 | 10 | 11 | **12** | ↑ continuing | Growing Trend |
| Incidents / Failures | 12 | 8 | 11 | **14** | ↑↑ peak | Emerging Consensus |
| Burnout / Cognitive Load | 6 | 7 | 11 | 3 (silent) | ↓ pause | Growing Trend |
| Deskilling / Learning | 8 | 6 | 10 | 3 (silent) | ↓ pause | Growing Trend |
| Hiring / Junior Pipeline | 4 | 6 | 9 | 3 | ↓ counter-narrative emergent | Active Debate |
| Hype vs Reality | 5 | 5 | 8 | 8 | flat | Active Debate |
| Dependency / Resilience | 5 | 4 | 8 | **11** | ↑ peak | Emerging Consensus |
| Tool-Specific Issues | 8 | 7 | 7 | 5 | flat | Growing Trend |
| Enterprise / Policy | 4 | 8 | 7 | 2 | ↓ E13 absence | Active Debate |

**Momentum highlights**:

- **Incidents / Failures** posts its program-high mention rate (14 in a 35-item corpus = 40%) driven by the Claude outage + three other within-window incidents. Signal Strength: Emerging Consensus.
- **Dependency / Resilience** posts its program-high (11) — direct corollary of Incidents/Failures + Thoughtworks AI-as-infrastructure framing.
- **Pricing / Cost** continues its E11→E12→E13 ascent: 10 → 11 → 12. Three-window monotonic rise on Uber + Copilot AI Credits + Simon Willison framing.
- **Code Quality and Productivity Reality both collapse sharply** — not because the topics are resolved, but because acute-incident coverage displaces steady-state discussion. Expect rebound in E14 as the analyst layer processes the events.
- **Review Burden, Burnout, Deskilling, Hiring** all silent or near-silent — clear analyst-corpus narrowing toward the week's headline events.
- **Architectural Philosophy** drops Nu-dominant — HN dev-stack thread + Computex Agentic-PC coverage carry the cluster, but with skeptic/maximalist tension rather than consensus.

---

## Signal Evolution

| Signal | First Obs | Last Obs | Obs Count | Status | Trajectory | Latest Confidence | Recommended Action |
|---|---|---|---:|---|---|---|---|
| `agent-production-destruction` | E4 (4/06) | **E13 (6/08)** | **6** | Promoted | **Vendor-side root-cause confirmed (sub-agent runaway)** | H | Continue tracking; Anthropic post-mortem is highest-leverage E14 retrieval |
| `anthropic-trust-arc` | E4 (4/06) | **E13 (6/08)** | **7** | Promoted | **Compounds — three axes in E13 (outage + leak rumor + Linux desktop trust gap)** | H | Continue; cross-tenant-leak verification is binary watch |
| `cost-runaway` | E6 (4/20) | **E13 (6/08)** | **8** | Promoted | **Budget-cap inflection (Uber + Copilot AI Credits same Monday)** | H | Continue; track post-cutover sentiment shock E14 |
| `cve-acceleration` | E1 (3/25) | **E13 (6/08)** | **8** | Promoted | Continuing — Martin Fowler 14-25x analyst datum + rsync corollary | M (E13 single-source) | Continue; M-confidence pending independent corroboration |
| `mcp-attack-surface` | E1 (3/25) | **E13 (6/08)** | **8** | Promoted | **Extends to systemic LLM-execution-boundary hardening** | M (E13) | Continue; watch second-vendor Lockdown Mode adoption |
| `stack-composition` | E4 (4/06) | **E13 (6/08)** | **6** | Promoted | "Sword and shield" paired-agent named on HN | M | Continue |
| `vibe-coding-disreputed` | E1 (3/25) | **E13 (6/08)** | **5** | Promoted | **Critical-infrastructure exemplar (rsync)** | H | Continue; rsync 3.5 outcome is load-bearing test |
| `productivity-paradox` | E3 (3/31) | E12 (6/01) | 5 | Promoted | Quiet this window | H | Hold — E14 rebound expected |
| `cognitive-debt-deskilling` | E2 (3/30) | E12 (6/01) | 4 | Promoted | Quiet this window | H | Hold — Thoughtworks Radar framing endures |
| `ai-burnout-paradox` | E3 (3/31) | E5 (4/13) | 3 | Promoted | Dormant 6+ windows | H | Watchful — retire if not reactivated by E15 |
| `review-cost-inversion` | E9 (5/11) | E12 (6/01) | 4 | **Promoted at E12** | Quiet this window | H | Hold — expect E14 rebound on post-cutover review-cost data |
| `junior-pipeline-collapse` | E2 (3/30) | **E13 (6/08)** | **4** | Promoted (E12) | **Newly contested (HN remote-vs-AI)** | H | Continue tracking; first credible counter-narrative |
| `delegation-gap-paradox` | E9 (5/11) | E12 (6/01) | 4 | **Promoted at E12** | Quiet this window | H | Hold |
| `reset-year-narrative` | E7 (4/27) | E12 (6/01) | 3 | **Promoted at E12** | Quiet this window | M | Hold |
| `agent-infrastructure-inflection` | E10 (5/18) | E12 (6/01) | 3 | Tracking | Quiet this window — Code w/ Claude consensus held | H | Continue |
| `ai-dependency-trap` | E12 (6/01) | **E13 (6/08)** | **2** | Tracking | **Partially corroborated by Uber cost-cap narrative + HN skeptic-vs-mainstream split** | H | Continue; one more observation to reach promotion |
| `vendor-model-independence` | **E13 (6/08)** | **E13 (6/08)** | **1** | **NEW Tracking** | First emergence — Microsoft MAI-Code-1-Flash + no-distillation positioning + Copilot integration | H | Continue; watch second hyperscaler positioning |
| `cursor-xai-acquisition` | E6 (4/20) | E7 (4/27) | 2 | Tracking | Dormant 6 windows | M | Candidate retire — folded into vendor-model-independence narrative |
| `enterprise-ai-controls` | E6 (4/20) | E6 (4/20) | 1 | Tracking | Dormant 7 windows | M | Candidate retire |
| `oss-maintainer-pushback` | E8 (5/04) | E8 (5/04) | 1 | Tracking | Dormant 5 windows | M | Candidate folded into vibe-coding-disreputed |
| `senior-deskilling` | E7 (4/27) | E8 (5/04) | 2 | Tracking | Dormant 5 windows | H | Candidate folded into cognitive-debt-deskilling |
| `thoughtworks-radar-formalization` | E4 (4/06) | E12 (6/01) | 2 | Tracking | Picked back up E12 via Radar v34 | H | Continue |

**Confirmed trends (highest cross-window observation counts)**:

- **`cost-runaway` (8 obs across 8 of last 8 windows)** — the strongest continuing-observation rate in the program. The signal is now the program's longest-running multi-phase arc.
- **`cve-acceleration` (8 obs across 8 of 13 windows)** — second-longest. Maturity well-established.
- **`mcp-attack-surface` (8 obs across 8 of 13 windows)** — systemic-vulnerability-class established.
- **`anthropic-trust-arc` (7 obs)** — compounds again in E13.
- **`agent-production-destruction` (6 obs, first vendor-side root-cause this window)** — qualitative shift.

**Signal regime observation**: of the 22 signals tracked across the program, only 8 (~36%) appeared in E13. The remaining 14 were either dormant or absent. This is a slightly lower active-signal rate than E11 (10/19 = 53%) or E12 (14/21 = 67%). The E13-specific narrowness reflects the small-corpus + acute-incident-displacement effect, not signal die-off.

---

## Cross-Extraction Contradictions

| Claim | First Position | Current Position | Evolution | Assessment |
|---|---|---|---|---|
| AI coding tools deliver net productivity gains under longitudinal measurement | E1: Cautious-Positive (Pragmatic Engineer / METR pilot framing) | **E13: Tilting Negative** (Uber four-month-budget-burn + Copilot AI Credits + Simon Willison enthusiasts-vs-skeptics) | Maximalist productivity narrative tilts decisively against on empirical cost evidence | **Tilting Negative** |
| AI-assisted code in critical infrastructure is acceptable when expert-supervised | E2: Cautious-Positive (early Tridgell adoption news) | **E13: Contested** (rsync 3.4.3 regressions; Tridgell's continued-AI-use posture + Martin Fowler 14-25x security-bug volume) | Critical-infra contributor norm crystallizing toward "AI-assisted commits acceptable IF test suite catches" | **Contested** |
| AI coding tools and providers are reliable enough for load-bearing production use | E2–E4: Mixed/Ambivalent | **E13: Tilting Negative** (Claude June 5 outage + cross-tenant rumor + OpenAI Lockdown Mode hardening signal) | First vendor-side root-cause + practitioner hardening push tilt strongly negative | **Tilting Negative** |
| Coding-AI vendor lock-in is acceptable because frontier-lab APIs are the only credible option | Implicit consensus through E12 | **E13: Resolved Negative** (Microsoft MAI-Code-1-Flash + Copilot integration + no-distillation posture) | Single-window resolution; hyperscaler-independence positioning is now a public vendor stance | **Resolved Negative** |
| Junior hiring collapse is driven by AI substitution rather than macro-economic conditions | E2: Trending Confirmed (Stanford 13–16% + Anthropic 14%) | **E13: Newly Contested** (HN remote-vs-AI counter-narrative) | First credible counter-narrative to the AI-causal framing | **Newly Contested** |
| AI-coding cost is a manageable per-seat expense | E1: Confirmed | E12: Trending Negative → **E13: Resolved Negative** (Uber + Copilot AI Credits convergence) | Per-seat-billing era is over; usage-based is the new default | **Resolved Negative** |
| Developers can choose to work without AI | Implicit through E11 | E12: Trending Negative (METR-can't-recruit) → **E13: Confirmed by mainstream** (HN dev-stack thread — skeptic positions exist but are marginal) | The choice exists but is increasingly marginal — `ai-dependency-trap` partial corroboration | **Trending Confirmed** (lock-in is real but minority skeptic posture exists) |
| AI-generated code is no more vulnerable than human-written code | E1: Trending Contested | E12: Resolved Negative (Veracode + arXiv 484k + CSA convergence) | Stable resolution; E13's Martin Fowler 14-25x datum reinforces | **Resolved Negative (stable)** |
| MCP attack surface is theoretical / vendor-disputed only | E1: Trending Contested | E12: Resolved Negative | Stable resolution; E13 extends the surface to LLM-execution-boundary hardening | **Resolved Negative (stable)** |

**Newly resolved**: vendor-lock-in (Resolved Negative E13); cost-per-seat (Resolved Negative E13).
**Newly contested**: junior-pipeline-collapse causal claim (HN remote-vs-AI E13 counter-narrative).
**Tilting movements**: AI productivity-vs-cost (Tilting Negative E13); load-bearing reliability (Tilting Negative E13).

---

## Vocabulary & Framing Drift

| Term | First Appeared | Frequency Trend | Significance |
|---|---|---|---|
| "Vibe coding" (failure mode) | E1 | Stable high through E13; "Vibe Fuck Up" escalation E13 | Critical-infra contributor norm now using the term as cautionary label |
| "AI dependency trap" | E12 | Reinforced E13 (Uber + HN skeptic framing) | Behavioral lock-in framing distinct from cognitive-debt |
| "Cognitive debt" | E2 | E12 Thoughtworks Radar v34 Trial-ring named technique; quiet E13 | Institutional formalization established |
| "Harness engineering" | E12 | Quiet E13 | Vendor-prescription label; await E14 spread |
| "AI Slop" | E11 | Echo E12; quiet E13 | Critic-side framing of AI-PR volume |
| "Stack composition" (operator framing) | E4 | Reinforced E13 ("sword and shield") | Multi-tool composition now mainstream |
| **"Sword and shield" (paired-agent)** | **E13 NEW** | Single observation | Practitioner-side risk-reduction pattern naming |
| **"AI Credits" (GitHub billing unit)** | **E13 NEW** | Single observation | New billing unit for usage-based-billing era |
| **"Sub-agent runaway / infinite loop"** | **E13 NEW** | Single observation | Vendor-side failure-mode terminology |
| **"Cross-tenant inference leak"** | **E13 NEW** | Single observation | Most severe trust-scenario framing in the program |
| **"Lockdown Mode" (OpenAI)** | **E13 NEW** | Single observation | Vendor-side execution-boundary hardening feature |
| **"Agentic PC" (Computex 2026)** | **E13 NEW** | Single observation | Vendor-marketing framing replacing "AI PC" |
| **"Spec-driven development" (mainstream)** | **E13 NEW** | Single observation | Post-vibe-coding workflow label |
| **"Project Glasswing" (Anthropic)** | **E13 NEW** | Single observation | Limited cybersecurity rollout of Mythos-class models |
| "FinOps for AI" / boardroom-FinOps | E12 | Reinforced E13 (Uber cap implicitly) | Cost-discipline regime |
| "Boardroom FinOps for AI" | E12 | Echo E13 (Uber datum) | Institutional-formalization of AI cost discipline |
| "Slopsquatting" (Veracode) | E12 | Quiet E13 | Supply-chain-attack class naming |
| "Mini Shai-Hulud" (supply-chain worm class) | E12 | Quiet E13 | TeamPCP supply-chain incident class |

**Vocabulary observation**: E13 mints 8 new terms in a single window — the highest single-window mint rate in the program. This reflects the dense incident + product-launch + framing-event clustering: each major event (outage, MAI launch, Lockdown Mode, github.dev token theft pivot, HN dev-stack thread, Computex pivot, Project Glasswing, Anthropic subscription split anticipation) generates its own terminology layer. Three terms ("Sub-agent runaway", "Cross-tenant inference leak", "AI Credits") are load-bearing operational vocabulary; the rest are framing/marketing labels.

---

## Gaps & Uncertainties

- **Reddit Tier-1 absent for FIVE consecutive windows** — five-window structural regime is the most important methodological caveat in the program. The longitudinal sentiment record materially undersamples the largest practitioner-voice channel. Pre-E11 vs E11–E13 cohort weighting should be applied in any sentiment-trend arithmetic.
- **Bluesky / Mastodon Tier-1 zero for FIVE consecutive windows** — parallel structural gap.
- **YouTube Tier-1.5 regression to zero in E13** — first complete-zero YouTube window since E11.
- **Anthropic public post-mortem for June 5 sub-agent runaway not yet published.** The Thoughtworks editorial framing is the load-bearing secondary; cross-tenant-leak rumor remains unconfirmed by Anthropic.
- **GitHub Copilot AI Credits post-cutover sentiment shock lags 1–2 weeks** — E14 is the first window with material practitioner-side reaction data.
- **rsync 3.4.3 quantified blast radius unknown** — regression count and affected-user count not retrieved beyond "incremental backup workflows broken."
- **Microsoft MAI-Code-1-Flash bench claims** are vendor-self-reported — independent SWE-Bench Pro / Verified replication is the credibility-gate.
- **Anthropic subscription split (June 15) is post-window** — E14 lookback should fully capture the practitioner-side reaction.
- **Anthropic Mythos / Project Glasswing technical detail** is vendor-post only; no third-party benchmark or customer disclosure.

---

## Watch List for Next Extraction

- **Anthropic public post-mortem for the June 5 Claude Code sub-agent runaway**. *Highest priority.* Resolves whether `agent-production-destruction` is vendor-side-root-cause-confirmed (elevating to vendor-architecture-class signal) or stays at availability-class. Cross-tenant inference-leak confirm/deny is the highest-stakes binary in `anthropic-trust-arc`.
- **GitHub Copilot AI Credits post-cutover practitioner reaction (Jun 8–15)**. *Highest priority.* First empirical test of cost-runaway's budget-cap-inflection phase. Expect Reddit and HN volume on AI Credits billing impact.
- **Anthropic subscription split / Agent SDK billing change (June 15)**. *Highest priority.* High topical activity flagged from extraction below-threshold queue; ThePrimeagen + Reddit (if available) + X coverage expected to materialize in E14 window.
- **Reddit / Bluesky / Mastodon retrieval restoration**. *Highest priority.* Five-consecutive-window structural-regime gap; without recovery the longitudinal record requires explicit retrospective re-weighting.
- **Third-party SWE-Bench Pro verification of Microsoft MAI-Code-1-Flash +16-point claim**. High priority — `vendor-model-independence` credibility depends on independent benchmark replication.
- **Cursor / Anthropic vendor response to Uber $1,500/mo cap narrative**. High priority — vendor pricing-narrative-response is the natural follow-up.
- **rsync 3.5 security-focused release outcome**. High priority — contributor-norm crystallization test of `vibe-coding-disreputed` resolution.
- **Second hyperscaler no-distillation positioning** (Google Gemini Code Assist, AWS Q). Medium priority — would advance `vendor-model-independence` from single-vendor framing to industry pattern.
- **Anthropic Project Glasswing technical detail / customer disclosure**. Medium priority — Mythos-class capability anchor.

---

## Longitudinal Report Metadata

| Field | Value |
|-------|-------|
| Longitudinal prompt | v1.3 |
| Domain config | v1.2 |
| Bootloader | v1.9 |
| Report generated | 2026-06-08 13:30 UTC |
| Input mode | summaries (--from-summaries) |
| Extractions covered | E1 through E13 |
| Date range | 2026-03-20 – 2026-06-08 (80 days) |
| Total tagged items | ~632 (sum across summaries; includes E10's +20 supplemental pass and E13's 35-item analyst-corpus window) |
| Tracked signals | 22 unique signal_ids across the program; 12 Promoted, 6 Tracking, 4 candidate retire-or-merge |
| NEW signals this window | `vendor-model-independence` |
| Escalated signals this window | none — all four E12 promotions (review-cost-inversion, junior-pipeline-collapse, reset-year-narrative, delegation-gap-paradox) hold; `ai-dependency-trap` advances to 2 obs (one more needed) |
| Confirmed trends | `cost-runaway` (8 obs, budget-cap-inflection phase), `cve-acceleration` (8 obs), `mcp-attack-surface` (8 obs, LLM-execution-boundary class), `anthropic-trust-arc` (7 obs, three-axis compound), `agent-production-destruction` (6 obs, vendor-side root-cause class) |
| Resolved contradictions | "Vendor lock-in is acceptable because frontier-lab APIs are only option" (Resolved Negative E13); "AI-coding cost is manageable per-seat expense" (Resolved Negative E13); prior resolutions hold |
| Newly contested claims | "Junior hiring collapse is AI-driven not macro-economic" (Newly Contested E13 — first credible counter); "Load-bearing AI reliability acceptable" (Tilting Negative E13); "AI productivity gains under longitudinal measurement" (Tilting Negative E13) |
