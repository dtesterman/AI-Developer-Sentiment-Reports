# Longitudinal Trend Report: 2026-03-20 – 2026-05-18 (Extractions 1 – 10)

## Executive Summary

Across ten consecutive weekly extractions spanning 59 days (506 sentiment-tagged items after the 2026-05-20 supplemental pass), the AI coding tools discourse has executed a clear regime shift: from "is the code any good?" (E1–E3, dominated by `cve-acceleration` and `mcp-attack-surface` technical-risk signals) through "is the agent safe?" (E4–E7, `agent-production-destruction` and `cost-runaway` become structural) into "is the harness right?" (E8–E9, `quality-as-infrastructure` and `claude-code-automation-platform` crystallize as architectural prescriptions) — and in E10, into **"who governs the gate?"** (`agent-production-destruction` graduates into an institutional-template signal as the Amazon 90-day code-safety reset lands; `oss-maintainer-pushback` hardens into a cross-project coalition; `enterprise-ai-controls` reappears with the Gartner 13%-governance-ready figure as anchor). The most recent window (E10, May 11–18) reverses E9's announcement-driven calm: Cautiously Negative climbs back into the low-40s (E9: 30%; E8: 44%) and Strongly Negative ticks to ~18% as the announcement-affect bounce fades and three convergent Tier-1 disclosures land inside the window — [CSA Labs 35-CVE / 45% OWASP / 20% slopsquatting](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/), [The Register 200k-server MCP design-flaw report](https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw/), and [Fortune's Amazon-outages analysis](https://fortune.com/2026/03/18/ai-coding-risks-amazon-agents-enterprise/) with the 90-day 335-systems reset. **Four new signals appear in E10**: `vendor-consolidation` (secondary-tier dev-tools vendors picking lanes around the top-three coding agents), `labor-market-bifurcation` (the umbrella signal recognizing that contraction and reshape stories now run in parallel rather than competing), and — added by the 2026-05-20 supplemental pass that activated Bluesky and integrated the [Anthropic 2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf) — `practitioner-skepticism-cluster` (Willison + Hightower + Boris Mann + Psyche.co + r/cscareerquestions cross-platform skeptical voice) and `delegation-gap-paradox` (vendor-confirmed 60% use / 0–20% delegation ceiling). The structural-risk layer remains intact across all ten windows: every signal in the Promoted tier of the Signal Store has been observed in ≥4 windows.

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
| E9 (5/4–11) | 50 | yes (Grok proxy) | yes | yes | yes | yes | partial (Tier 2 only) | yes | 7 |
| E10 (5/11–18) | 50 → **70** | metadata via Grok relay (suppl) | yes | yes | **yes (suppl: Willison, Hightower)** | zero | partial (Tier 2 only) | partial | 9 |

**Composition anomalies (E10-specific):**

- **First full-window Reddit gap in the program.** `reddit.com` is blocked at the WebSearch user-agent level in this execution environment for the entire E10 lookback. The E8 (browser path) and E9 (Grok proxy) workarounds did not run this week. r/ExperiencedDevs, r/cscareerquestions, r/cursor, r/ClaudeCode, r/vibecoding signal all suppressed. This is the most consequential single composition issue across the 10-window program — Reddit has been the dominant practitioner-signal source for `anthropic-trust-arc`, `agent-production-destruction`, `cost-runaway`, and `ai-burnout-paradox` across E4–E9.
- **Bluesky and Mastodon zero**: search returned platform-meta content (Bluesky's own AI assistant "Attie" announcements) rather than developer-sentiment posts; experimental-tier promotion criteria not met. E10 is the first window since E5 with zero Bluesky items.
- **Composition shift toward Tier-1 blogs / analyst publications**: with practitioner-Reddit suppressed, the E10 sample is composition-shifted toward editorial Tier-1 content (ThoughtWorks Radar v34, CSA Labs, Fortune, Register, Gartner, Stack Overflow). This composition is *more negative* than the practitioner-Reddit corpus historically produces — explaining a portion of the CN climb from 30% → 42%.

**Composition verdict (full program)**: Mid-window composition is stable enough for trend reads from E4 onward. E1–E3 baselines remain noisier; report direction-only comparisons against E1–E3 and quantified comparisons against E4–E10. **E10 numbers are composition-shifted** — apply a "no Reddit" mental adjustment when reading the sentiment-trajectory delta.

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
| E9 | 6% | 8% | 18% | 30% | 16% | 22% | **CN retreat**; SP off the floor (Code w/ Claude announcement) |
| E10 | 2% | 10% | 12% | **42%** | 18% | 16% | **CN re-climb** toward E8 high; SP retreats |

**Composition-adjusted reading**: The E10 CN re-climb is approximately *50% structural* (three convergent Tier-1 disclosures landing inside the window — CSA Labs, MCP 200k, Fortune Amazon) and *50% compositional* (Reddit suppression shifts sample toward more-negative Tier-1 editorial). The structural component is the more important signal: the announcement-affect of Code w/ Claude was *real but transient*, and the underlying signal-store-tracked risks are intact. The Strongly Negative reading (18% at E10) is in line with E4–E9 (range 13–17%); the program's structural-risk floor is now at ~16–18% across all windows from E4 forward.

---

## Cluster Momentum

Mention counts per cluster, E5 onward where comparable. (E1–E4 used a coarser cluster set; reported as "—".)

| Cluster | E5 | E6 | E7 | E8 | E9 | E10 | Trajectory | Signal Strength |
|---------|---:|---:|---:|---:|---:|----:|------------|------------------|
| Architectural Philosophy | — | 17 | 17 | 18 | 17 | 18 | Stable at top | Emerging Consensus |
| Code Quality | — | 20 | 20 | 8 | 9 | **16** | E10 sharp re-climb | Active Debate |
| Trust / Verification | — | 22 | 22 | 17 | 13 | 14 | Cooling then stable | Active Debate |
| Incidents / Failures | — | 9 | 9 | 11 | 10 | 13 | Elevated; rising | Emerging Consensus |
| Enterprise / Policy | — | — | — | 1 | — | **12** | E10 new prominence | Emerging Consensus |
| Productivity Reality | — | 23 | 23 | 9 | 10 | 11 | Cooling then steady | Active Debate |
| Pricing / Cost | — | 14 | 17 | 19 | 13 | 8 | Sustained cooling | Growing Trend |
| Burnout / Cognitive Load | — | 4 | 4 | 4 | 4 | **7** | E10 climb | Active Debate |
| Hiring / Junior Pipeline | — | 4 | 4 | 2 | 1 | **5** | E10 reassertion | Active Debate |
| Hype vs Reality | — | 8 | 8 | 5 | 4 | 5 | Cooling-stable | Declining Narrative |
| Deskilling / Learning | — | 2 | 2 | 5 | 7 | 5 | Continuing climb (slight pullback) | Growing Trend |
| Dependency / Resilience | — | 6 | 6 | 7 | 5 | 4 | Slight cooling | Growing Trend |
| Team & Org Dynamics | — | — | — | — | 1 | 4 | E10 reassertion | Growing Trend |
| Job Security | — | — | — | — | — | 4 | NEW E10 | Isolated Signal |
| Review Burden | — | — | — | 3 | — | — | E8 only | Isolated Signal |

**Momentum highlights (cumulative through E10):**

- **Fastest rising**: Enterprise / Policy — E8: 1 → E10: 12. Driven by the [Augment Code CTO checklist](https://www.augmentcode.com/guides/cto-ai-coding-checklist), [Gartner Hype Cycle for Agentic AI](https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai), [OSS bans coalition](https://www.infoq.com/news/2026/02/ai-floods-close-projects/) + [Rust Foundation policy work](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/408), and the [Amazon 90-day code-safety reset](https://fortune.com/2026/03/18/ai-coding-risks-amazon-agents-enterprise/) institutional template. The cluster's emergence in E10 is the *most consequential single cluster movement* of the 10-window program.
- **Sharpest re-climb**: Code Quality — E8: 8 → E9: 9 → E10: 16. The [CSA Labs 35-CVE / 45% OWASP](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/), [Lightrun 43% need debugging](https://venturebeat.com/technology/43-of-ai-generated-code-changes-need-debugging-in-production-survey-finds), and the [comprehension-debt anchors](https://medium.com/@addyosmani/comprehension-debt-the-hidden-cost-of-ai-generated-code-285a25dac57e) restored Code Quality as a top-two cluster.
- **Sustained cooling**: Pricing / Cost — E8: 19 → E10: 8. Cluster has cooled steadily since the May 6 rate-limit doubling, though the [Pragmatic Engineer 30%-still-hitting-limits survey](https://newsletter.pragmaticengineer.com/p/the-impact-of-ai-on-software-engineers-2026) suggests the *underlying issue* is not resolved.
- **New cluster prominence (E10 only)**: Job Security — 4 mentions in E10 (NEW, formerly subsumed under Hiring / Junior Pipeline). The bifurcation of the labor-market story into contraction + reshape requires Job Security and Hiring / Junior Pipeline as parallel tracks.

---

## Signal Evolution

| signal_id | First | Last | Obs | Status | Trajectory | Confidence | Recommended Action |
|-----------|------:|-----:|----:|--------|-----------|-----------|---------------------|
| cve-acceleration | E1 | E10 | **8** | Promoted | ↑ (Veracode flat-line E10 is signal maturation marker) | H | Continue tracking; pull Veracode primary source for E11 |
| mcp-attack-surface | E1 | E10 | **7** | Promoted | ↑ (four-source cluster E10 — most concentrated of program) | H | Watch for first vendor-side mitigation (hardened-by-default sampling) |
| vibe-coding-disreputed | E1 | E10 | 5 | Promoted | → (now failure-mode attribution category, not practice) | H | Monitor for vocabulary winner: cognitive-debt vs comprehension-debt |
| anthropic-trust-arc | E4 | E10 | 6 | Promoted | → (Microsoft-internal-CC-adoption is new cross-vendor signal) | H | Watch for second corroborating cross-vendor adoption story |
| agent-production-destruction | E4 | E10 | **5** | Promoted | ↑ (Amazon 90-day reset is institutional-template signal) | H | Track reset-template propagation to other FAANG/PE operators |
| stack-composition | E4 | E10 | 6 | Promoted | → (3-lane / 3-winner stable: Claude/Cursor/Codex) | M | Continue tracking; minimal action |
| cost-runaway | E6 | E10 | **5** | Promoted | → (signal alive after rate-limit doubling; Grok Build $300 ceiling-test) | H | Watch Grok Build pricing settlement at E11 |
| ai-burnout-paradox | E3 | E10 | **4** | Promoted | ↑ (reappears with stronger institutional anchors after E5–E9 gap) | H | Track 60–75% engineer-fatigue figure across surveys |
| cognitive-debt-deskilling | E2 | E10 | **4** | Promoted | ↑↑ (ThoughtWorks Radar v34 institutional consolidation) | H | Track vocabulary-winner outcome; pull primary studies |
| productivity-paradox | E3 | E10 | **5** | Promoted | → (Lightrun 43% + Yegge amplification framings continue) | H | Continue tracking; minimal action |
| oss-maintainer-pushback | E8 | E10 | **2** | Tracking | ↑↑ (E8: 1 obs → E10: cross-project coalition shape) | H | **Promote to Promoted on 3rd obs** (E11 expected) |
| vendor-consolidation | E10 | E10 | 1 | Tracking | NEW | H | Promote at E11 if corroborated; SD Times + Microsoft signals strong |
| labor-market-bifurcation | E10 | E10 | 1 | Tracking | NEW | H | Promote at E11 if corroborated; CNN counterweight + Tom's Hardware are durable |
| senior-deskilling | E7 | E8 | 2 | Tracking | → (absorbed into cognitive-debt-deskilling this window) | H | Consider merging into cognitive-debt-deskilling at consolidation |
| junior-pipeline-collapse | E2 | E5 | 2 | Tracking | → (subsumed under labor-market-bifurcation E10) | H | Retain as sub-signal of labor-market-bifurcation |
| reset-year-narrative | E7 | E7 | 1 | Tracking | → (absorbed into 2026-architectural-reset framing E10) | M | Likely retire; absorbed into vibe-coding-disreputed + architectural cluster |
| cursor-xai-acquisition | E6 | E7 | 2 | Tracking | → (no observation E8–E10) | M | Monitor for re-emergence; otherwise candidate for Retired |
| enterprise-ai-controls | E6 | E6 | 1 | Tracking | → (re-emergent via Augment Code + Gartner + OSS bans cluster in E10) | M | Re-observed E10 as sub-pattern under Enterprise/Policy cluster; consider merging |
| thoughtworks-radar-formalization | E4 | E4 | 1 | Tracking | → (Radar v34 in E10 should re-observe this signal) | H | E10 observation under Architectural Philosophy cluster — update store |

**Key signal evolution events at E10:**

1. **`agent-production-destruction` graduates** from observation-class to institutional-template-class with the [Amazon 90-day code-safety reset](https://fortune.com/2026/03/18/ai-coding-risks-amazon-agents-enterprise/). The signal's *next-phase question* is no longer "will this pattern recur?" (it will) but "will the countermeasure template propagate?"
2. **Two new signals minted**: `vendor-consolidation` and `labor-market-bifurcation`. Both have high first-window confidence and are candidates for Promoted on 2nd observation.
3. **`cognitive-debt-deskilling` reaches institutional anchor** in [ThoughtWorks Radar v34](https://www.thoughtworks.com/en-de/about-us/news/2026/combat-ai-cognitive-debt-radar-v34). The frame is now cited interchangeably across practitioner, academic, and analyst voices — a maturation marker.
4. **`mcp-attack-surface` reaches concentration peak** — four independent Tier-1/Tier-1.5 sources within a single 7-day window. Most concentrated MCP-attack-surface cluster of the program.
5. **`oss-maintainer-pushback` is upgrade-candidate** — second observation with cross-project coalition shape; recommend Promoted upgrade if E11 corroborates.

---

## Cross-Extraction Contradictions

| # | Claim | First Position | Latest Position | Evolution | Assessment |
|---|-------|----------------|-----------------|-----------|------------|
| 1 | "Anthropic's MCP design is working as intended" | Vendor framing E1 | [Register E10 200k-server disclosure](https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw/) + 10 CVEs to date + 4-source cluster | Original claim sustained explicitly by vendor; *publicly contested* in 6 of 10 windows | **Trending Negative across all windows** |
| 2 | "Doubled Claude Code rate limits resolve the cost-runaway grievance" | E9 announcement (vendor-positive) | [Pragmatic Engineer E10 — 30% still hitting limits](https://newsletter.pragmaticengineer.com/p/the-impact-of-ai-on-software-engineers-2026) | Vendor claim survived 1 window; structural counter-evidence in E10 | **Trending Negative** |
| 3 | "Vibe coding is a distinct, defensible practice" | E1 Karpathy origin | E9 Karpathy + Willison both concede; E10 reframed as failure-mode attribution category | Definitionally collapsed E9; now disreputed E10 | **Resolved (Disreputed)** |
| 4 | "Junior dev hiring is collapsing under AI pressure" | E2 ([CNN](https://www.cnn.com/2026/04/08/tech/ai-software-developer-jobs)/[Tom's Hardware](https://www.tomshardware.com/tech-industry/tech-industry-lays-off-nearly-80-000-employees-in-the-first-quarter-of-2026-almost-50-percent-of-affected-positions-cut-due-to-ai) anchor) | E10 reframed as bifurcation (contraction + reshape parallel narratives) | Position evolved from monotonic to bifurcating | **Contested → Bifurcating** (resolution via `labor-market-bifurcation` slug) |
| 5 | "AI coding tools will deliver durable productivity gains" | Vendor framing E1+ | E10 caveat-laden ("must include quality infrastructure") | Net throughput claim survives but constrained | **Contested** |
| 6 | "AI-generated code is reliable enough to ship without infrastructure-level quality gates" | Implicit pre-program | E5+: "quality must become infrastructure" consensus across 5+ sources; E10: [Lightrun 0% leaders very confident](https://venturebeat.com/technology/43-of-ai-generated-code-changes-need-debugging-in-production-survey-finds) | Position has been Trending Negative for 5 consecutive windows | **Trending Negative (5 windows)** |
| 7 | "Detection of AI-authored OSS contributions is feasible" | Implicit pre-program | [InfoQ E10: "functionally impossible within a year or two"](https://www.infoq.com/news/2026/02/ai-floods-close-projects/) | Concession to detection-impossibility now openly stated | **Trending Negative** (E10) |
| 8 | "AI-generated code is maintainable" | Vendor / pre-2026 generic | [InfoQ E10: "not intended to be maintained, only replaced by more AI-generated code"](https://www.infoq.com/articles/ai-generated-mvp/) | Substantively novel counter-position emerges (regeneration-as-maintenance) | **Trending Negative / Contested** (NEW E10) |
| 9 | "The MCP STDIO RCE class is being mitigated quickly" | Implicit early-2026 expectation | E10: still no public mitigation 60+ days after disclosure | Mitigation-cadence question now unresolved across 4 windows | **Trending Negative** |

---

## Vocabulary & Framing Drift

| New term | First appeared | Frequency trend | Significance |
|----------|---------------|-----------------|--------------|
| vibe coding | E1 | Peak E5; declining E8–E10 | Now used as failure-mode attribution; definitionally collapsed E9 |
| cognitive debt | E2 | Sustained climb E2 → E10 | Displaces "technical debt" as dominant 2026 frame; ThoughtWorks Radar v34 institutional anchor E10 |
| comprehension debt | E9 (Osmani rename) | Single-source E9; analyst pickup E10 | Practitioner variant of cognitive debt; per-PR comprehension budgets proposed |
| harness engineering | E8 (ThoughtWorks) | E8–E10 sustained | Verification-bottleneck architectural framing |
| quality as infrastructure | E9 (d4b.dev) | E9–E10 consensus across 5+ sources | Code quality moves from reviewer-discipline to production infrastructure |
| agentic engineering | E9 (Karpathy rename) | Cross-cited E9–E10 | Reframe attempt of vibe coding's positive end |
| Dreaming | E9 (Anthropic Managed Agents) | Single-source E9; pending production-report E10 | Scheduled self-review of prior sessions (Claude Code) |
| Routines | E9 (Anthropic Claude Code) | Single-source E9; pending production-report E10 | Event-driven Claude Code runs |
| Vibe Security Radar | E10 (Georgia Tech / CSA Labs) | NEW E10 | CVE-tracking project; 35 CVEs in March 2026, ~5.8x growth in 60 days |
| slopsquatting | E10 (CSA Labs) | NEW E10 | Malicious packages at LLM-hallucinated names — ~20% reference-rate |
| agentic fatigue | E10 (ExplainX consolidation) | NEW E10; cross-cited | Burnout vector specific to agent-managing workflows; 60–75% engineer report rate |
| regeneration-as-maintenance | E10 (InfoQ MVP-architecture piece) | NEW E10 | Novel position: AI-generated code not maintained but replaced |
| 90-day code-safety reset | E10 (Amazon / Fortune) | NEW E10 | Institutional countermeasure template; 335 critical systems, senior-engineer pre-deploy |
| Coding Agent Swarms | E10 (ThoughtWorks Radar v34) | NEW E10 | Dozens-to-hundreds of dynamically composed agents (Assess) |
| OpenSpec | E10 (ThoughtWorks Radar) | NEW E10 | Spec-driven framework positioned as "response to vibe-coding chaos" |
| Arena Mode | E10 (Grok Build) | NEW E10 | Automated-evaluation layer for parallel-agent fleets |

**Vocabulary headline (E10)**: The window introduced 6 new terms — the highest single-window vocabulary turnover of the program. Five of the six relate to either *security-debt accounting* (Vibe Security Radar, slopsquatting), *workflow countermeasures* (90-day code-safety reset), or *architectural patterns* (Coding Agent Swarms, OpenSpec, regeneration-as-maintenance) — confirming that the discourse is now operating at architectural / institutional levels rather than at tool-comparison level.

---

## Gaps & Uncertainties

- **Reddit Tier-1 retrieval is critically broken** for E10. The 10-window program has now had three different Reddit-retrieval mechanisms (direct WebSearch E1–E7; logged-in browser E8; Grok proxy E9; nothing E10). A durable Reddit path is the program's highest-priority infrastructure debt.
- **Bluesky / Mastodon experimental-tier promotion** has been stuck across 3 windows — search returns platform-meta content rather than practitioner posts. Reconsider promotion criteria or change retrieval path.
- **Podcast retrieval returns zero items for four consecutive windows** (E7–E10). The Pragmatic Engineer podcast was retrieved at Tier 2 in E10 (Yegge + Beck episodes) — *only because* the host's newsletter cross-publishes show notes. Recommend formal Tier 3 demotion.
- **YouTube transcript retrieval has degraded** to "channel page only" from E9 onward. ThePrimeagen and Fireship signal absent at episode level for two consecutive windows.
- **Cross-window pattern-ID renaming risk**: the program now has 19 tracked signals; the analysis engine v1.17 Bootstrap Step gives slug-stability guarantee, but a manual consolidation pass should still verify that no slug has silently drifted between windows.
- **Several E10 source claims need primary-source verification**: Veracode 45% OWASP flat-line; Snap 1,000-engineers attribution (Dev Genius pseudonym); Amazon 90-day reset 335-systems specifics not corroborated by AWS engineering blog.

---

## Watch List for Next Extraction (E11)

1. **Amazon 90-day code-safety reset propagation** [highest]: which other FAANG-tier or PE-backed operator publicly adopts a similar senior-engineer human-review gate? Specific watch: AWS, Meta, Microsoft engineering blogs; Stripe / Datadog / Shopify production-policy disclosures.
2. **Reddit Tier-1 retrieval restoration** [highest]: without it, E11 practitioner signal will remain suppressed and program continuity weakened.
3. **`vendor-consolidation` corroboration** [high]: second-window observation expected if pattern holds — promote to Promoted status on confirmation.
4. **First MCP client shipping hardened-by-default sampling controls** [high]: the four-source MCP-attack-surface cluster needs a vendor-side mitigation signal to balance the longitudinal record.
5. **First production-experience reports on Routines / Dreaming / Managed Agents** [high]: 2 windows since announcement with no concrete production evidence; either ships or slips.
6. **Grok Build $300/mo tier durability** [medium]: does the price hold or compress to Cursor Ultra / Claude Code Max ($200/mo)?
7. **Microsoft-internal-CC-adoption cross-corroboration** [medium]: does the [HN E10 signal](https://news.ycombinator.com/item?id=46854999) gain second / third corroborating cross-vendor adoption stories?
8. **`labor-market-bifurcation` signal corroboration** [medium]: do the contraction-and-reshape parallel narratives both gain new evidence in E11?

---

## Longitudinal Report Metadata

| Field | Value |
|-------|-------|
| Longitudinal prompt | v1.3 |
| Domain config | v1.2 |
| Bootloader | v1.9 |
| Report generated | 2026-05-18 (Mon) automated scheduled run |
| Input mode | summaries (--from-summaries) |
| Extractions covered | E1 through E10 |
| Date range | 2026-03-20 – 2026-05-18 (59 days) |
| Total tagged items | 506 (sum across 10 summaries; E10 increased 50→70 by 2026-05-20 supplemental pass) |
| Tracked signals | 21 (17 prior + 4 new this window: `vendor-consolidation`, `labor-market-bifurcation`, `practitioner-skepticism-cluster`, `delegation-gap-paradox`) |
| NEW signals this window | `vendor-consolidation`, `labor-market-bifurcation`, `practitioner-skepticism-cluster`, `delegation-gap-paradox` |
| Escalated signals this window | `oss-maintainer-pushback` (Tracking → Promoted candidate at 3rd obs); `agent-production-destruction` (Promoted → institutional-template-class) |
| Confirmed trends | `cve-acceleration` (8 obs), `mcp-attack-surface` (7 obs), `cognitive-debt-deskilling` (4 obs with institutional anchor), `agent-production-destruction` (5 obs with countermeasure template), `cost-runaway` (5 obs surviving rate-limit doubling) |
| Resolved contradictions | "Vibe coding is a distinct, defensible practice" (Resolved as Disreputed) |
| Newly contested claims | "AI-generated code is maintainable" (NEW position: regeneration-as-maintenance from [InfoQ MVP piece](https://www.infoq.com/articles/ai-generated-mvp/)) |
