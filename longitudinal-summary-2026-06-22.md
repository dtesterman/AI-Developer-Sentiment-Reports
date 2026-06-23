# Longitudinal Trend Report: 2026-03-20 – 2026-06-22 (Extractions 1 – 15)

## Executive Summary

Across fifteen consecutive weekly extractions spanning 94 days (~727 sentiment-tagged items), the AI coding tools discourse has executed a clear regime-shift sequence: "is the code any good?" (E1–E3) → "is the agent safe?" (E4–E7) → "is the harness right?" (E8–E9) → "who governs the gate?" (E10) → "who pays the review cost?" (E11) → "who pays the cognitive cost?" (E12) → "is the infrastructure load-bearing AND who pays?" (E13) → "who do we trust, and what is the supply-chain cost?" (E14) → and now in **E15 to "the MCP supply chain IS the incident class — and BYOK is the economic counter-move"** — a week in which the AgentJacking disclosure adds a fresh MCP exploit class on top of an already-saturated incident surface, and VS Code's BYOK release reframes the pricing-and-trust frontier.

E15 mints two new signals — `ide-paradigm-shift` and `byok-pricing-shift` — and re-confirms five tracked signals at high observation density. `mcp-attack-surface` reaches **9 observations** with [The New Stack's AgentJacking disclosure (2026-06-21)](https://thenewstack.io/agentjacking-sentry-mcp-attack/) joining [OX Security's systemic MCP RCE](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/), [Check Point's CVE-2025-59536 + CVE-2026-21852 RCE/token-exfiltration disclosure](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/), and the [coordinated malicious JetBrains plugin campaign](https://blog.cyberdesserts.com/ai-agent-security-risks/) in the same window. Five Critical/Significant incidents land in E15 — the highest count of any extraction since E11.

The most consequential E15 macro-shift is **`byok-pricing-shift` minting against `cost-runaway`'s 10-window arc**. [VS Code's 2026-06-18 BYOK release](https://code.visualstudio.com/blogs/2026/06/18/byok-vscode) lets developers plug Anthropic/OpenAI/Gemini/Ollama keys directly into the native chat picker without a Copilot subscription — the first hyperscaler-scale move to eliminate seat-cost lock-in. [Databricks Agent Bricks at DAIS 2026](https://www.databricks.com/blog/agent-bricks-dais-2026) makes MCP a first-class Unity Catalog citizen with cross-system permission bridging — the deterministic counter-design to AgentJacking. [Cursor's repackaged Teams pricing](https://cursor.com/blog/teams-pricing-june-2026) and [Pragmatic Engineer's "Pulse" framing of eng-department FinOps cuts](https://newsletter.pragmaticengineer.com/p/the-pulse-a-trend-of-trying-to-cut) — naming Microsoft Claude-Code license cancellations and Uber's April budget exhaustion — complete the structural reframe. The E14 cost-runaway story was "the bill is too high"; the E15 story is "the architecture changes to dodge the bill".

`cognitive-debt-deskilling` graduates from blog idea to industry-tracked concept this window. [ThoughtWorks Radar's Codebase Cognitive Debt entry](https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt), [LeadDev's "AI coding creates two kinds of debt"](https://leaddev.com/ai/ai-coding-creates-two-kinds-of-debt-youre-only-measuring-one), and the [r/ClaudeAI "Are you using Claude as much as 2-3 months ago?" usage-deflation thread](https://www.reddit.com/r/ClaudeAI/comments/1u8reiu/are_you_guys_using_claude_as_much_as_you_were_23/) surface the same arc from analyst, practitioner-press, and end-user angles. Anthropic's own controlled study (referenced via the LeadDev piece) reports 17% lower comprehension scores for AI-assisted juniors; the r/ClaudeAI thread reports 80–90% of what was built isn't used.

`ide-paradigm-shift` is the second new mint — Theo t3.gg's [2026 Is The Year IDEs Die](https://www.youtube.com/watch?v=XYYZM01P2S0) and [The Rise of Agent Experience (AX)](https://www.youtube.com/watch?v=EXeCOsIu0Ps), [ThoughtWorks Radar's Coding agent swarms](https://www.thoughtworks.com/radar/techniques/coding-agent-swarms) and [Team of coding agents](https://www.thoughtworks.com/radar/techniques/team-of-coding-agents), and the [r/ClaudeCode senior-practitioner framing](https://www.reddit.com/r/ClaudeCode/comments/1u68q4y/how_i_actually_use_claude_code_as_a_senior/) ("stop using one agent for everything") all sit on the same architectural arc. After multi-window foreshadowing in `stack-composition` and `claude-code-automation-platform`, the IDE-replacement narrative is now Radar-and-creator consensus.

`delegation-gap-paradox` continues — [Stack Overflow's trust-gap data](https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/) (84% use, 29% trust accuracy, 3% "highly trust"), [Pragmatic Engineer's "AI Tooling for SWEs 2026" report](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) (95% weekly use, 56% doing 70%+ of work with AI) — but the in-window Reddit corpus reframes the gap as bimodal-by-experience-level rather than uniform. Senior practitioners constrain rather than reject.

Sentiment composition shifts toward the center: **SN 22% (↓6 from E14's 28%)** despite the highest incident-count week since E11 — the discourse has consolidated the MCP story into a single recurring storyline rather than discovering it fresh each week; **CN 28% (↓2)**; MA rises to 22% (↑5) on the Cursor acquisition concern, the Reddit usage-deflation polarization, and Pragmatic Engineer's bimodal-by-experience data; CP rises to 14% (↑4) on X/Twitter productivity boosts and BYOK-as-enabler framing; SP holds at 3%; Nu retreats to 11%. The structural ~50% SN+CN floor (E6–E15) remains the durable signal of the program's settled state.

**Critical composition note**: E15 retrieval continues E14's pattern — Reddit URLs sourced via ChatGPT browsing (8 verified URLs from r/cursor, r/ClaudeAI, r/ClaudeCode, r/vibecoding, r/cscareerquestions); YouTube + incidents via Gemini grounding (two Theo t3.gg URLs flagged for manual click-through verification); X/Twitter via Grok native firehose (10 items). **Bluesky/Mastodon zero-yield persists** — a six-window regime hardening into a structural gap rather than a transient blockage.

**Highest-priority next-window watch**: confirmation/refutation of the Cursor acquisition narrative; first production case study of VS Code BYOK at enterprise scale; GLM-5.2 + open-weights coding-model adoption (graduates `vendor-model-independence`?); manual click-through verification of Theo t3.gg June 2026 video uploads; Bluesky/Mastodon direct app navigation via Claude in Chrome.

---

## Source Composition Audit

| Extraction | Window end | Items | Reddit | Bluesky/Mastodon | X (firehose) | Blogs | YouTube | HN | Incidents |
|---|---|---|---|---|---|---|---|---|---|
| E1 – E9 | 2026-03 – 2026-05 | ~480 cum | mixed | irregular | irregular | strong | weak | weak | irregular |
| E10 | 2026-05-11 | 47 | 0 | 9 | 8 | 21 | 1 | 1 | 4 |
| E11 | 2026-05-18 | 52 | 0 | 14 | 6 | 22 | 2 | 1 | 4 |
| E12 | 2026-06-01 | 49 | 0 | 11 | 7 | 23 | 2 | 2 | 3 |
| E13 | 2026-06-08 | 46 | 0 | 12 | 5 | 21 | 2 | 1 | 3 |
| E14 | 2026-06-15 | 54 | 10 (Grok) | 6 | 8 | 21 | 2 | 1 | 5 |
| E15 | 2026-06-22 | 39 | 8 (ChatGPT) | 0 | 10 (Grok) | 15 | 4 (Gemini) | 2 | 5 |

**Composition anomalies**: E15 item-count drops 28% vs E14 (54 → 39). Two causes: Bluesky/Mastodon zero-yield persists into a sixth consecutive window; the blog/publication tier is leaner this week (15 vs E14's 21) because much of the discourse is concentrated in a small number of high-density artifacts (Pragmatic Engineer Pulse, ThoughtWorks Radar 3 entries, OX Security disclosure, AgentJacking The New Stack piece) rather than spread across many independent voices. Sentiment readings remain valid; volume-trend comparisons should be discounted.

**Composition verdict**: usable; Bluesky/Mastodon recurrent gap requires structural workaround (Claude-in-Chrome direct-handle navigation not yet operationalized).

---

## Sentiment Trajectory

| Extraction | SN | CN | MA | CP | SP | Nu | Direction |
|---|---|---|---|---|---|---|---|
| E10 | 24 | 31 | 19 | 12 | 4 | 10 | — |
| E11 | 26 | 33 | 16 | 11 | 3 | 11 | SN ▲ |
| E12 | 22 | 35 | 15 | 13 | 4 | 11 | SN ▼ CN ▲ |
| E13 | 24 | 30 | 16 | 12 | 3 | 15 | flat |
| E14 | 28 | 30 | 17 | 10 | 3 | 12 | SN ▲ |
| **E15** | **22** | **28** | **22** | **14** | **3** | **11** | **SN ▼ MA ▲ CP ▲** |

**Composition-adjusted reading**: The SN decline is *not* an MCP-fatigue moment — the MCP story is louder than ever — but the absolute incident-class discovery shock has passed. The MA rise is the bimodal-by-experience reframe captured in Reddit + Pragmatic Engineer's data: practitioners constraining tools rather than rejecting them. CP's rise is driven by tier-2 X/Twitter productivity boosts (5 of 10 items) and BYOK-as-enabler framing; under-weight Bluesky/Mastodon means CP is genuinely under-sampled this window.

---

## Cluster Momentum

| Cluster | E13 | E14 | E15 | Trajectory | Signal strength |
|---|---|---|---|---|---|
| Trust / Verification | 10 | 14 | 18 | ▲▲▲ (3-window climb) | Strong |
| Productivity Reality | 5 | 8 | 17 | ▲▲ (sharp rise) | Strong |
| Code Quality | 8 | 10 | 12 | ▲ | Moderate |
| Architectural Philosophy | 11 | 9 | 10 | flat | Strong |
| Incidents / Failures | 9 | 11 | 4 | ▼▼ (consolidates into single storyline) | Strong (severity, not volume) |
| Pricing / Cost | 14 | 12 | 5 | ▼▼ (transitions from sticker-shock to architecture) | Moderate |
| Enterprise / Policy | 7 | 6 | 6 | flat | Moderate |
| Dependency / Resilience | 6 | 7 | 5 | ▼ | Moderate |
| Hype vs Reality | 4 | 5 | 7 | ▲ | Emerging |
| Burnout | 6 | 7 | 0 | ▼▼▼ (dormant) | Watch |
| Team Dynamics | 3 | 3 | 5 | ▲ | Emerging |
| Deskilling | 4 | 3 | 3 | flat | Moderate |
| Hiring / Junior-Senior | 4 | 4 | 2 | ▼ | Watch |

**Momentum highlights**:
- **Fastest rising**: Productivity Reality (+9), driven by X/Twitter productivity-claim density.
- **Sharpest decline**: Pricing / Cost (-7) and Incidents / Failures (-7) — both reflect *consolidation*, not absence. Pricing has merged into byok-pricing-shift; Incidents have merged into mcp-attack-surface.
- **Most contested**: Trust / Verification and Productivity Reality — both bimodal, with senior practitioners and survey aggregates reading the same data differently.

---

## Signal Evolution

| signal_id | First appeared | Last observed | Obs count | Status | Trajectory | Confidence | Action |
|---|---|---|---|---|---|---|---|
| `cost-runaway` | E1 | E15 | 10 | Promoted | Continuing | H | Track — now expressed as architecture shift, not numeric escalation |
| `mcp-attack-surface` | E1 | E15 | 9 | Promoted | Intensifying | H | Track — new exploit class added in-window (AgentJacking) |
| `anthropic-trust-arc` | E4 | E14 | 8 | Promoted | Tilting Negative | H | Track — dormant this window, watch E16 for Anthropic AgentJacking response |
| `cve-acceleration` | E6 | E14 | 8 | Promoted | Continuing | H | Track |
| `stack-composition` | E2 | E14 | 7 | Promoted | Continuing | H | Track |
| `vibe-coding-disreputed` | E5 | E14 | 6 | Promoted | Stabilizing | H | Track |
| `delegation-gap-paradox` | E11 | E15 | 5 | Promoted | Continuing | H | Track — now bimodal-by-experience-level |
| `cognitive-debt-deskilling` | E5 | E15 | 5 | Promoted | Confirming | H | Track — graduates to Radar this window |
| `ai-burnout-paradox` | E4 | E14 | 4 | Promoted | Reactivated | H | Track — dormant this window after E14 vocabulary consolidation |
| `agent-production-destruction` | E2 | E15 | 4 | Promoted | Continuing | H | Track — PocketOS + AgentJacking both map to anti-pattern |
| `productivity-paradox` | E3 | E15 | 7 | Promoted | Continuing | M | Track |
| `junior-pipeline-collapse` | E5 | E14 | 4 | Promoted | Newly Contested | M | Watch E16 for second remote-work-vs-AI study |
| `claude-code-automation-platform` | E10 | E14 | 3 | Tracking | Tilting consolidating | M | Track — IDE-paradigm-shift may absorb this signal |
| `delegation-gap-paradox` | E11 | E15 | 5 | Promoted | Continuing | H | (dup row — see above) |
| `ide-paradigm-shift` | **E15** | E15 | **1 (NEW)** | Tracking | Initial | M | Watch E16 for production case study |
| `byok-pricing-shift` | **E15** | E15 | **1 (NEW)** | Tracking | Initial | M | Watch E16 for VS Code BYOK adoption signal |
| `fable5-release` | E14 | E14 | 1 | Tracking | Single-window | M | Watch E16 for Fable 5 vendor-restriction follow-up |
| `vendor-model-independence` | E13 | E13 | 1 | Tracking | Dormant | M | Watch GLM-5.2 absorption (E15 single observation) |
| `ai-as-infrastructure` | E13 | E13 | 1 | Tracking | Dormant | M | Watch for next dual-vendor outage |
| `ai-dependency-trap` | E12 | E14 | 2 | Tracking | Confirming | M | Track |
| `review-cost-inversion` | E11 | E14 | 4 | Tracking | Continuing | M | Track |
| `agent-infrastructure-inflection` | E11 | E14 | 4 | Tracking | Continuing | M | Track |
| `oss-maintainer-pushback` | E8 | E14 | 5 | Tracking | Continuing | M | Track |
| `enterprise-ai-controls` | E10 | E15 | 4 | Tracking | Continuing | M | Track (ServiceNow kill switch re-anchor) |

[NEW in v1.3 summaries mode: signal IDs quoted directly from input pattern.id slugs; cross-window continuity preserved by slug-stability mandate.]

---

## Cross-Extraction Contradictions

| Claim | First position | E14 position | E15 position | Evolution | Assessment |
|---|---|---|---|---|---|
| AI coding tools materially accelerate engineering output | Strongly supported (E1–E3) | Contested (E11+) | Contested | Maturation: from headline claim to bimodal-by-experience reading | **Settled-contested** |
| Anthropic's vendor posture is enterprise-reliable | Supported (E4–E6) | Tilting Negative (E14) | Tilting Negative | Compounding: MCP RCE + outages + AgentJacking | **Tilting Negative** |
| MCP architecture is enterprise-safe | Forecasted concern (E1–E10) | Tilting Negative (E14) | Tilting Negative | Confirmed as systemic issue with 200K+ vulnerable instances | **Tilting Negative** |
| Junior pipeline collapse is AI-caused | Strongly supported (E5–E11) | Newly Contested (E14) | Insufficient signal E15 | Watch | **Newly Contested, pending** |
| Cursor's vendor stability supports adoption recommendation | Supported (E1–E13) | (not addressed) | Newly Contested (E15) | New contestation surface | **Newly Contested** |
| AI coding tools work in greenfield without operator skill | Supported in some quarters | (not addressed) | Tilting Negative (E15) | Stack Overflow + practitioner reframing | **Tilting Negative** |
| Vibe coding is a viable production practice | Supported early; contested mid (E5–E10) | Resolved Negative (E14) | (terminology cycle complete) | Resolved | **Resolved Negative** |
| Fable 5 represents a clear quality leap | (NEW E14) | Contested | (dormant) | Watch | **Contested, single-window** |

---

## Vocabulary & Framing Drift

| Term | First appeared | Frequency trend | Significance |
|---|---|---|---|
| AgentJacking | **E15 (2026-06-21)** | NEW | High — names a new MCP exploit class; The New Stack as the canonical reference |
| Cognitive debt | E12 (formalized E15) | ▲▲ | High — now a ThoughtWorks Radar Trial entry, paired with LeadDev framing |
| Agent Experience (AX) | E15 | NEW | High — Theo t3.gg framing; replaces DX as the design target |
| Coding agent swarms | E15 | NEW | High — ThoughtWorks Radar entry |
| Team of coding agents | E15 | NEW | High — ThoughtWorks Radar entry |
| BYOK (in IDE context) | E15 (2026-06-18 anchor) | NEW | High — VS Code blog as the canonical reference |
| Vibe & Verify | E14 | Stabilizing | High — completes vibe-coding terminology cycle |
| Brain fry / cognitive crunch / agentic fatigue | E14 | (dormant E15) | Moderate — three names for one concept; consolidation expected |
| Big model smell | E14 | (dormant E15) | Moderate — Willison framing for over-eager Fable 5 behavior |
| Reset year / two-debts framing | E11 / E15 | ▲ | Moderate |
| Mother of all AI supply chains | E14 | Continuing | High — OX Security framing now industry shorthand |

---

## Gaps & Uncertainties

- **Bluesky/Mastodon zero-yield (six consecutive windows)** — even with ChatGPT browsing fallback, direct-handle navigation returns no in-window items. Structural workaround required: Claude-in-Chrome direct app navigation to specific handles.
- **Two Theo t3.gg YouTube URLs unverified** (XYYZM01P2S0, EXeCOsIu0Ps) — Gemini-grounded; manual click-through required before consumer-tier surfacing.
- **arXiv preprints and Anthropic comprehension study** — not in-band confirmable this window; flagged for E16.
- **Microsoft internal Claude-Code license cancellations** — second-hand attribution via Medium + Pragmatic Engineer; no direct internal confirmation.
- **Cursor acquisition narrative** — highest-engagement in-window Cursor thread presupposes an acquisition not officially announced.
- **Anthropic's response to AgentJacking** — no vendor statement or advisory in window. Watch E16.

---

## Watch List for Next Extraction

- **Confirmation or refutation of the Cursor acquisition narrative** — vendor statement or Bloomberg/TechCrunch primary. *Highest priority.*
- **Anthropic AgentJacking response** — security advisory, post-disclosure CVE assignment, official position on MCP sanitization. *Highest priority.*
- **First production case study of VS Code BYOK** at enterprise scale (post 2026-06-18 release). *Highest priority.*
- **GLM-5.2 / open-weights coding-model adoption signal** — does this graduate `vendor-model-independence`? Watch HN, Reddit, Pragmatic Engineer.
- **Manual click-through verification of Theo t3.gg June 2026 video uploads** to confirm Gemini-supplied URLs.
- **Bluesky/Mastodon direct-handle navigation via Claude in Chrome** — operationalize as documented gap-fill ahead of E16.
- **Junior-pipeline-collapse re-contest evidence** — second remote-work-vs-AI study or second enterprise-tripling-hire report would destabilize consolidation.
- **arXiv Brynjolfsson "canaries" preprint and Anthropic comprehension study** — carry over from E14 watch.

---

## Longitudinal Report Metadata

| Field | Value |
|-------|-------|
| Longitudinal prompt | v1.3 |
| Domain config | v1.2 |
| Bootloader | v1.9 |
| Report generated | 2026-06-22 17:45 UTC |
| Input mode | summaries (--from-summaries) |
| Extractions covered | E1 through E15 |
| Date range | 2026-03-20 – 2026-06-22 (94 days) |
| Total tagged items | ~727 (sum across summaries; E15 = 39-item ChatGPT+Grok+Gemini cross-LLM corpus) |
| Tracked signals | 24 unique signal_ids across the program; 13 Promoted, 8 Tracking, 3 confirmed retire-or-merge |
| NEW signals this window | `ide-paradigm-shift`, `byok-pricing-shift` |
| Escalated signals this window | none (consolidation week) |
| Confirmed trends | `cost-runaway` (10 obs), `mcp-attack-surface` (9 obs), `anthropic-trust-arc` / `cve-acceleration` (8 obs each), `stack-composition` (7 obs), `productivity-paradox` (7 obs), `vibe-coding-disreputed` (6 obs), `cognitive-debt-deskilling` / `delegation-gap-paradox` (5 obs each), `oss-maintainer-pushback` (5 obs) |
| Resolved contradictions | "Vibe coding uniformly dangerous" (Resolved Negative E14, holds); prior resolutions hold; new contestations: "Cursor vendor stability" (E15 NEW), "AI works in greenfield without operator skill" (E15 NEW) |
| Newly contested claims | "Cursor's vendor stability is reliable enough for adoption recommendation" (Newly Contested E15 NEW); "AI coding tools work for greenfield without operator skill" (Tilting Negative E15 NEW) |
