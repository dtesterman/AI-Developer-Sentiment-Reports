# Longitudinal Trend Report: 2026-03-20 – 2026-06-01 (Extractions 1 – 12)

## Executive Summary

Across twelve consecutive weekly extractions spanning 73 days (597 sentiment-tagged items including the E10 supplemental pass), the AI coding tools discourse has executed a clear regime shift from "is the code any good?" (E1–E3, dominated by `cve-acceleration` and `mcp-attack-surface` technical-risk signals) through "is the agent safe?" (E4–E7, `agent-production-destruction` and `cost-runaway` become structural) into "is the harness right?" (E8–E9, `quality-as-infrastructure` and `claude-code-automation-platform` crystallize as architectural prescriptions) into "who governs the gate?" (E10), "who pays the review cost?" (E11), and now in E12 into **"who pays the cognitive cost of being unable to work without?"** — a new Tracking signal `ai-dependency-trap` mints this window on the back of [TechCrunch's METR-cannot-recruit reporting](https://techcrunch.com/2026/05/29/coders-are-refusing-to-work-without-ai-and-that-could-come-back-to-bite-them/), the [Anthropic 17% comprehension-drop RCT](https://www.anthropic.com/research/AI-assistance-coding-skills), Amazon's Kirorank internal-leaderboard shutdown after employee gaming, and Uber exhausting its 2026 AI budget in four months without measurable productivity gains. The signal is distinct from `cognitive-debt-deskilling` (mechanism) and `delegation-gap-paradox` (trust): dependency-trap is the *behavioral lock-in* — cannot or will not work without — that compounds the cognitive-debt mechanism into a workforce-resilience risk.

The most consequential E12 institutional event is [Thoughtworks Radar v34 placing "Codebase cognitive debt" on Trial](https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt) and pairing it with the [Thoughtworks Insights "Harness engineering" prescription](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/harness-engineering-agent-feedback-exploring-ai-coding-sensors). Cognitive debt has now graduated from individual researcher framing (E2: Margaret Storey) through analyst commentary (E6–E10) into Trial-ring named technique with prescription literature — the analyst equivalent of qualified institutional adoption. The longitudinal `cognitive-debt-deskilling` signal (now 4 windows, E2/E5/E6/E12) reaches "institutional formalization" status.

The third E12 macro-shift is **Pricing / Cost rebounding decisively after three windows of retreat**, driven by the [GitHub Copilot June 1 usage-based-billing cutover](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) landing inside the lookback window. [SiliconANGLE's 98% FinOps boardroom datum](https://siliconangle.com/2026/05/28/finops-ai-spending-boardroom-strategy-finopsx/), [Pragmatic Engineer's cost-cutting Pulse](https://newsletter.pragmaticengineer.com/p/the-pulse-a-trend-of-trying-to-cut), [Visual Studio Magazine's $30-$40/session backlash](https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx), and the Amazon Kirorank + Uber budget data points re-energize `cost-runaway` with a *FinOps-formalization* axis it didn't have in E6–E10. Three within-window May incidents (Anthropic May 14 outage, OpenAI May 14 third-party code-security incident, Mini Shai-Hulud npm/PyPI worm May 11–12) add a fourth availability-class exemplar to `agent-production-destruction` and additional SDK-class CVEs ([Flowise CVE-2026-41265 CVSS 9.8](https://carthageelectronics.com/cve-may-2026-zero-day-vulnerabilities/), [Windsurf CVE-2026-30615](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)) advance `mcp-attack-surface` to "production-confirmed plus systemic SDK-class vulnerability."

Sentiment composition cools modestly from E11: Cautiously Negative holds at 43% (flat from E11), Strongly Negative ticks up to 16% (E11: 14%) on the new May-14 dual-incident corpus + Mini Shai-Hulud, Cautiously Positive holds at 12% on the strength of [Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) reading as quietly competent + [Cursor Composer 2.5](https://cursor.com/blog/composer-2-5) launch + Pragmatic Engineer 2026 tooling survey reading as maturation-of-adoption. **Critical composition caveat escalated**: E12 is the *fourth* consecutive window with zero Tier-1 Reddit / Bluesky / Mastodon yield — the structural composition risk has crossed from "significant" to *regime*; every percentage should be read as composition-shifted toward the analyst-publication corpus, and the longitudinal record needs a recovery path for E13 or an explicit retrospective re-weighting acknowledgment.

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
| E12 (5/25–6/1) | **49** | **zero** | yes (5) | yes (32) | **zero (1 promoted Substack)** | **zero** | yes (5) | **zero** | 7 |

**Composition anomalies (E12-specific):**

- **Fourth consecutive zero-Reddit window.** `reddit.com` continues to be blocked at the WebSearch user-agent level. No browser workaround or Grok proxy invoked. No r/ExperiencedDevs, r/cscareerquestions, r/cursor, r/ClaudeCode, r/vibecoding signal for the fourth week running.
- **Fourth consecutive zero-Bluesky / zero-Mastodon window.** The experimental_social tier did register one Substack-promoted Tier-1 item (Willison agent-definition piece), but no native Bluesky/Mastodon retrieval.
- **HN recovers to 5-item yield** from E11's 1-item; HN is now the only practitioner-social Tier-1 source operating at sample-meaningful rate.
- **YouTube recovers to 5-item yield** from E11's zero; channel pages with title/snippet inference, flagged Manual per gap convention.
- **Tier-1 blogs/publications at 32/49 items (65%)** — lower than E11's 98% but still well above the program mean; combined with HN (5) and YouTube (5), the analyst-publication+aggregator share is 42/49 = 86%.

**Composition verdict (full program through E12)**: E1–E3 baselines remain noisier and report direction-only. E4–E10 form the stable mid-window-composition cohort with full social-platform coverage. **E11–E12 are structurally composition-shifted toward the analyst-publication corpus** with no native Reddit / Bluesky / Mastodon. The four-window stretch (E9-rescued, E10-rescued, E11, E12 — only the last two unrescued) confirms the social-platform-Tier-1 retrieval pipeline is structurally failing in the standard automated configuration. **Recommend regime annotation**: pre-E9 and post-E9 should be weighted separately in any sentiment-trend arithmetic across the full program.

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
| E11 | 2% | 12% | 12% | **43%** | 14% | 17% | CN holds near E10/E8 high; SN cools; CP recovers |
| E12 | 2% | 12% | 12% | **43%** | **16%** | 14% | CN flat at structural-risk floor; SN ticks up on new May incidents |

**Composition-adjusted reading**: E12 CN flat (43% → 43%) confirms the program's structural-risk floor at ~42–44% CN once practitioner-social composition is suppressed. The SN bump (14% → 16%) reflects the within-window May-14 dual-incident corpus + Mini Shai-Hulud — three new disclosures landed inside the lookback where E11 had only the Composio retrospective coverage. The CP flat at 12% reflects the Opus 4.7 release + Cursor Composer 2.5 + Pragmatic Engineer survey reading-as-maturation balance — no individual recovery signal but no retreat either. The Strongly Positive 2% holds (Cognition Devin 89% disclosure is the within-window SP datum, replacing E11's HN "innovation of the year" thread as the lone strong-positive). **The structural-risk layer continues intact across all twelve windows; the program is at a stable equilibrium of "Cautiously Negative analyst consensus with periodic incident-driven Strongly Negative spikes."**

---

## Cluster Momentum

Mention counts per cluster, E5 onward where comparable.

| Cluster | E5 | E6 | E7 | E8 | E9 | E10 | E11 | E12 | Trajectory | Signal Strength |
|---------|---:|---:|---:|---:|---:|----:|----:|----:|------------|------------------|
| Code Quality | — | 20 | 20 | 8 | 9 | 16 | 17 | **18** | E12 holds #1; three converging empirical anchors land in-window | Emerging Consensus |
| Architectural Philosophy | — | 17 | 17 | 18 | 17 | 18 | 13 | **16** | Recovers on Thoughtworks v34 Trial + harness engineering | Emerging Consensus |
| Productivity Reality | — | 23 | 23 | 9 | 10 | 11 | 12 | 14 | Continuing climb; paradox is the consensus | Active Debate |
| Trust / Verification | — | 22 | 22 | 17 | 13 | 14 | 13 | 13 | Stable | Active Debate |
| Review Burden | — | — | — | 3 | — | — | **14** | 12 | E11 explosion holds; cognitive-debt absorbs some attention | Emerging Consensus |
| **Pricing / Cost** | — | 14 | 17 | 19 | 13 | 8 | 5 | **11** | **Decisive rebound** via FinOps formalization | Growing Trend |
| Incidents / Failures | — | 9 | 9 | 11 | 10 | 13 | 10 | 11 | Stable-with-tail; four-exemplar agent-blast-radius | Emerging Consensus |
| Burnout / Cognitive Load | — | 4 | 4 | 4 | 4 | 7 | 8 | **11** | Sustained climb; cognitive-debt convergence | Active Debate |
| Deskilling / Learning | — | 2 | 2 | 5 | 7 | 5 | 8 | 10 | Continuing climb; Anthropic 17% + TechCrunch dep-trap | Growing Trend |
| Hiring / Junior Pipeline | — | 4 | 4 | 2 | 1 | 5 | **10** | 9 | E11 doubling consolidates; Anthropic 14% confirms Stanford | Emerging Consensus |
| Hype vs Reality | — | 8 | 8 | 5 | 4 | 5 | 6 | 8 | Modest climb; Yegge IDE-died framing | Active Debate |
| Dependency / Resilience | — | 6 | 6 | 7 | 5 | 4 | 5 | 8 | Climbs on Anthropic outage + Shai-Hulud + GitHub-strain | Growing Trend |
| Tool-Specific Issues | — | — | — | — | — | — | 5 | 7 | NEW prominence carries forward; Composer 2.5 + Devin 89% | Active Debate |
| Enterprise / Policy | — | — | — | 1 | — | 12 | 9 | 7 | Cooling; cost-discipline-as-governance axis dominates | Emerging Consensus |

**Momentum highlights (cumulative through E12):**

- **Fastest rising (E11→E12)**: Pricing / Cost — E11: 5 → E12: 11. The decisive rebound is driven by the [Copilot June 1 cutover](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) landing inside the lookback, [SiliconANGLE 98% FinOps datum](https://siliconangle.com/2026/05/28/finops-ai-spending-boardroom-strategy-finopsx/), [Pragmatic Engineer cost-cutting trend](https://newsletter.pragmaticengineer.com/p/the-pulse-a-trend-of-trying-to-cut), [Visual Studio Magazine pricing backlash](https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx), and the Amazon Kirorank + Uber budget anecdotes from [TechCrunch's dependency-trap piece](https://techcrunch.com/2026/05/29/coders-are-refusing-to-work-without-ai-and-that-could-come-back-to-bite-them/). The cluster's E10 → E11 retreat is now decisively reversed via FinOps formalization.
- **Second-fastest rising (E11→E12)**: Architectural Philosophy — E11: 13 → E12: 16. Recovery driven by [Thoughtworks Radar v34 Codebase cognitive debt](https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt), [Thoughtworks Insights harness engineering](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/harness-engineering-agent-feedback-exploring-ai-coding-sensors), [Storey](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/), and the [HN "Year the IDE Died" thread](https://news.ycombinator.com/item?id=46218922).
- **Third-fastest rising (E11→E12)**: Burnout / Cognitive Load — E11: 8 → E12: 11, on cognitive-debt + review-burden convergence. [O'Reilly Radar's "Burnout and Cognitive Debt"](https://www.oreilly.com/radar/burnout-and-cognitive-debt/) explicitly ties the two clusters together.
- **Modest retreat**: Review Burden — E11: 14 → E12: 12. Not a resolution; cognitive-debt has absorbed some of the analytical attention E11 directed at PR-throughput specifically. The cluster's quantitative spine (Harness 81%/4.6×/2× + Builder.io 60% YoY) is intact and continues to circulate.
- **Continuing climb (3 windows)**: Deskilling / Learning — E10: 5 → E11: 8 → E12: 10. The Anthropic 17% study + Stack Overflow Pulse + TechCrunch dependency-trap convergence is the within-program strongest single climbing-cluster trajectory.
- **Sustained Code Quality #1 (3 windows running at 16–18)**: Veracode 100+ LLM study + arXiv 484k issues + CSA Labs CVE surge constitute three converging large-scale empirical anchors landing in the same week — the question has structurally shifted from "is AI code less secure?" to "how do we instrument at production scale?"
- **Tool-Specific carries forward**: E11's new prominence holds at 7 mentions on Composer 2.5 + Devin 89% + Opus 4.7 + Pragmatic Engineer tooling survey.

---

## Signal Evolution

Signal IDs are quoted directly from input `patterns[].id` slugs per v1.3 summaries mode.

| signal_id | First | Last | Obs | Status | Trajectory | Confidence | Recommended Action |
|-----------|------:|-----:|----:|--------|-----------|-----------|---------------------|
| cve-acceleration | E1 | E12 | **10** | Promoted | ↑ ([Veracode 45%/86%/88%](https://www.infosecurity-magazine.com/news/ai-generated-code-vulnerabilities/) + [arXiv 484k issues](https://arxiv.org/abs/2603.28592) + CSA Labs anchor; three converging large-scale anchors) | H | Continue; cluster matured to "background datum + empirical-spine" status |
| mcp-attack-surface | E1 | E12 | **9** | Promoted | ↑ ([Anthropic MCP RCE class 30+ CVEs](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html) + [Flowise CVE-2026-41265 CVSS 9.8](https://carthageelectronics.com/cve-may-2026-zero-day-vulnerabilities/); production-confirmed + systemic SDK-class) | H | Continue tracking at production-confirmed status |
| agent-production-destruction | E4 | E12 | **8** | Promoted | ↑ ([Anthropic May 14 outage](https://gvwire.com/2026/05/14/claude-ai-goes-down-for-thousands-downdetector-shows/) adds availability-class fourth exemplar; PocketOS retrospective coverage continues) | H | Continue; signal now four-exemplar with two sub-classes |
| anthropic-trust-arc | E4 | E12 | **7** | Promoted | ↑ (May 14 outage adds availability-credibility axis; Opus 4.7 reads quietly competent on capability axis) | H | Continue; multi-axis evaluation |
| ai-burnout-paradox | E3 | E12 | **6** | Promoted | ↑ ([O'Reilly Burnout+Cognitive Debt](https://www.oreilly.com/radar/burnout-and-cognitive-debt/); cognitive-debt convergence) | H | Continue; cognitive-debt becomes parent narrative |
| cognitive-debt-deskilling | E2 | E12 | **5** | Promoted | ↑↑ ([Thoughtworks Radar v34 Trial-ring placement](https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt) — institutional formalization milestone) | H | Continue; INSTITUTIONALLY FORMALIZED this window |
| cost-runaway | E6 | E12 | **5** | Promoted | ↑↑ ([Copilot June 1 cutover](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) + FinOps formalization axis) | H | Continue; signal re-energized with new axis |
| productivity-paradox | E7 | E12 | **4** | Promoted | ↑ ([Pragmatic Engineer 2026 tooling survey](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) is strongest single adoption datum; Cognition Devin 89% adds vendor-named-customer datum) | H | Continue; paradox is the consensus |
| stack-composition | E4 | E12 | **4** | Promoted | ↑ ([Pragmatic Engineer survey](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) crystallizes three-winner equilibrium; Composer 2.5 cost-positioning) | H | Continue tracking |
| vibe-coding-disreputed | E5 | E12 | **3** | Promoted | ↑ ([Builder.io "AI Slop" framing](https://www.builder.io/blog/developers-drowning-in-ai-prs); ThePrimeagen practitioner-video layer) | H | Continue tracking |
| **review-cost-inversion** | E11 | E12 | **2** | Tracking | ↑ ([Builder.io 60% YoY anchor](https://www.builder.io/blog/developers-drowning-in-ai-prs); [CodeAnt](https://www.codeant.ai/blogs/prevent-ai-code-review-overload); [Qodo](https://www.qodo.ai/blog/5-ai-code-review-pattern-predictions-in-2026/)) | H | Promotion threshold reached at 2nd observation — recommend promotion at next consolidation run |
| **junior-pipeline-collapse** | E2 | E12 | **4** | Tracking | ↑ ([Anthropic Labor Market 14%](https://www.anthropic.com/research/labor-market-impacts) confirms Stanford 13–16%; [CIO 40–50% drop](https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html)) | H | **Promotion threshold reached** — recommend promotion at next consolidation run |
| **reset-year-narrative** | E9 | E12 | **3** | Tracking | ↑ ([Thoughtworks Radar v34 Trial](https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt) formalizes the frame as named technique with [harness engineering prescription](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/harness-engineering-agent-feedback-exploring-ai-coding-sensors)) | H | **Promotion threshold reached** — recommend promotion at next consolidation run |
| delegation-gap-paradox | E10 | E12 | **3** | Tracking | ↑ ([Stack Overflow 2025 Dev Survey re-anchor — 84%/46%/3%](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/); [Domain expertise still wanted](https://stackoverflow.blog/2026/03/16/domain-expertise-still-wanted-the-latest-trends-in-ai/)) | H | **Promotion threshold reached** — recommend promotion at next consolidation run |
| agent-infrastructure-inflection | E11 | E12 | **2** | Tracking | ↑↑ ([Cognition Devin 89% disclosure](https://techcrunch.com/2026/05/29/cognitions-scott-wu-says-ai-coding-agents-shouldnt-replace-humans/) is first named-vendor reference at 80%+ autonomy threshold) | H (up from M) | Approaching promotion at E13 if corroborated |
| **ai-dependency-trap** | E12 | E12 | **1** | Tracking | NEW | H | Mint window; promote at E13/E14 if corroborated |
| cursor-xai-acquisition | E6 | E7 | 2 | Tracking | → (no follow-up in E8–E12) | M | **Retire** — narrative has not crystallized in 5 windows |
| vendor-consolidation | E10 | E10 | 1 | Tracking | → (not observed in E11/E12) | H | Tracking-decay — recommend retire if not observed by E13 |
| labor-market-bifurcation | E10 | E10 | 1 | Tracking | → (subsumed by `junior-pipeline-collapse` in E11/E12) | H | **Retire and merge** with `junior-pipeline-collapse` |
| practitioner-skepticism-cluster | E10 | E10 | 1 | Tracking | → (Reddit gap suppresses re-observation; HN partial-rescue insufficient) | M | Defer judgment to post-gap |
| claude-code-automation-platform | E9 | E9 | 1 | Tracking | → (subsumed by `agent-infrastructure-inflection`) | H | **Retire and merge** with `agent-infrastructure-inflection` |
| quality-as-infrastructure | E9 | E9 | 1 | Tracking | → (alive but tagged under `reset-year-narrative`) | H | **Retire and merge** with `reset-year-narrative` |
| enterprise-ai-controls | E6 | E6 | 1 | Tracking | → (not observed in E10–E12) | M | Tracking-decay |
| thoughtworks-radar-formalization | E4 | E4 | 1 | Tracking | → (Radar v34 in E12 is thematic re-emergence under `reset-year-narrative` / `cognitive-debt-deskilling`, not structural follow-up to E4 signal as originally defined) | H | **Retire** — Radar v34 cognitive-debt is captured by other signals |
| oss-maintainer-pushback | E5 | E5 | 1 | Tracking | → (not observed in E6–E12) | M | Tracking-decay |
| senior-deskilling | E6 | E6 | 1 | Tracking | → (subsumed by `cognitive-debt-deskilling` post-E12 formalization) | M | **Retire and merge** with `cognitive-debt-deskilling` |

**NEW signals this window**: `ai-dependency-trap`
**Reached promotion threshold this window**: `review-cost-inversion`, `junior-pipeline-collapse`, `reset-year-narrative`, `delegation-gap-paradox` (4 simultaneous threshold-reaches — largest single-window promotion cohort since E5)
**Approaching promotion (2 obs at H)**: `agent-infrastructure-inflection`
**Recommended retire/merge consolidations at next run**: `labor-market-bifurcation` → merge into `junior-pipeline-collapse`; `claude-code-automation-platform` → merge into `agent-infrastructure-inflection`; `quality-as-infrastructure` + `thoughtworks-radar-formalization` → merge into `reset-year-narrative`; `senior-deskilling` → merge into `cognitive-debt-deskilling`; retire `cursor-xai-acquisition` (5 windows no-follow-up)

---

## Cross-Extraction Contradictions

| Claim | First Position | Current Position | Evolution | Assessment |
|-------|----------------|------------------|-----------|------------|
| "Autonomous coding by Q3 will arrive at vendor-named reference customers" | E11: NEW Contested (Code w/ Claude vendor-side reportage vs analyst review-burden offset) | E12: **Tilting Confirmed** at vendor self-disclosure threshold ([Cognition Devin 89%](https://techcrunch.com/2026/05/29/cognitions-scott-wu-says-ai-coding-agents-shouldnt-replace-humans/) is first named-vendor reference at 80%+ autonomy) | First named-customer corroboration at autonomy threshold | **Tilting Confirmed** (NEW E12) |
| "Junior dev hiring is collapsing under AI pressure" | E10: Contested | E12: **Trending Confirmed** (Stanford 13-16% + Anthropic 14% + CIO 40-50% converge) | Strongest cross-source convergence the corpus has seen | **Trending Confirmed** |
| "MCP attack surface is theoretical / vendor-disputed only" | E1–E9: Trending Negative | E12: **Resolved Negative** ([Anthropic MCP RCE class 30+ CVEs](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html) + [Flowise CVE-2026-41265](https://carthageelectronics.com/cve-may-2026-zero-day-vulnerabilities/) + Composio = production-confirmed + systemic SDK-class) | Resolved at production-confirmed systemic-class | **Resolved Negative** (NEW E12) |
| "AI-generated code is no more vulnerable than human-written code" | E1+: Trending Negative | E12: **Resolved Negative** ([Veracode](https://www.infosecurity-magazine.com/news/ai-generated-code-vulnerabilities/) + [arXiv 484k](https://arxiv.org/abs/2603.28592) + CSA Labs converging anchors) | Three converging large-scale empirical anchors | **Resolved Negative** (NEW E12) |
| "AI-coding cost is a manageable per-seat expense" | E6+: implicit; E11: implicit | E12: **Trending Negative** ([Copilot cutover](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) + [VS Mag $30-$40/session](https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx) + Uber budget exhaustion + [Pragmatic Engineer cost-cutting](https://newsletter.pragmaticengineer.com/p/the-pulse-a-trend-of-trying-to-cut)) | FinOps formalization shifts framing | **Trending Negative** (NEW E12) |
| "Developers can choose to work without AI" | E12: NEW Contested | E12: **Trending Negative** ([TechCrunch refusing-without-AI / METR can't recruit](https://techcrunch.com/2026/05/29/coders-are-refusing-to-work-without-ai-and-that-could-come-back-to-bite-them/); [Anthropic 17% comprehension](https://www.anthropic.com/research/AI-assistance-coding-skills) + behavioral lock-in evidence) | NEW E12; mints the `ai-dependency-trap` signal | **Trending Negative** (NEW E12) |
| "Vibe coding is a distinct, defensible practice" | E1–E5: Contested | E10–E12: Resolved | Stable through 3 windows | **Resolved** (stable) |
| "AI coding productivity gains hold up under longitudinal measurement" | E3–E7: Contested | E12: Contested (paradox stable; Pragmatic Engineer adoption data + Cognition vendor claims vs arXiv 484k + maintenance-cost framing) | Paradox is the consensus | **Contested** (paradox stable) |
| "AI-generated code review can be safely abbreviated at scale" | E11: Trending Negative | E12: Trending Negative (Builder.io 60% YoY + CodeAnt/Qodo prescription literature) | Stable | **Trending Negative** (carried) |

---

## Vocabulary & Framing Drift

| New term (or term in new use) | First appeared | Frequency trend | Significance |
|-------|----------------|------------------|--------------|
| **AI dependency trap** | E12 | First appearance | Names the behavioral lock-in compounding cognitive-debt mechanism into workforce-resilience risk |
| **Codebase cognitive debt (Thoughtworks Radar v34 Trial-ring)** | E12 | First appearance as Radar-named technique | Institutional formalization of the cognitive-debt concept tracked across E2–E11 |
| **Harness engineering (Thoughtworks Insights framing)** | E12 | First appearance | Names feedforward (Agent Skills, spec-driven) + feedback (mutation testing, runtime sensors) controls around coding agents |
| **AI Slop (Builder.io "I didn't become a developer to review AI slop")** | E12 | First appearance | Vivid practitioner framing for AI-PR-volume cost on reviewers |
| **Kirorank (Amazon internal token-leaderboard, shut down after gaming)** | E12 | First appearance | Anecdotal evidence for cost-runaway behavioral-incentive failure |
| **Observed exposure (Anthropic Labor Market Impacts metric)** | E12 | First appearance | Anthropic's capability × actual-usage measure for labor-market analysis |
| **Boardroom FinOps for AI (SiliconANGLE)** | E12 | First appearance | 98% of FinOps teams now manage AI spend; usage-based billing as governance catalyst |
| **Slopsquatting (Veracode framing — ~20% rate of AI-hallucinated package names)** | E12 | First appearance as standalone term | Specific failure mode within `cve-acceleration` |
| **Mini Shai-Hulud (TeamPCP self-propagating supply-chain worm class)** | E12 | First appearance | New incident class name |
| Review-cost inversion | E11 | E11 → E12 stable, mature | Names the workflow-structural cause; now consolidated |
| Decision fatigue (Stack Overflow framing) | E11 | E11 → E12 stable | Mechanism for review-cost-inversion |
| Invisible Burden (SD Times / Harness framing) | E11 | E11 → E12 stable | Harness 2026 survey packaging vocabulary |
| Complacency with AI-generated code (Thoughtworks Hold) | E11 | E11 → E12 stable | Institutional anchor naming rubber-stamping |
| Canaries in the Coal Mine (Stanford) | E11 | E11 → E12 corroborated by Anthropic 14% | Academic anchor; now corroborated within program |
| Sandbox escape via malicious tool registration | E11 | E11 → E12 carried forward | Composio incident class; SDK-class CVE follow-on widens base |
| Capability Curve / Managed Agents / Proactive Workflows / Routines / Dreaming | E11 | E11 → E12 retrospective coverage continues | Anthropic Code w/ Claude feature vocabulary; Q3 verdict pending |
| Vibe Security Radar | E10 | E10 → E12 stable | Anchor reference for CVE-attribution time series |
| Agentic fatigue (ExplainX) | E9 | E9 → E12 stable | Vocabulary winner for burnout-paradox |
| Slopsquatting | E10 | E10 → E12 named technique | Named failure mode within cve-acceleration |

---

## Gaps & Uncertainties

- **Reddit Tier-1 absent for FOUR consecutive windows (E9-rescued, E10-rescued, E11, E12).** Cumulative composition risk has crossed from "significant" to *regime*. Recommend formal engineering intervention (dedicated Reddit-extraction skill modeled on `flipboard-extraction` plus alternative-UA strategies) rather than continued manual rescue.
- **Bluesky / Mastodon Tier-1 zero for four consecutive windows.** Same persistent gap; E12 has one Substack-promoted item but no native Bluesky/Mastodon retrieval.
- **YouTube transcripts and podcasts** — five YouTube items retrieved in E12 with title/snippet inference only; flagged Manual.
- **Cognition Devin 89% disclosure** — vendor self-disclosure only; no third-party customer reference at 80%+ autonomy threshold yet.
- **Anthropic May 14 outage** — single GV Wire / Downdetector aggregate source; Anthropic post-mortem not retrieved in-window. If no public post-mortem materializes the data point degrades from availability-class agent-production-destruction exemplar to dependency-trap anecdote.
- **GitHub Copilot June 1 cutover post-mortem** — pre-cutover backlash captured; E13 is the first empirical test of the FinOps-formalization narrative.
- **METR Feb 2026 productivity-experiment-redesign note** — single secondary source via TechCrunch; recommend manual METR-blog pull for E13.
- **Composio incident second-source corroboration (from E11)** — still pending in E12; the [Anthropic MCP RCE class disclosure](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html) provides systemic complement but is not a peer-vendor sandbox-escape postmortem.
- **Harness 2026 survey primary report (from E11)** — still pending in E12.
- **Q2 2026 BLS / LinkedIn corroboration of Stanford + Anthropic junior-pipeline convergence** — pending.
- **Harness engineering as named technique** — single Thoughtworks Insights source within E12; watch for additional analyst adoption.

---

## Watch List for Next Extraction

1. **GitHub Copilot June 1 cutover post-mortem (highest)** — E13 is the first window after cutover; expect a measurable practitioner-discourse shift confirming or refuting the FinOps-formalization narrative.
2. **Reddit / Bluesky / Mastodon retrieval restoration (highest)** — four zero-yield windows constitute a structural regime; the longitudinal record needs a recovery path or explicit retrospective re-weighting acknowledgment.
3. **Anthropic Claude May 14 outage post-mortem (highest)** — if Anthropic publishes a public post-mortem in E13, it elevates the availability-class exemplar of `agent-production-destruction`; if not, the data point degrades.
4. **Second vendor named-customer 80%+ autonomy disclosure (high)** — would corroborate Code w/ Claude Shopify/Mercado Libre + Cognition Devin claims and advance `agent-infrastructure-inflection` toward "production-confirmed across vendors."
5. **METR primary-source pull (high)** — manual fetch of Feb 2026 productivity-experiment-redesign note for primary methodology.
6. **Q2 2026 BLS / LinkedIn data on junior-pipeline (high)** — corroborate or refute Stanford 13-16% + Anthropic 14% convergence.
7. **Harness engineering as named technique (medium)** — watch for additional analyst adoption beyond Thoughtworks.
8. **AI-load-as-infrastructure-strain (medium)** — Pragmatic Engineer GitHub-breaks framing; watch for GitLab/Bitbucket comparative reliability data.

---

## Longitudinal Report Metadata

| Field | Value |
|-------|-------|
| Longitudinal prompt | v1.3 |
| Domain config | v1.2 |
| Bootloader | v1.9 |
| Report generated | 2026-06-01 15:00 UTC |
| Input mode | summaries (--from-summaries) |
| Extractions covered | E1 through E12 |
| Date range | 2026-03-20 – 2026-06-01 (73 days) |
| Total tagged items | 597 (sum of items_tagged across summaries; includes E10's +20 supplemental pass) |
| Tracked signals | 26 unique signal_ids across the program; 10 Promoted, 11 Tracking (4 reached promotion threshold this window), 5 candidate retire-or-merge |
| NEW signals this window | ai-dependency-trap |
| Escalated signals this window | review-cost-inversion (Tracking → Promotion threshold reached); junior-pipeline-collapse (Tracking → Promotion threshold reached); reset-year-narrative (Tracking → Promotion threshold reached); delegation-gap-paradox (Tracking → Promotion threshold reached); agent-infrastructure-inflection (M → H confidence) |
| Confirmed trends | cve-acceleration (10 obs), mcp-attack-surface (9 obs, production-confirmed systemic-class), agent-production-destruction (8 obs, four-exemplar with two sub-classes), anthropic-trust-arc (7 obs), cognitive-debt-deskilling (5 obs, Thoughtworks Radar Trial-ring formalized) |
| Resolved contradictions | "MCP attack surface is theoretical" (Resolved Negative E12); "AI-generated code is no more vulnerable than human" (Resolved Negative E12); "Vibe coding is a distinct defensible practice" (Resolved against, stable E10-E12) |
| Newly contested claims | "AI-coding cost is manageable per-seat expense" (Trending Negative, NEW E12); "Developers can choose to work without AI" (Trending Negative, NEW E12 — mints ai-dependency-trap) |
