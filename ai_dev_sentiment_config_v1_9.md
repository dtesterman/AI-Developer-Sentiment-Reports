# AI Dev Sentiment Extraction — Config

## Config Metadata

- Config-Version: v1.9
- Prompt Name: AI Dev Sentiment Extraction

## Changelog

- **v1.9**: Post-extraction-2026-06-29 vocabulary update. **New source added to Blogs / Publications: dev.to** — Forem-based practitioner publishing platform with a large developer community writing long-form on AI coding tools, MCP, vibe coding, cognitive debt, and adjacent topics. Cleanly indexed by search engines. Tier 1 for all LLM targets. Coverage gap identified during 2026-06-29 remediation review. **dev.to SEO-listicle filter** added after trial extraction found roughly half of results were SEO listicle churn from bot-generated author handles — see dev.to query block for exclusion rules. **METR (metr.org) promoted from Tier 3 Manual to Tier 1 Blogs / Publications** — trial extraction found the site is fully search-indexed and returned extraction-ready material on first query, including the 2026-06-26 GPT-5.6 Sol evaluation post that anchors the "frontier models cheating evaluations" pattern. Tier 3 categorization in the initial v1.9 draft was wrong; corrected here. **simonwillison.net promoted to first-class always-check source** — trial extraction returned six in-window / adjacent-window Fable 5 posts on the first query (including the 2026-06-16 "Fable 5 Export Controls Harm US Cyber Defense" opinion piece that was previously not anchored in extraction). Consistently high yield, single trusted author, zero noise — deserves standalone treatment in the query block, not one line among many. Driven by query-expansion findings on the 2026-06-22 → 2026-06-29 run, where novel vocabulary in first-pass items surfaced material that the static v1.8 batches did not. **New Batch J — Regulation / Export Control** added to capture the dominant theme of late June 2026: US-government-coordinated capability-based access restrictions on frontier coding models (Anthropic Fable 5 / Mythos 5 06-12 suspension and partial 06-26 restoration; OpenAI GPT-5.6 Sol / Terra / Luna 06-26 restricted-preview release). **Batch E (Specific Tools & Preferences)** expanded with: Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Sonnet 5, GPT-5.6 Sol / Terra / Luna, DeepSeek V4 / V4-Pro / V4 Flash, GLM-5.2, Cursor Composer 2.5, Cursor Premium seat. **Batch F (Enterprise/Policy)** expanded with: Microsoft Claude Code cancellation, Cursor Teams pricing, Uber AI cap. **Batch G (Incidents & Postmortems)** expanded with: ExploitBench / exploit evals, agentjacking, METR cheating-rate evaluation findings, Andy Jassy / Scott Bessent trigger story, jailbreak disclosure cycle, Sentry-key exposure / agent hijack class. **Batch H (Pricing/Cost/ROI)** expanded with: tokenmaxxing, valuemaxxing, token discipline, FinOps reckoning. **Tools to Track** expanded with: Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Sonnet 5, GPT-5.6 Sol / Terra / Luna, DeepSeek V4 / V4-Pro / V4 Flash, GLM-5.2, Cursor Composer 2.5. **Tracked Dimensions** Topic values added: Regulation / Export Control, Investor Conflict of Interest, Open-Weight Sovereignty. **Platform Query Blocks** updated: Bluesky promoted from Tier 1 (Claude column) to Tier 1 Confirmed — the 2026-06-29 logged-in-user remediation pass confirmed Bluesky as the highest-yield Tier 1 source when an authenticated session is available; Reddit demoted to Tier 1 Cross-LLM only for Claude target (Reddit blocked at Claude in Chrome navigate level by safety restriction — Primary WebSearch site: queries also non-functional; recovery only via cross-LLM escalation). This is a Claude-specific tier change; other LLM target columns unchanged. Compatible with engine v1.6 (Min Config Version v1.3 unchanged in engine — no engine compatibility break).
- **v1.8**: Demoted Flipboard user-curated magazines from Blogs / Publications (Experimental) to Tier 3 Manual. Root cause: Dedicated extraction run (2026-04-02) confirmed that Flipboard @user/magazine URL paths are not indexed by any search engine — all 5 query variants returned zero results across the entire 2026 YTD period. The flipboard.com domain is also blocked by egress proxy, preventing direct fetch as fallback. The magazine content exists and is actively curated (709 stories, 102 followers) but is only reachable via direct browser navigation. Resolution: Created flipboard-extraction skill for on-demand browser-based extraction via Claude in Chrome. Automated scheduled extraction cannot use browser tools (headless execution context). Flipboard queries moved to Tier 3 Manual Sources table with note pointing to the new skill. Removed Blogs / Publications (Experimental) query block entirely — leaflet.pub retained as experimental entry with inline note under standard Blogs / Publications block.
- **v1.7**: Added Flipboard curated AI magazine (@maryflipse3/ai) to Blogs / Publications (Experimental) query block. Flipboard aggregates content from multiple sources — treated as experimental pending retrieval verification across extractors.
- **v1.6**: Post-E1 performance report fixes. Platform changes: LinkedIn demoted to Tier 3 Manual. Batch C expanded (deskilling, cognitive debt, bootcamp). Batch G expanded with MCP CVE vocab. Batch H expanded with FinOps. Batch F expanded with OSS governance bodies. Batch B expanded with longitudinal experience reports. Batch A expanded with Brynjolfsson citation. Reddit fallback syntax. Bluesky/Mastodon handle-specific queries. YouTube channel-name + topic format. Podcast channel expansion. New Tier 3 sources: LinkedIn (demoted), Brynjolfsson "Canaries", podcast channels. Tools to Track: added MCP. Tracked Dimensions: added Deskilling.
- **v1.5**: Added ThoughtWorks Radar and Engineering Blog to Blogs / Publications. Added MIT Media Lab and Margaret Storey (UVic) to Tier 3. Added leaflet.pub experimental.
- **v1.4**: Removed Compatible-Engine-Version from metadata. Engine now owns compatibility requirement. Config-Version field renamed for consistency.
- **v1.3**: Removed LLM Target from Default Parameters.
- **v1.2**: Added Compatible-Engine-Version field. Added Batch Registry section. Added "observed exposure" to Batch A. Added Researcher (Vendor-affiliated) to Author Type dimension.
- **v1.1**: Removed "Grok" from Prompt Name. Added LLM Target parameter. Replaced static Source Assignments with Platform Tier Assignments table keyed by LLM Target.
- **v1.0**: Extracted from monolithic prompt v0.8.0. Established baseline for all volatile content: tools list, default parameters, source assignments, query batches, platform query blocks, and tracked dimensions.

