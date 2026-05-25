# Longitudinal Trend Report: 2026-03-20 – 2026-05-25 (Extractions 1 – 11)

## Executive Summary

Across eleven consecutive weekly extractions spanning 66 days (548 sentiment-tagged items including the E10 supplemental pass), the AI coding tools discourse has executed a clear regime shift: from "is the code any good?" (E1–E3, dominated by `cve-acceleration` and `mcp-attack-surface` technical-risk signals) through "is the agent safe?" (E4–E7, `agent-production-destruction` and `cost-runaway` become structural) into "is the harness right?" (E8–E9, `quality-as-infrastructure` and `claude-code-automation-platform` crystallize as architectural prescriptions), into **"who governs the gate?"** at E10 (Amazon 90-day code-safety reset as institutional template), and now in E11 into **"who pays the review cost?"** — `review-cost-inversion` mints this window as a new Tracking signal with the strongest H-confidence first-observation quantitative spine of any new signal in the program (Harness 81% / 4.6× / 2× triple via [SD Times](https://sdtimes.com/softwaredev/the-invisible-burden-how-ai-is-redefining-developer-productivity-in-2026/) + [Stack Overflow decision-fatigue mechanism](https://stackoverflow.blog/2026/05/21/coding-agents-are-giving-everyone-decision-fatigue/) + [Addy Osmani's review-allocation framework](https://addyo.substack.com/p/code-review-in-the-age-of-ai) + [Thoughtworks Complacency Hold ring](https://www.thoughtworks.com/en-us/radar/techniques/complacency-with-ai-generated-code) — four convergent Tier-1 sources within seven days). The second E11 mint is `agent-infrastructure-inflection` (Tracking, M→H confidence), capturing the analyst consensus around Code w/ Claude's five infrastructure features and the Shopify / Mercado Libre 90%-autonomous reference-customer framing — currently second-hand-only and pending Q3 production reports.

The most consequential E11 structural event is the [Composio May 2026 sandbox-escape disclosure](https://composio.dev/blog/composio-may-2026-security-incident) — the first production-confirmed MCP-style sandbox-escape and tool-injection event with public technical disclosure. The longitudinal `mcp-attack-surface` signal (now 8 windows, E1→E11) advances from "vendor-disputed CVE cluster" toward "production-confirmed incident class," pending second-source corroboration in E12. The within-window junior-pipeline story tilts decisively toward the contraction side after the [Stanford "Canaries in the Coal Mine" academic anchor](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/) (13–16% employment decline for 22-to-25-year-olds in AI-exposed roles); `junior-pipeline-collapse` reaches 3 observations (E2, E5, E11) at H confidence and meets the promotion threshold this window.

Sentiment composition is flat-to-slightly-cooling from E10: Cautiously Negative holds in the low 40s (43%, vs E10 42%), Strongly Negative ticks down (14%, vs E10 18%) on no-new-disaster-this-week, Cautiously Positive recovers modestly (12%, vs E10 10%) on the strength of Code w/ Claude follow-on + [Thoughtworks placing Claude Code on Adopt](https://www.thoughtworks.com/radar/tools/claude-code) + the [Anthropic Opus 4.7 release](https://www.anthropic.com/news/claude-opus-4-7) reading as quietly competent. **Critical composition caveat sustained**: E11 is the *third consecutive window* with zero Tier-1 Reddit / Bluesky / Mastodon yield — the structural composition risk is now significant enough to warrant escalation beyond manual fallback queries (recommended action: dedicated Reddit-extraction skill modeled on flipboard-extraction).

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
| E10 (5/11–18) | 50→**70** | metadata via Grok relay (suppl) | yes | yes | yes (suppl) | zero | partial (T2) | partial | 9 |
| E11 (5/18–25) | 42 | **zero** | yes (1) | yes (41) | **zero** | **zero** | zero | partial (1) | 6 |

**Composition anomalies (E11-specific):**

- **Third consecutive zero-Reddit window.** `reddit.com` continues to be blocked at the WebSearch user-agent level for the entire E11 lookback. The E8 browser workaround and the E9 Grok proxy workaround did not run this week. No r/ExperiencedDevs, r/cscareerquestions, r/cursor, r/ClaudeCode, r/vibecoding signal. The supplemental Grok-relay path that augmented E10 was not invoked in E11.
- **Third consecutive zero-Bluesky / zero-Mastodon window.** Same persistent gap — search queries return no usable practitioner posts within the lookback. The E10 supplemental Chrome-browser pass that surfaced [Simon Willison](https://simonwillison.net/2026/May/6/code-w-claude-2026/) and Kelsey Hightower posts directly was not invoked in E11.
- **HN reduced to single-item yield**: only the [Claude Code most-impressive-innovation thread](https://news.ycombinator.com/item?id=46333753) registered as a Tier-1 HN item.
- **Tier-1 blogs/publications dominate the sample at 41/42 items (98%).** The composition risk is now well past the "noise" threshold and into "the analysis-publication corpus *is* the corpus."

**Composition verdict (full program)**: E1–E3 baselines remain noisier and report direction-only against later windows. E4–E10 form the stable mid-window-composition cohort. **E11 is structurally composition-shifted toward the analyst-publication corpus** (Tier-1 blogs 41/42); apply a "no practitioner social signal" mental adjustment when reading the sentiment numbers. The three-window stretch (E9, E10, E11 — though E9 and E10 were partially rescued by supplemental Grok / browser paths) suggests the social-platform-Tier-1 retrieval pipeline is structurally failing in the standard automated configuration and warrants engineering intervention rather than continued manual rescue.

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
| E8 | 0% | 6% | 19% | **44%** | 17% | 15% | CN series high (vendor-trust collapse) |
| E9 | 6% | 8% | 18% | 30% | 16% | 22% | **CN retreat**; SP off floor (CC announcement) |
| E10 | 2% | 10% | 12% | **42%** | 18% | 16% | **CN re-climb** toward E8 high; SP retreats |
| E11 | 2% | 12% | 12% | **43%** | 14% | 17% | CN holds near E10/E8 high; SN cools; CP recovers |

**Composition-adjusted reading**: The E11 CN holds essentially flat from E10 (42% → 43%) — this is consistent with the program's structural-risk floor at ∼42–44% CN once the practitioner-social composition is suppressed. The SN cooling (18% → 14%) is best read as *no-new-disaster-this-week* in a window dominated by analyst pieces digesting prior incidents rather than reporting new ones — the [Composio May 2026 disclosure](https://composio.dev/blog/composio-may-2026-security-incident) is the lone new incident and reads as Significant (single-source, sandbox-escape class) rather than Critical. The CP modest recovery (10% → 12%) reflects the Code w/ Claude follow-on coverage + Opus 4.7 release + Thoughtworks Adopt; this is the first window in three where Anthropic-specific items register net-positive. The Strongly Positive 2% is unchanged — the program's SP floor remains hard at 0–2% across E4–E11. **The structural-risk layer continues intact across all eleven windows.**

---

## Cluster Momentum

Mention counts per cluster, E5 onward where comparable. (E1–E4 used a coarser cluster set; reported as "—".)

| Cluster | E5 | E6 | E7 | E8 | E9 | E10 | E11 | Trajectory | Signal Strength |
|---------|---:|---:|---:|---:|---:|----:|----:|------------|------------------|
| Architectural Philosophy | — | 17 | 17 | 18 | 17 | 18 | 13 | First retreat from sustained top | Emerging Consensus |
| Code Quality | — | 20 | 20 | 8 | 9 | 16 | **17** | E11 holds #1 (E10 re-climb consolidated) | Active Debate |
| Trust / Verification | — | 22 | 22 | 17 | 13 | 14 | 13 | Cooling-stable | Active Debate |
| Incidents / Failures | — | 9 | 9 | 11 | 10 | 13 | 10 | Elevated; retreating | Emerging Consensus |
| Enterprise / Policy | — | — | — | 1 | — | 12 | 9 | Stable post-E10 emergence | Emerging Consensus |
| Productivity Reality | — | 23 | 23 | 9 | 10 | 11 | 12 | Cooling-stable; slight climb | Active Debate |
| Pricing / Cost | — | 14 | 17 | 19 | 13 | 8 | 5 | Sustained cooling | Growing Trend |
| Burnout / Cognitive Load | — | 4 | 4 | 4 | 4 | 7 | 8 | Sustained climb | Active Debate |
| Hiring / Junior Pipeline | — | 4 | 4 | 2 | 1 | 5 | **10** | E11 doubles — academic-anchor consolidation | Emerging Consensus |
| Hype vs Reality | — | 8 | 8 | 5 | 4 | 5 | 6 | Cooling-stable | Declining Narrative |
| Deskilling / Learning | — | 2 | 2 | 5 | 7 | 5 | 8 | Continuing climb | Growing Trend |
| Dependency / Resilience | — | 6 | 6 | 7 | 5 | 4 | 5 | Stable | Growing Trend |
| Team & Org Dynamics | — | — | — | — | 1 | 4 | — | E11 absent (subsumed in Review Burden) | Isolated Signal |
| Job Security | — | — | — | — | — | 4 | — | E11 subsumed in Hiring | Isolated Signal |
| **Review Burden** | — | — | — | 3 | — | — | **14** | **E11 explosion** — newly named cluster | Emerging Consensus |
| Tool-Specific Issues | — | — | — | — | — | — | 5 | NEW E11 prominence | Isolated Signal |

**Momentum highlights (cumulative through E11):**

- **Fastest rising (E10→E11)**: Review Burden — E8: 3 → E10: implicit → E11: 14. The cluster's E11 explosion is the *single most consequential cluster movement of E11*. Drivers: [Stack Overflow decision-fatigue piece](https://stackoverflow.blog/2026/05/21/coding-agents-are-giving-everyone-decision-fatigue/), [SD Times Harness-survey "Invisible Burden"](https://sdtimes.com/softwaredev/the-invisible-burden-how-ai-is-redefining-developer-productivity-in-2026/) (81% / 4.6× / 2× quantitative anchor), [Addy Osmani Code Review framework](https://addyo.substack.com/p/code-review-in-the-age-of-ai), and [Thoughtworks Complacency Hold ring](https://www.thoughtworks.com/en-us/radar/techniques/complacency-with-ai-generated-code). The cluster has graduated from "isolated E8 mention" to "newly named cluster with quantitative spine and institutional anchor" within one window.
- **Second-fastest rising (E10→E11)**: Hiring / Junior Pipeline — E10: 5 → E11: 10. The doubling reflects the [Stanford Canaries](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/) academic anchor + [Anthropic 17% skill-mastery](https://www.infoq.com/news/2026/02/ai-coding-skill-formation/) vendor anchor + IEEE / CIO / Futurist / Science-Tech News echo cluster.
- **First retreat from sustained top**: Architectural Philosophy — E10: 18 → E11: 13. The "2026 reset toward architecture" frame holds but competes for analyst attention with the review-burden frame. This is the first window in 7 that the cluster is not in #1 position.
- **Sustained cooling holds**: Pricing / Cost — E8: 19 → E11: 5. Cluster has continued retreating; vendor pricing-tier rebalancing watch is the E12+ trigger to re-test.
- **Confirmed signal-store-tracked cluster continues**: Code Quality holds #1 at 17 mentions, anchored on the [CSA Labs 35-CVE March figure](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/) which is now the most-cited single quantitative datum in the corpus (propagated across Dark Reading, Techzine, Augment, Salesforce Ben).
- **Team & Org Dynamics + Job Security**: both clusters subsumed under more-specific E11 frames (Review Burden absorbs the team-dynamics work; Hiring / Junior Pipeline absorbs job-security on the cohort-specific contraction story).

---

## Signal Evolution

Signal IDs are quoted directly from input `patterns[].id` slugs per v1.3 summaries mode (unambiguous cross-window tracking).

| signal_id | First | Last | Obs | Status | Trajectory | Confidence | Recommended Action |
|-----------|------:|-----:|----:|--------|-----------|-----------|---------------------|
| cve-acceleration | E1 | E11 | **9** | Promoted | ↑ (CSA Labs anchor now most-cited corpus datum; Sonar 2026 survey corroborates) | H | Continue tracking; cluster has matured to "background datum" status |
| mcp-attack-surface | E1 | E11 | **8** | Promoted | ↑↑ (**Composio production-confirmed graduation pending second-source**) | H | Watch E12 for second-source corroboration; Red Hat skills-as-alternative positioning is institutional vendor response |
| agent-production-destruction | E4 | E11 | **7** | Promoted | ↑ (Composio adds third confirmed exemplar; three vendor/customer contexts) | H | Continue tracking; cluster has matured to "named incident class" |
| anthropic-trust-arc | E4 | E9 | 6 | Promoted | → (not observed in E10/E11; Opus 4.7 read as quiet capability iteration) | H | Watch E12 for re-observation; absence reflects post-keynote settling, not arc resolution |
| stack-composition | E4 | E9 | 6 | Promoted | → (not observed in E10/E11; subsumed by `agent-infrastructure-inflection` in E11) | M | Recommend retire-and-rename merge with `agent-infrastructure-inflection` after E13 if pattern holds |
| ai-burnout-paradox | E3 | E11 | **6** | Promoted | ↑ (E11 re-observation via Stack Overflow / SD Times mechanism; HBR Brain Fry + Axios still anchor) | H | Continue tracking; pattern is now structural feature of agentic-workflow rather than power-user-specific |
| vibe-coding-disreputed | E1 | E10 | 6 | Promoted | → (not observed in E11 as standalone; subsumed under `reset-year-narrative` framing) | H | Recommend retire after one more absent window; framing has consolidated |
| cost-runaway | E6 | E10 | 5 | Promoted | → (cluster mention count at series-low 5 in E11; signal alive but quiet) | H | Watch E12 Cursor / Claude Code / Codex pricing-tier rebalancing as re-test |
| productivity-paradox | E3 | E7 | 4 | Promoted | ↑ (not observed as standalone in E8–E11; consolidated into review-cost-inversion + delegation-gap-paradox via Harness survey) | H | Recommend retire-and-rename to consolidate with `review-cost-inversion` after E12 if pattern holds |
| cognitive-debt-deskilling | E2 | E10 | 4 | Promoted | → (not observed in E11 standalone; Cognitive World + Addy Osmani anchors still active) | H | Continue tracking; cluster has matured to "background datum" |
| **junior-pipeline-collapse** | E2 | E11 | **3** | Tracking | ↑↑ (**Promotion threshold reached**; Stanford academic anchor + Anthropic 17% study + IEEE/CIO/Futurist/STN echo) | H | **Promote to Promoted at next consolidation pass** |
| **reset-year-narrative** | E7 | E11 | **2** | Tracking | ↑ (Thoughtworks Complacency Hold + ITBrief reset framing + d4b.dev × 2 + Salesforce Ben) | H | One more observation to reach promotion threshold |
| oss-maintainer-pushback | E8 | E10 | 2 | Tracking | → (not observed in E11; OSS-governance cluster present but no dedicated coalition piece this window) | H | Continue tracking; needs E12 observation to reach promotion |
| senior-deskilling | E7 | E8 | 2 | Tracking | → (not observed in E9–E11) | H | Recommend tracking-decay if not observed by E13 |
| cursor-xai-acquisition | E6 | E7 | 2 | Tracking | → (no follow-up in E8–E11) | M | Recommend retire if not observed by E12 — narrative has not crystallized |
| delegation-gap-paradox | E10 | E11 | 2 | Tracking | ↑ ([Stack Overflow trust gap pieces](https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/) anchor stays cited; Sonar 2026 survey corroborates) | H | One more observation to reach promotion threshold |
| vendor-consolidation | E10 | E10 | 1 | Tracking | → (not observed in E11) | H | Continue tracking; needs E12+ observation |
| labor-market-bifurcation | E10 | E10 | 1 | Tracking | → (subsumed by `junior-pipeline-collapse` in E11 — contraction-side tilt resolves the bifurcation toward one signal) | H | Recommend retire-and-merge with `junior-pipeline-collapse` after E12 if pattern holds |
| practitioner-skepticism-cluster | E10 | E10 | 1 | Tracking | → (not observed in E11 — Reddit/Bluesky gap suppresses likely re-observation) | M | Cannot evaluate while social-platform retrieval is broken; defer judgment to post-gap E12+ |
| claude-code-automation-platform | E9 | E9 | 1 | Tracking | → (subsumed by `agent-infrastructure-inflection` in E11) | H | Recommend retire-and-merge with `agent-infrastructure-inflection` after E13 |
| quality-as-infrastructure | E9 | E9 | 1 | Tracking | → (still alive via d4b.dev pieces in E11 but tagged under `reset-year-narrative` framing) | H | Recommend retire-and-merge with `reset-year-narrative` after E12 |
| enterprise-ai-controls | E6 | E6 | 1 | Tracking | → (not observed in E10/E11) | M | Recommend tracking-decay if not observed by E13 |
| thoughtworks-radar-formalization | E4 | E4 | 1 | Tracking | → (not observed since E4) | H | Recommend retire — Radar v34 in E10 was thematic, not structural follow-up |
| **review-cost-inversion** | E11 | E11 | 1 | Tracking | NEW | H | Promote at E12 if corroborated; Harness 81%/4.6×/2× anchor + Stack Overflow + Osmani + Thoughtworks Hold is the strongest H-confidence first-observation in the program |
| **agent-infrastructure-inflection** | E11 | E11 | 1 | Tracking | NEW | M | Promote at E13 if corroborated; pending Q3 production reports on Code w/ Claude features and Shopify/Mercado Libre 90%-autonomous customers |

**NEW signals this window**: `review-cost-inversion`, `agent-infrastructure-inflection`
**Reached promotion threshold**: `junior-pipeline-collapse` (3 obs at H)
**Approaching promotion (2 obs at H)**: `reset-year-narrative`, `delegation-gap-paradox`
**Recommended retire/merge consolidations**: `productivity-paradox` → merge into `review-cost-inversion`; `stack-composition` + `claude-code-automation-platform` → merge into `agent-infrastructure-inflection`; `quality-as-infrastructure` → merge into `reset-year-narrative`; `labor-market-bifurcation` → merge into `junior-pipeline-collapse`; `vibe-coding-disreputed` → retire (framing consolidated); `cursor-xai-acquisition` and `thoughtworks-radar-formalization` → retire (no follow-up)

---

## Cross-Extraction Contradictions

| Claim | First Position | Current Position | Evolution | Assessment |
|-------|----------------|------------------|-----------|------------|
| "Junior dev hiring is collapsing under AI pressure" | E10: Contested (Tom's Hardware vs CNN counterweight) | E11: Trending Confirmed (Stanford academic anchor + Anthropic 17% vendor anchor outweigh CNN minority position) | Tilted toward contraction side with strongest academic + vendor empirical pairing | **Trending Confirmed** |
| "MCP attack surface is theoretical / vendor-disputed only" | E1–E9: Trending Negative (CVE cluster, vendor-disputed "works as expected") | E11: Trending Negative; production-confirmed Composio incident graduates the signal | Composio = first production-confirmed sandbox-escape with technical disclosure | **Trending Negative** |
| "Vibe coding is a distinct, defensible practice" | E1–E5: Contested | E10–E11: Resolved (failure-mode-attribution category, not practice) | Stable through 2 windows | **Resolved** |
| "AI coding productivity gains hold up under longitudinal measurement" | E3–E7: Contested | E11: Contested (productivity-paradox consolidates; Harness review-cost data is strongest contradicting datum yet) | Paradox is now analyst consensus; the question shifts from "gain or no gain?" to "what cost?" | **Contested** (paradox stable) |
| "AI-generated code review can be safely abbreviated at scale" | E8: tentatively raised | E11: Trending Negative (Thoughtworks Complacency Hold + Harness 4.6× / 2× quantification + Osmani prescription) | First window where the claim is directly and institutionally refuted | **Trending Negative** (NEW E11) |
| "Autonomous coding by Q3 will arrive as advertised at Anthropic-named reference customers (Shopify, Mercado Libre at 90%)" | E11: NEW Contested (vendor-side reportage vs analyst-side review-burden offset) | E11: Contested — pending Q3 production data | NEW E11 contradiction; resolution depends on Q3 customer testimonials | **Contested** (NEW E11; resolution Q3) |
| "Doubled Claude Code rate limits resolve the cost-runaway grievance" | E10: Trending Negative | E11: Not raised in-window | Insufficient new data in E11; cluster cooling may resolve via attrition rather than confirmation | **Trending Negative** (carried) |
| "Anthropic's MCP design is working as intended; no protocol-level patch needed" | E5+: Trending Negative | E11: Trending Negative (Composio incident is the strongest single contradicting datum) | Position increasingly untenable | **Trending Negative** |
| "Detection of AI-authored OSS contributions is feasible" | E8: Trending Negative | E11: Not raised in-window | Status quo holds; no new data | **Trending Negative** (carried) |
| "AI-generated code is maintainable" | E10: Trending Negative | E11: Not raised explicitly in-window | Reset-year-narrative captures the same thesis differently | **Trending Negative** (carried; absorbed into reset-narrative) |

---

## Vocabulary & Framing Drift

| New term (or term in new use) | First appeared | Frequency trend | Significance |
|-------|----------------|------------------|--------------|
| Review-cost inversion | E11 | First appearance | Names the workflow-structural cause of which "burnout" is the affective consequence; quantified by Harness 4.6× / 2× |
| Decision fatigue (Stack Overflow framing) | E11 | First appearance | Mechanism for review-cost-inversion: constant trust/override micro-decisions as exhaustion vector |
| Invisible Burden (SD Times / Harness framing) | E11 | First appearance | The packaging vocabulary for the Harness 2026 survey results; likely to recur as the data propagates |
| Complacency with AI-generated code (Thoughtworks Hold ring name) | E11 | First appearance | Institutional-credibility anchor naming rubber-stamping as the defect |
| Capability Curve / Managed Agents / Proactive Workflows / Routines / Dreaming | E11 | First appearance | Anthropic Code w/ Claude feature vocabulary; will recur as Q3 production reports either confirm or refute |
| Canaries in the Coal Mine (Stanford framing) | E11 | First appearance | Academic-credibility anchor for junior-pipeline-collapse |
| Sandbox escape via malicious tool registration | E11 | First appearance | Names the Composio incident class; will recur if a second MCP-platform vendor publishes corroborating disclosure |
| Vibe Security Radar (Georgia Tech / CSA Labs) | E10 | E10 → E11 stable | Most-cited single CVE-tracking project anchor across the corpus |
| 90-day code-safety reset (Amazon institutional countermeasure) | E10 | E10 → E11 carried | Institutional template; watch for second-FAANG adoption |
| Agentic fatigue (ExplainX consolidation) | E9 | E9 → E10 → E11 stable | The vocabulary winner for the burnout-paradox framing |
| OpenSpec (spec-driven response to vibe-coding chaos) | E10 | E10 → E11 stable | Vocabulary winner of the "post-vibe-coding" reset framing |
| Slopsquatting (LLM-hallucinated package supply chain attack) | E10 | E10 → E11 stable | Names a specific failure mode within `cve-acceleration` |

---

## Gaps & Uncertainties

- **Reddit Tier-1 absent for three consecutive windows (E9, E10, E11).** Cumulative composition risk is now significant — practitioner-Reddit signal that historically drove much of the Mixed and Cautiously Positive vote share has been suppressed. Recommend escalation: dedicated Reddit-extraction skill modeled on `flipboard-extraction` plus alternative-UA strategies.
- **Bluesky / Mastodon Tier-1 zero for three consecutive windows.** Same persistent gap. The E10 supplemental Chrome-browser pass that surfaced Willison/Hightower posts was not invoked in E11.
- **YouTube transcripts and podcasts — zero automated yield.** Channel pages only; episode transcripts require manual browser session.
- **Composio incident single-source.** Production-confirmed graduation of `mcp-attack-surface` is contingent on second-source corroboration from a major MCP-platform vendor in E12.
- **Code w/ Claude 90%-autonomous customers second-hand only.** Shopify and Mercado Libre at 90% autonomous are cited via conference reportage; no primary-source customer testimonial captured. The `agent-infrastructure-inflection` signal's H-confidence graduation depends on Q3 production reports.
- **Harness 2026 survey single-source quantitative anchor.** The 81% / 4.6× / 2× triple is surfaced via SD Times reportage only; primary report pull recommended for E12.
- **Stanford "Canaries" 2025-snapshot artifact risk.** Q2 2026 BLS / LinkedIn corroboration watch.
- **Pricing / Cost cluster series-low (5 mentions in E11).** Cluster may be entering a quiet phase rather than resolving; watch for E12 Cursor / Claude Code / Codex pricing-tier rebalancing.
- **Anthropic Opus 4.7 release reading.** [Anthropic's Opus 4.7 announcement](https://www.anthropic.com/news/claude-opus-4-7) is read in this corpus as a *quietly competent capability iteration* — but no SmartScope-style postmortem has yet surfaced to confirm or refute the quality reading. Watch E12–E13.

---

## Watch List for Next Extraction

1. **Composio second-source corroboration (highest)** — does Anthropic, Cloudflare, JFrog, or Red Hat publish a corroborating MCP-style sandbox-escape disclosure in E12 to clean-graduate `mcp-attack-surface`?
2. **Reddit / Bluesky / Mastodon retrieval restoration (highest)** — three zero-yield windows constitutes structural composition risk; without restoration, E12+ practitioner signal continues suppressed.
3. **Q3 production reports on Code w/ Claude infrastructure features (high)** — Managed Agents, Proactive Workflows, Capability Curve, Routines, Dreaming. Does the platform-bet ship or quietly slip?
4. **Primary-source customer testimonials from Shopify / Mercado Libre at 90% autonomous (high)** — currently second-hand only via conference reportage.
5. **Harness 2026 survey primary report pull (high)** — verify the 81% / 4.6× / 2× triple and extract additional review-burden quantification beyond SD Times reportage.
6. **Q2 2026 BLS / LinkedIn data on 22-25yo employment decline (medium)** — corroborate or refute Stanford Canaries finding; resolves whether `junior-pipeline-collapse` graduation is empirically robust or 2025-snapshot artifact.
7. **`review-cost-inversion` second-source corroboration (medium)** — does the 4.6× / 2× quantification reproduce in a second independent survey, or does the Harness 2026 survey end up the sole quantitative spine?
8. **Pricing / Cost cluster re-emergence (medium)** — Cursor / Claude Code / Codex pricing-tier rebalancing in E12 is the natural re-test trigger.

---

## Longitudinal Report Metadata

| Field | Value |
|-------|-------|
| Longitudinal prompt | v1.3 |
| Domain config | v1.2 |
| Bootloader | v1.9 |
| Report generated | 2026-05-25 16:30 UTC |
| Input mode | summaries (--from-summaries) |
| Extractions covered | E1 through E11 |
| Date range | 2026-03-20 – 2026-05-25 (66 days) |
| Total tagged items | 548 (sum of items_tagged across summaries; includes E10's +20 supplemental pass) |
| Tracked signals | 25 unique signal_ids across the program; 10 Promoted, 12 Tracking, 3 candidate retire-or-merge |
| NEW signals this window | review-cost-inversion, agent-infrastructure-inflection |
| Escalated signals this window | junior-pipeline-collapse (Tracking → Promoted threshold reached); reset-year-narrative and delegation-gap-paradox approaching promotion |
| Confirmed trends | cve-acceleration (9 obs), mcp-attack-surface (8 obs, graduating to production-confirmed pending E12), agent-production-destruction (7 obs, named incident class), ai-burnout-paradox (6 obs), anthropic-trust-arc (6 obs) |
| Resolved contradictions | "Vibe coding is a distinct defensible practice" (Resolved against, stable through E10–E11) |
| Newly contested claims | "Autonomous coding by Q3 will arrive at named reference customers" (Code w/ Claude vendor reportage vs review-burden offset); "AI-generated code review can be safely abbreviated at scale" (Trending Negative, NEW E11) |