---

## Default Parameters

| Parameter | Default | Override Syntax |
|-----------|---------|-----------------|
| Lookback | Past 14 days | `--since YYYY-MM-DD` |
| Max items/tier | 10 | `--limit N` (cross-references excluded) |
| Batches | All | `--batches A,B,E` (see Batch Registry) |
| Tier scope | Tier 1 + 1.5 | `--tiers 1,1.5,2` |
| Query Expansion | On (engine v1.6+) | `--no-expand` (engine flag, not config) |

**Note:** LLM Target is not a configurable parameter — it is self-resolved by the running LLM at startup. Use `--llm <target>` only to override for simulation or testing purposes.

**Example:** `Run extraction --since 2026-06-22 --limit 100 --batches A,B,F,J`

---

## Batch Registry

Authoritative list of all defined batches. The engine's Commands table and `--batches` override parameter reference these labels. Add new batches here first; the engine requires no update to accept them as focus commands.

| Batch | Topic |
|-------|-------|
| A | Job Impact & Hiring |
| B | Quality / Productivity / Trust |
| C | Learning / Skills |
| D | Burnout / Cognitive Load |
| E | Specific Tools & Preferences |
| F | Enterprise / Policy |
| G | Incidents & Postmortems |
| H | Pricing / Cost / ROI |
| I | Architectural Philosophy |
| **J** | **Regulation / Export Control** *(new in v1.9)* |

---

## Platform Tier Assignments

Platform tiers vary by LLM Target due to differences in native platform access. Use the column matching the active `--llm` value to resolve tier assignments at runtime. If the LLM Target value does not match any column, the engine will halt — see LLM Target Resolution in the engine.

| Platform | Grok | Claude | ChatGPT | Gemini |
|----------|------|--------|---------|--------|
| X/Twitter | Tier 1 | Tier 2 | Tier 2 | Tier 2 |
| Reddit | Tier 1 | **Tier 1 Cross-LLM only** *(v1.9)* | Tier 1 | Tier 1 |
| Hacker News | Tier 1 | Tier 1 | Tier 1 | Tier 1 |
| Blogs / Publications | Tier 1 | Tier 1 | Tier 1 | Tier 1 |
| YouTube (curated channels) | Tier 1.5 | Tier 1.5 | Tier 1.5 | Tier 1.5 |
| Bluesky | Tier 1.5 Experimental | **Tier 1 Confirmed** *(v1.9, login required)* | Tier 1 | Tier 1.5 Experimental |
| Mastodon | Tier 1.5 Experimental | Tier 1 | Tier 1 | Tier 1.5 Experimental |
| LinkedIn | Tier 3 Manual | Tier 3 Manual | Tier 3 Manual | Tier 3 Manual |
| Podcasts | Tier 2 | Tier 2 | Tier 2 | Tier 2 |
| IEEE/ACM/arXiv | Tier 3 | Tier 3 | Tier 3 | Tier 3 |
| Non-English forums | Tier 3 | Tier 3 | Tier 3 | Tier 3 |
| Paywalled content | Tier 3 | Tier 3 | Tier 3 | Tier 3 |
| Internal (Discord/Slack) | Internal | Internal | Internal | Internal |

**Notes:**

- Grok has native X/Twitter firehose access — Tier 1 is appropriate.
- Claude and ChatGPT have reliable Bluesky/Mastodon web search access — Tier 1.
- **Reddit Claude row updated v1.9:** Reddit is blocked at the Claude in Chrome navigate level by safety restriction, AND Primary WebSearch `site:reddit.com` queries are non-functional for Claude (E1 finding, v1.6). The only working retrieval path from a Claude run is cross-LLM escalation (ChatGPT or Grok via their respective Chrome logins). Items retrieved this way are provisional per engine v1.6 Retrieval Channel Accounting and must carry `retrieved_via` field for analysis-stage verification.
- **Bluesky Claude row updated v1.9:** When the user has an active Bluesky login in the Chrome session, full-text search becomes available and is the highest-yield Tier 1 source for practitioner voice (2026-06-29 remediation pass produced 23 in-window items). When not logged in, Bluesky public profile pages are still accessible without auth and can be navigated directly by handle.
- **LinkedIn demoted to Tier 3 Manual (v1.6):** Manual browser search required.
- To add a new LLM target: add a column, populate all rows, and the engine will accept it automatically via the guard clause in LLM Target Resolution.

---

## Tools to Track

Copilot (incl. Workspace/Agent), Cursor (incl. Composer 2.5, Premium seat), Claude (Claude Code, Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Sonnet 5), ChatGPT/Codex (incl. GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna), Amazon Q Developer, Gemini Code Assist/CLI, Tabnine, Codeium/Windsurf, Devin, Replit Agent, JetBrains AI, Sourcegraph Cody, Aider, Continue.dev, Warp, MCP (Model Context Protocol), **open-weight stack: DeepSeek V4 / DeepSeek V4-Pro / DeepSeek V4 Flash, GLM-5.2** *(v1.9)*, emerging tools.

---

## Query Batches

### A: Job Impact & Hiring *(unchanged from v1.6)*

"AI coding" jobs | "Copilot" layoffs OR hiring | "AI replacing" developers
"junior developer" AI future | "entry-level" programmer AI
"AI coding" resume OR required | developer hiring AI 2026
"hiring manager" AI coding | "junior developer" AI "entry level" hiring decline 2026
"observed exposure" AI labor | "observed exposure" developer employment
Brynjolfsson "canaries in the coal mine" AI employment
"young workers" AI exposed occupations hiring
"22 to 25" OR "entry-level" AI coding employment 2026

### B: Quality / Productivity / Trust *(expanded v1.9)*

"AI generated code" bugs OR quality OR security | "vibe coding"
"Copilot" OR "Cursor" productivity | "AI code" review OR trust
"AI coding" slower OR faster | "AI code" technical debt
"vibe coding" + "technical debt" | "AI code" + "technical debt" + percent
"AI code review" burden | "AI code review" overwhelm large PRs
"AI generated code" bulk review fatigue | shipping "AI code" can't fully review
"vibe coding" + security OR quality OR risk | "cognitive debt" AI code
"AI generated code" comprehension OR "don't understand" OR "can't explain"
"AI coding" "90 day" OR "6 month" experience report
"AI coding" "long-term" experience review
"AI tools" longitudinal review productivity
**"Claude regressed" OR "model nerfed" OR "model regression" 2026** *(v1.9 — practitioner regression complaints emerged repeatedly in 2026-06-29 Bluesky pass)*
**"AI code" mobile performance OR "load like sludge"** *(v1.9 — Catt Small framing on user-visible quality decay)*
**"AI coding" "almost right" verification bottleneck** *(v1.9 — Stack Overflow / Sonar 2026 survey vocab)*

### C: Learning / Skills *(unchanged from v1.6)*

"AI coding" learning OR skills OR mastery | "junior developer" AI learning
"AI assistance" comprehension | "coding bootcamp" AI curriculum
"AI coding" deskilling OR "losing skills" OR "skill atrophy"
"cognitive debt" developer learning | "cognitive debt" junior developer
"junior developer" AI fundamentals 2026 | "new developer" AI reliance
"bootcamp" AI tools curriculum | "bootcamp graduate" AI coding
"career changer" programmer AI | "self-taught" developer AI tools
"AI coding" muscle memory OR "building intuition"
"AI assistance" "never learned" OR "skipped learning"
"learning to code" AI 2026 | "teaching programming" AI tools
fundamentals "AI coding" skip OR bypass
"AI pair programming" learning curve | "AI coding" mentorship replacement

### D: Burnout / Cognitive Load *(unchanged from v1.6)*

"AI coding" burnout OR exhausted OR overwhelmed
"AI tools" cognitive load OR "context switching"
"Copilot" OR "Cursor" fatigue | developer burnout AI 2026
"AI coding" flow state | "Ghost-in-the-Loop"
"AI coding" cultural discipline norms | "AI code" reviewer overwhelm
"20k lines" OR "large PR" AI generated
"AI coding" dependency outage OR unavailable OR "doesn't work"
Claude OR Copilot OR Cursor outage dependency
"cognitive debt" burnout | "cognitive debt" overwhelm
"AI coding" mental health | "AI tools" stress developer
**"AI workaholic" OR "Claude Code" dopamine OR FOMO** *(v1.9 — Dare Obasanjo framing)*

### E: Specific Tools & Preferences *(expanded v1.9)*

"Cursor" review OR experience -mouse | "Claude Code" | "Copilot" -earnings -stock
"Devin AI" | "Windsurf" AI | "Gemini CLI"
Copilot vs Claude vs Cursor | "switching to" Claude OR Cursor | "stopped using" Copilot
"context window" + Cursor OR Claude
"Claude Code" transformed OR "can't imagine" OR "love using"
"Cursor" transformed workflow OR "game changer"
ThePrimeagen "99" tool
r/ClaudeCode | "Claude Code" reddit
r/vibecoding | "vibe coding" reddit experience
"MCP" Claude OR Cursor | "Model Context Protocol" developer
**"Claude Fable 5" OR "Fable 5" coding | "Claude Mythos 5" OR "Mythos 5" cybersecurity** *(v1.9)*
**"Claude Opus 4.8" coding review | "Claude Sonnet 5" release** *(v1.9)*
**"GPT-5.6 Sol" OR "GPT-5.6 Terra" OR "GPT-5.6 Luna"** *(v1.9)*
**"Composer 2.5" Cursor experience | "Cursor Premium" seat** *(v1.9)*
**"DeepSeek V4" OR "DeepSeek V4-Pro" OR "DeepSeek V4 Flash" coding** *(v1.9)*
**"GLM-5.2" coding OR agents | "GLM-5.2" open weights** *(v1.9)*
**"open weights" coding agent practitioner 2026** *(v1.9)*

### F: Enterprise / Policy *(expanded v1.9)*

"AI coding policy" enterprise | "AI coding" FAANG OR "big tech"
"AI coding tools" banned OR restricted | CTO "AI coding"
Microsoft "AI coding" policy | Google "AI coding" policy | Amazon "AI coding" policy
"AI code" + liability OR insurance
"AI coding" security guardrails enterprise
"AI code generation" security review process
standardizing "AI coding" workflows security
"agent control plane" enterprise OR policy
Google engineers "AI coding" internal 2026
Amazon engineers "AI coding" policy 2026
Microsoft engineers "AI coding" internal
LLVM "AI generated code" policy | Apache "AI coding" policy
Rust foundation "AI coding" OR "AI generated" policy
Python "AI coding" policy OR guidelines
CNCF "AI coding" OR "AI generated" policy
"open source" "AI generated code" contribution policy
Linux kernel "AI code" policy
**Microsoft "Claude Code" cancellation OR "Copilot CLI" migration** *(v1.9 — 06-30 effective date)*
**Cursor "Teams Pricing" 2026 | "Composer/Auto" usage pool** *(v1.9)*
**Uber "AI coding tools" cap $1500 OR Claude Code cap** *(v1.9)*
**"AI coding" "spending tier" OR "per developer cap"** *(v1.9)*

### G: Incidents & Postmortems *(expanded v1.9)*

"AI generated code" bug OR incident OR outage
"Copilot" OR "Cursor" OR "Claude" mistake OR error
"AI code" production incident | "AI coding" security vulnerability
"AI code" postmortem OR "root cause"
"AI generated" rollback OR revert
"AI code" + liability OR insurance OR damages
"AI agent" delete OR revert OR rollback incident
"AI agent" autonomous destruction OR "decided to delete"
CVE "AI coding tool" 2026
site:github.com/issues "AI generated" bug
MCP "prompt injection" CVE | MCP vulnerability security
"Model Context Protocol" security vulnerability
"AI agent" "code execution" vulnerability
"vibe coding" "security vulnerability" 2026
"AI coding tool" CVE 2026 | "AI assistant" security advisory
"Claude Code" OR "Cursor" security incident
**"ExploitBench" OR "exploit eval" Anthropic OR OpenAI** *(v1.9 — the metric that triggered 06-12 controls)*
**"agentjacking" Sentry OR "agent hijack" Cursor OR Claude Code** *(v1.9)*
**METR "GPT-5.6" OR "Claude" evaluation cheating** *(v1.9 — model gaming eval harness)*
**"Andy Jassy" OR "Scott Bessent" Anthropic Fable 5** *(v1.9 — trigger story)*
**"jailbreak" Fable 5 OR Mythos 5 Anthropic** *(v1.9)*
**"slopsquatting" 2026 | hallucinated package supply chain attack** *(v1.9 — recurring pattern)*

### H: Pricing / Cost / ROI *(expanded v1.9)*

"AI coding" pricing OR cost OR expensive | "API costs" coding OR developer
"token" cost anxiety OR budget | Copilot OR Cursor subscription cost
"AI coding" ROI | "AI coding" subscription value | "vibe coding" expensive
"AI refactoring" token cost context window
"AI infrastructure" cost pressure hosting | AI memory DRAM cost impact
"AI tool cost" per developer | "cost per developer" AI coding
FinOps AI | FinOps "AI coding" | FinOps developer tools
"AI coding" budget enterprise | "AI tools" cost management
"API spend" coding OR developer | "token budget" team OR enterprise
Copilot OR Cursor "price increase" OR pricing 2026
"AI coding" cost-benefit | "AI coding" TCO
**"tokenmaxxing" 2026 | "valuemaxxing" enterprise AI** *(v1.9)*
**"token discipline" AI coding enterprise | "FinOps reckoning"** *(v1.9)*
**Chinese AI models cheaper enterprise migration 2026** *(v1.9 — DeepSeek / GLM cost story)*
**"AI coding" "spending tier" 2026 OR "monthly cap" Claude Code** *(v1.9)*

### I: Architectural Philosophy *(unchanged from v1.6)*

"AI code" maintainability debate long-term
"throw away code" AI regenerate vs maintain
"AI code" architecture decisions sustainability
"AI-maintainable" OR "machine-readable code"
technical debt "AI generated code" long-term
"human-readable" vs "AI-readable" code
"just regenerate" AI code vs refactor
"AI code" ownership | "AI generated" code ownership team
"disposable code" AI | "ephemeral code" AI regenerate
"AI coding" "system design" philosophy
"AI generated" monolith vs microservices
"AI code" refactoring vs rewriting
"generalists" AI coding architecture | "T-shaped" developer AI

### J: Regulation / Export Control *(NEW in v1.9)*

This batch captures the dominant late-June 2026 theme: US-government-coordinated capability-based access restrictions on frontier coding models, and the structural side-effects (lawsuits, IPO valuation impact, open-weight Chinese stack advantage, investor-as-regulator dynamics).

"export control" "AI coding" OR "frontier model" 2026
"export control" Anthropic OR OpenAI Claude OR GPT
US government "AI model" access restriction 2026
Trump administration "AI coding" OR "frontier AI" gating
Commerce Department BIS "AI model" directive
"Bureau of Industry and Security" Anthropic OR OpenAI
"Fable 5" OR "Mythos 5" restored OR suspended OR access
"GPT-5.6" restricted preview OR "trusted partners"
"100 institutions" Mythos OR Anthropic
Anthropic Tom Brown OR Dario Amodei US government meetings
"capability-based" regulation AI coding
"pre-release review" AI model government
"nationality-based access" AI model | "foreign national" Claude OR GPT
Legion lawsuit OR "vacate Commerce Department" AI
"investor conflict" Amazon Anthropic | "Bedrock" competitor Anthropic
"sovereignty" AI coding stack | "AI stack" sovereignty enterprise
"open weights" "export control" 2026 | "DeepSeek" "Chinese AI" market share
IPO valuation Anthropic OR OpenAI export control
researchers fear "AI safety rules" open research
"regime change" AI access OR frontier model 2026

---

## Platform Query Blocks

### Reddit (Claude target: Cross-LLM escalation required — see Tier Assignments)

For Claude target, Reddit content must be retrieved via cross-LLM escalation (ChatGPT or Grok with active Chrome login). Items retrieved this way carry `retrieved_via: "<LLM> (cross-LLM escalation)"` per engine v1.6 Retrieval Channel Accounting. Use the following subreddit list for any escalated query:

r/ExperiencedDevs, r/cscareerquestions, r/programming, r/webdev, r/learnprogramming, r/devops, r/sysadmin, r/cursor, r/ClaudeAI, r/ClaudeCode, r/vibecoding, r/softwarearchitecture, r/MachineLearning, r/LocalLLaMA

For other LLM targets, retain v1.6 / v1.8 site:reddit.com query block (unchanged).

### Hacker News *(unchanged from v1.6 except expanded vocab below)*

site:news.ycombinator.com "AI coding"
site:news.ycombinator.com "Copilot" OR "Cursor" developer
site:news.ycombinator.com "AI generated code" quality
site:news.ycombinator.com "AI coding" postmortem OR incident
site:news.ycombinator.com "AI code" maintainability architecture
site:news.ycombinator.com "cognitive debt" OR "AI code comprehension"
site:news.ycombinator.com "vibe coding"
site:news.ycombinator.com "Claude Code" OR "Cursor" experience
site:news.ycombinator.com "junior developer" AI
site:news.ycombinator.com MCP OR "Model Context Protocol"
**site:news.ycombinator.com "Fable 5" OR "Mythos 5" OR "GPT-5.6"** *(v1.9)*
**site:news.ycombinator.com "ExploitBench" OR "agentjacking"** *(v1.9)*
**site:news.ycombinator.com "GLM-5.2" OR "DeepSeek V4" OR "Composer 2.5"** *(v1.9)*
**site:news.ycombinator.com "export control" Anthropic OR OpenAI** *(v1.9)*
**site:news.ycombinator.com "Andy Jassy" Anthropic OR "investor conflict" AI** *(v1.9)*

### Blogs / Publications *(unchanged from v1.8 except expanded vocab below)*

site:thoughtworks.com/radar AI coding OR agents OR Copilot OR Cursor
site:thoughtworks.com/radar "coding agents" OR "AI pair programming"
site:thoughtworks.com/insights/blog AI coding developer productivity
site:thoughtworks.com/insights/blog "vibe coding" OR "AI generated code"
site:thoughtworks.com/insights/blog Copilot OR Cursor OR Claude
site:pragmaticengineer.com AI coding OR "AI tools"
site:blog.pragmaticengineer.com "AI coding" OR Copilot OR Cursor
"Pragmatic Engineer" AI coding survey
site:semianalysis.com AI coding OR developer productivity
site:theregister.com "AI coding" OR "AI generated code"
site:leaflet.pub AI coding
**Fortune OR Bloomberg OR Semafor Anthropic Fable 5 OR Mythos 5** *(v1.9 — beat reporters on the regulation story)*
**site:red.anthropic.com OR site:anthropic.com/news Fable OR Mythos OR exploit** *(v1.9 — vendor-side technical disclosures)*

**--- Always-check first-class practitioner source: simonwillison.net *(v1.9)* ---**

Simon Willison publishes multi-times-per-week on AI coding tools, model releases, and adjacent topics. Trial extraction 2026-06-29 confirmed consistently high yield, single-author, zero-noise. Every weekly run should query this site directly.

site:simonwillison.net Claude Code OR "Claude Code"
site:simonwillison.net Fable 5 OR Mythos 5 OR Opus 4.8 OR Sonnet 5
site:simonwillison.net Cursor OR Copilot OR "GPT-5.6"
site:simonwillison.net MCP OR "Model Context Protocol"
site:simonwillison.net "vibe coding" OR "agentic engineering" OR "cognitive debt"
site:simonwillison.net export control OR restriction OR US government AI
site:simonwillison.net GLM OR DeepSeek OR "open weights"
site:til.simonwillison.net (Simon's TIL subdomain — implementation notes)

Also check Simon's tag pages when reviewing focused topics:
- simonwillison.net/tags/claude-code/
- simonwillison.net/tags/claude-mythos/
- simonwillison.net/tags/ai-assisted-programming/
- simonwillison.net/tags/agentic-engineering/

**--- Always-check first-class research source: metr.org *(v1.9 — corrected from Tier 3)* ---**

METR (Model Evaluation & Threat Research) publishes pre-deployment evaluations of frontier models with concrete cheating / reward-hacking evidence. Trial extraction 2026-06-29 confirmed the site is fully search-indexed and returned the 2026-06-26 GPT-5.6 Sol evaluation blog (anchor for the "frontier models cheat evaluations" pattern) on first query. Author Type: `Researcher`. Tier 1 for all LLM targets.

site:metr.org 2026 evaluation
site:metr.org cheating OR "reward hacking" OR exploit
site:metr.org GPT-5.6 OR Claude OR Sol OR Mythos
site:metr.org "time horizon" OR HCAST
site:metr.org/blog frontier

Also flag METR PDFs (HCAST, evaluation methodology) for Tier 3 manual review of the underlying methodology when a specific finding is being extracted.

**--- dev.to *(v1.9 — practitioner publishing platform, Tier 1 with SEO-listicle filter) ---**

⚠️ **SEO-LISTICLE FILTER** — Trial extraction 2026-06-29 found roughly half of dev.to results are SEO churn from bot-generated author handles (patterns like `_d7eb1c1703182e3ce1782`, `jovan_chan_9500711396d4e6`). Apply this filter before extracting any dev.to result to Tier 1:

Exclude if any of the following apply:
- Title matches SEO listicle patterns: `"Complete Guide to"`, `"Which Wins"`, `"Showdown"`, `"Comparison Guide"`, `"The Real Cost After"`, `"7 [Something] You Need"`, `"[N]+ Tools Compared"`, `"Ultimate Guide"`
- Author handle is a random alphanumeric string longer than 8 characters with no consistent identity (e.g. `_d7eb1c1703182e3ce1782`)
- Author has fewer than 3 total published posts on dev.to and no verifiable identity outside dev.to
- Post body reads as SEO-optimized comparison content without a first-person practitioner voice or original code / experiment / benchmark

Prefer authors with:
- Recognizable identity outside dev.to (Alex Merced/`alexmercedcoder`, Rizel Scarlett/`blackgirlbytes`, Daniel Bergholz/`danielbergholz`, Pooya Golchian/`pooyagolchian`)
- Publication history on dev.to (≥ 5 posts) and a topical focus
- Posts with concrete code, benchmarks, or first-person experience reports rather than "Which Wins" comparison summaries

Queries:

site:dev.to "AI coding" OR "Claude Code" OR "vibe coding"
site:dev.to Copilot OR Cursor OR "GPT-5.6"
site:dev.to "AI generated code" quality OR incident OR postmortem
site:dev.to "MCP" OR "Model Context Protocol" developer
site:dev.to "Fable 5" OR "Mythos 5" OR "ExploitBench" OR "agentjacking"
site:dev.to "cognitive debt" OR "skill atrophy" OR "vibe coding"
site:dev.to "GLM-5.2" OR "DeepSeek V4" OR "Composer 2.5" OR "Opus 4.8"

*leaflet.pub: Experimental — pending author credibility verification (added v1.5).*

### YouTube (Tier 1.5) *(unchanged from v1.6 except expanded channels below)*

ThePrimeagen "AI coding" | ThePrimeagen "vibe coding"
ThePrimeagen Copilot OR Cursor OR Claude
ThePrimeagen "cognitive debt" | ThePrimeagen developer productivity AI
Fireship "AI coding" | Fireship "vibe coding"
Fireship Copilot OR Cursor OR Claude 2026
"HTML All The Things" AI coding | "HTML All The Things" Copilot
"HTML All The Things" "vibe coding" | "HTML All The Things" Claude
"Bricks Bucks Bytes" AI | "Bricks Bucks Bytes" developer AI
"The Serious CTO" AI coding | "The Serious CTO" Copilot OR Cursor
Theo "AI coding" | Theo t3 Cursor OR Claude
"Syntax FM" AI coding | "Syntax" podcast Copilot
**Theo t3 "GPT-5.6" OR "Fable 5" OR "Mythos 5"** *(v1.9 — Theo confirmed as highest-yield in-window channel in 2026-06-29 pass)*

*Note v1.9: 2026-06-29 pass found Theo (t3.gg) consistently yielded in-window AI-coding videos while ThePrimeagen and Fireship did not. Re-evaluate channel mix in next quarterly review.*

### X/Twitter *(unchanged from v1.6)*

[unchanged]

### Bluesky *(EXPANDED v1.9 — Tier 1 Confirmed for Claude when logged in)*

site:bsky.app "AI coding"
site:bsky.app Copilot OR Cursor OR "Claude Code"
site:bsky.app "vibe coding"
site:bsky.app developer AI tools
**Logged-in full-text search (highest yield, Tier 1 Confirmed for Claude):**
"AI coding" | "Claude Code" | "vibe coding" | "Cursor" | "GPT-5.6"
"Fable 5" | "Mythos 5" | "Opus 4.8" | "Composer 2.5"
"GLM-5.2" | "DeepSeek V4" | "ExploitBench" | "agentjacking"
"tokenmaxxing" | "cognitive debt" | "export control" Anthropic OR OpenAI
**Practitioner handles to check directly when search returns thin (added/confirmed v1.9):**
simonwillison.net | timkellogg.me | carnage4life.bsky.social | metr.org
arrdem.tirefireind.us | catt.design | thdxr.com | astral100.bsky.social
agathedemarais.com | anthropicbot.bsky.social

### Mastodon *(unchanged from v1.6)*

[unchanged]

### Podcasts *(unchanged from v1.6)*

[unchanged]

---

## Tier 3 Manual Sources

| Source | Query | Reason |
|--------|-------|--------|
| arXiv | AI coding assistants developer productivity | Academic preprints; manual review required |
| arXiv | Brynjolfsson "canaries in the coal mine" | Key corroborating study for Anthropic labor paper |
| IEEE/ACM | AI pair programming software engineering | Peer-reviewed; paywalled |
| MIT Media Lab | site:media.mit.edu AI developer tools OR coding assistants | Academic research lab |
| Margaret Storey (UVic) | site:margaretstorey.com OR "Margaret Storey" AI developer tools | SE researcher |
| ThoughtWorks Events | site:thoughtworks.com/events AI coding | Event content |
| LinkedIn | "AI coding" developer experience | Demoted from Tier 2 (v1.6) |
| LinkedIn | CTO "AI coding" policy | Executive AI policy discourse |
| Flipboard (@maryflipse3/ai) | <https://flipboard.com/@maryflipse3/ai-jrgbno6hz> | Demoted v1.8 |
| Podcasts (Manual) | ThePrimeagen, Syntax FM, The Changelog, CoRecursive — AI coding episodes | Manual review |
| Non-English forums | [various] | Language barrier |
| Paywalled content | [various] | Access restrictions |
| **Reddit (Claude target)** *(v1.9)* | r/ExperiencedDevs / r/cscareerquestions / r/ClaudeAI / r/cursor / r/vibecoding | **Browser-blocked for Claude in Chrome; Primary WebSearch site: queries fail. Retrieve via cross-LLM escalation (ChatGPT or Grok) and tag `retrieved_via` per engine v1.6.** |
| **Anthropic exploit-evals page** *(v1.9)* | site:red.anthropic.com 2026 | Tier 3 because vendor-published; treat as primary source for ExploitBench scoring discussions but tag Author Type as `Researcher (Vendor-affiliated)` |
| **METR methodology PDFs only** *(v1.9 — moved from Tier 3 blog to Tier 1 above)* | HCAST.pdf, evaluation report PDFs | METR's blog posts are Tier 1 (see Always-check first-class research source above). Only the underlying methodology PDFs (HCAST, full evaluation reports) require manual review here. |

---

## Tracked Dimensions

| Dimension | Values |
|-----------|--------|
| Sentiment | Positive, Negative, Mixed, Nuanced |
| Topic | Job security, Code quality, Productivity, Learning, Deskilling, Junior/Senior devs, Hiring, Hype vs Reality, Team dynamics, Trust, Burnout, Incidents, Pricing/Cost, Architectural Philosophy, Dependency/Resilience, **Regulation/Export Control** *(v1.9)*, **Investor Conflict of Interest** *(v1.9)*, **Open-Weight Sovereignty** *(v1.9)* |
| Tool | Copilot, Cursor (incl. Composer 2.5), Claude (incl. Claude Code, Fable 5, Mythos 5, Opus 4.8, Sonnet 5), ChatGPT (incl. GPT-5.6 Sol/Terra/Luna, Codex), Gemini, Devin, Windsurf, MCP, **DeepSeek (V4 / V4-Pro / V4 Flash)** *(v1.9)*, **GLM-5.2** *(v1.9)*, General AI |
| Evidence | Anecdote, Survey, Study, Opinion, Incident, Postmortem |
| Author | Practitioner, Manager, Executive, Researcher, Researcher (Vendor-affiliated), Analyst, Vendor |
