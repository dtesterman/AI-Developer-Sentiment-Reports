# AI Dev Sentiment Extraction — Lessons Learned

**Source run:** `extraction-weekly-2026-06-15-to-2026-06-22.jsonc`
**Engine / Config at run time:** v1.5.4 / v1.8
**Recorded:** 2026-06-22
**LLM Target:** Claude

This document captures durable lessons from the 2026-06-22 weekly run that should feed the next config / engine revision. Each lesson is paired with the concrete change that operationalizes it.

The two highest-leverage changes for next week specifically are **L1** (retrieval-method column with browser-direct default for Bluesky/Mastodon) and **L5** (post-level URL capture). Without those, dedup and audit get harder every week.

---

## Procedural / config changes

### L1. Demote Bluesky/Mastodon from "web-search Tier 1" to "browser-direct Tier 1"

**Evidence.** Web-search path returned zero in-window Bluesky/Mastodon items across three LLMs (Claude/WebSearch, ChatGPT browsing, Gemini Google grounding). Direct `bsky.app/profile/{handle}` navigation returned 13 in-window posts from four handles in a single pass. Same retrieval-failure shape as Flipboard's v1.8 demotion — the gap is search-engine indexing, not absent content.

**Change for config v1.9.** Add a `retrieval_method` column to the Platform Tier Assignments table with values `web-search | browser-direct | api | manual`. Tier assignment without a retrieval-method assignment is incomplete — current schema is a bug.

Suggested initial mapping for Claude as LLM Target:

| Platform | Tier | Retrieval Method |
| :---- | :---- | :---- |
| Reddit | Tier 1 | browser-direct (ChatGPT-mediated acceptable) |
| Hacker News | Tier 1 | web-search |
| Blogs / Publications | Tier 1 | web-search |
| Bluesky | Tier 1 | **browser-direct** |
| Mastodon | Tier 1 | **browser-direct** |
| X/Twitter | Tier 2 | Grok-mediated (firehose) |
| YouTube | Tier 1.5 | browser-direct + Gemini-grounded (cross-verified) |
| LinkedIn | Tier 3 Manual | manual |
| Podcasts | Tier 2 | manual |
| Flipboard | Tier 3 Manual | `flipboard-extraction` skill (browser-direct) |

### L2. Curate and version a known-good handle list per platform

**Evidence.** `krzysztofcieslak.bsky.social` (named in config v1.6) loaded an empty profile this run — handle was likely renamed or made private. Meanwhile, `gergely.pragmaticengineer.com` and `mitsuhiko.at` were the highest-signal Bluesky producers and weren't in the config at all.

**Change for config v1.9.** Add a "Known-Good Handles" appendix per platform, treated as data with a changelog. Initial Bluesky list validated this run:

- `simonwillison.net` (47.7K followers, in-window: heavy)
- `gergely.pragmaticengineer.com` (40.3K, in-window: heavy)
- `mitsuhiko.at` (44.4K, in-window: medium)
- `kelseyhightower.com` (101.4K, in-window: light/off-topic this week)
- ~~`krzysztofcieslak.bsky.social`~~ — REMOVE (profile not loading)
- ADD: `mariozechner.at`, Thorsten Ball (handle TBC) — observed as repost chain anchors

Same pattern for Mastodon (`simon@simonwillison.net` validated; build out next week).

### L3. Make Reddit retrieval ChatGPT-mediated by default for Claude

**Evidence.** Three runs in (E1, E2, this run), Claude still cannot retrieve via `site:reddit.com` or the v1.6 fallback queries. ChatGPT-with-browsing recovered 15 in-window items in 2m 9s of "thinking". Old.reddit.com direct navigation also works in browser.

**Change for config v1.9.** Replace the Reddit Platform Query Block's "Reddit (Fallback)" subsection with a procedural directive: "For LLM Target = Claude, route Reddit queries through ChatGPT-with-browsing via Claude in Chrome, OR direct-navigate to `old.reddit.com/r/<sub>/new` and read with `get_page_text`." Keep the query list as inputs to whichever path; drop the pretense that `site:` works.

### L4. Tighten time-window discipline at emit time

**Evidence.** This run softened — PocketOS (April 2026), Stack Overflow Feb 2026 survey, Pragmatic Engineer reader survey (date undated but pre-window), Cursor v1.6 history — all crept into Tier 1 blogs/publications because they kept showing up in search results and corroborated in-window patterns. They belong in `gaps.below_threshold` as supporting context, not as Tier 1 items.

**Change for engine v1.5.5.** Add a hard pre-emit validation rule (sibling to the existing v1.5.1–v1.5.4 guard clauses):

```
For every item in tier1.*, tier1_5.*, tier2.*:
  require date_field is present
  require ISO_8601(date_field) ∈ [since, today]
  if not, move to gaps.below_threshold with reason="outside-window-corroborating-evidence"
```

This is a class of bug identical to V-12/V-13/V-16/V-17 — silent type/range looseness becoming standard practice.

---

## Data-quality changes

### L5. Post-level URLs are required; `get_page_text` returns handle-level URLs

**Evidence.** All 13 Bluesky entries in this run share their profile URL because `get_page_text` strips per-post permalinks. Without post-level URLs, dedup is impossible across weeks and the v1.5.4 anti-fabrication rule ("only include retrieved URLs") is technically violated — the URLs we have aren't the post URLs.

**Change for engine / runbook.** Add Pass 3.1 to the procedure: after `get_page_text` identifies posts of interest, use `read_page` with element refs to extract the actual permalinks from the post-card DOM nodes, OR scroll/click through to capture them. Required field for `tier1.primary_social[].url`. Without this, Bluesky/Mastodon entries should carry a `_url_quality: "handle-only"` flag.

### L6. Date encoding must be ISO 8601, not "1d ago"

**Evidence.** Bluesky/Mastodon display relative dates ("1d", "2d", "5d", "1mo"). `get_page_text` strips the ISO date that lives in the hover-title attribute. I computed dates by subtracting from "today is 2026-06-22" — fine for one run, drift-prone over time and unverifiable in audit.

**Change for engine / runbook.** Use `read_page` with depth-scoped queries to grab the post-card's `title` attribute (which holds the full ISO timestamp on Bluesky), or document the relative-to-ISO computation as an explicit rule the runbook step must perform with the run's "today" date.

### L7. Engagement schema is inconsistent across sources — normalize per platform

**Evidence.** Grok emitted `~444 likes, 15 reposts, 50 replies`; Bluesky web view shows three bare numbers in the order **replies / reposts / likes** (note the order is non-obvious — easy to swap); ChatGPT formatted varied; HN uses points/comments instead of likes/reposts. The engine's `engagement: {likes, reposts, replies}` is the right canonical shape — but Pass 2/3 need source-specific normalizers.

**Change for config v1.9 / engine v1.5.5.** Add a per-platform engagement-mapping table to the engine's JSONC-Specific Field Rules:

| Source | Surface order | Canonical mapping |
| :---- | :---- | :---- |
| Bluesky (web) | replies / reposts / likes | `{replies, reposts, likes}` |
| X/Twitter | likes / reposts / replies | `{likes, reposts, replies}` |
| Mastodon | replies / boosts / favourites | `{replies, reposts: boosts, likes: favourites}` |
| Reddit | upvotes / comments | `{likes: upvotes, replies: comments, reposts: 0}` |
| Hacker News | points / comments | `{likes: points, replies: comments, reposts: 0}` |

---

## Anti-fabrication / verification

### L8. Cross-LLM items need an explicit verification step before promotion to Tier 1

**Evidence.** Gemini's Choice A response produced clearly hallucinated URLs (reddit.com URLs labeled as YouTube videos). Choice B's two Theo t3.gg URLs (`XYYZM01P2S0`, `EXeCOsIu0Ps`) are still URL-unverified and they currently anchor an emerging pattern (L9).

**Change for engine v1.5.5.** Items sourced from secondary LLMs already carry a `_via` field — extend with `_verified: bool`. Rule:

```
For every item with _via != null:
  require either _verified == true (Pass 3 click-through confirmation)
  or item lands in tier3_flags with reason="cross-LLM-unverified"
```

Items can be promoted from `tier3_flags` to their proper tier on a subsequent run after verification.

### L9. Soft-confidence patterns can't anchor an emerging pattern

**Evidence.** The "IDE death / Agent Experience" emerging pattern emitted in this run includes the two unverified Theo URLs as 2 of its 4 sources. If those URLs don't verify, the pattern drops to 2 sources, sits right at the L→M confidence boundary, and may be below threshold.

**Change for engine v1.5.5.** Add rule to `emerging_patterns[]`:

```
For every emerging_patterns entry:
  require at least 2 sources where _verified == true
  if not, downgrade confidence by one step OR move to gaps.below_threshold
```

---

## Engine / output schema changes

### L10. `tier1.primary_social[]` is under-specified — define it per LLM Target

**Evidence.** For Claude, the Platform Tier Assignments table puts Reddit, HN, Bluesky, Mastodon, and Blogs all at Tier 1. The output schema has dedicated keys `reddit[]`, `hacker_news[]`, `blogs_publications[]` — leaving "primary social" as "the leftover Tier-1 platforms with no key". I treated Bluesky/Mastodon as primary by exclusion, but that's not a defined rule.

**Change for config v1.9.** Add a `primary_social_platform` row to the Platform Tier Assignments table:

| LLM Target | Primary Social Platform(s) |
| :---- | :---- |
| Grok | X/Twitter |
| Claude | Bluesky + Mastodon |
| ChatGPT | Bluesky + Mastodon |
| Gemini | (TBD — likely none until access verified) |

Engine v1.5.5 reads this row to know what to put in `tier1.primary_social[]` vs. the named keys.

### L11. `gap_fill_method` should be first-class structured data, not a free-text string

**Evidence.** I jammed three-pass narration into a single string field. That works for one report but makes cross-run analysis impossible — which retrieval path yielded the most signal? Which platform-method pair has highest ROI?

**Change for engine v1.5.5.** Replace `report_metadata.gap_fill_method: string` with:

```jsonc
"passes": [
  {
    "number": 1,
    "method": "WebSearch",
    "platforms_attempted": ["hacker_news", "blogs_publications", "reddit"],
    "platforms_recovered": ["hacker_news", "blogs_publications"],
    "items_added": 17,
    "notes": "..."
  },
  {
    "number": 2,
    "method": "cross-LLM (Grok/ChatGPT/Gemini) via Claude in Chrome",
    "platforms_attempted": ["x_twitter", "reddit", "youtube"],
    "platforms_recovered": ["x_twitter", "reddit", "youtube"],
    "items_added": 23,
    "notes": "..."
  },
  {
    "number": 3,
    "method": "direct browser navigation",
    "platforms_attempted": ["bluesky", "mastodon"],
    "platforms_recovered": ["bluesky", "mastodon"],
    "items_added": 13,
    "notes": "..."
  }
]
```

This is the cleanest path to data-driven retrieval-method assignment for L1 — after a few weeks of this data, the per-platform optimal method becomes a number, not a guess.

---

## Out-of-scope but worth flagging

- **L?: Engine's "primary social platform status" field is binary (Working/Degraded/Failed)** — but the reality is per-method. This run had web-search "Failed" for Bluesky but browser-direct "Working" — and the field can only carry one value. Subordinate to L11.
- **L?: The Grok run used "Fast" mode** — could request deeper research mode for higher recall on X. Worth experimenting once.
- **L?: Krzysztof Cieslak handle removal needs cross-reference** — config v1.6 cites him as an E1 success ("ChatGPT retrieved 3 items including Krzysztof Cieslak") — that historical evidence should be preserved even as the handle is dropped from the active list.

---

## Implementation order for next week

1. **Apply L1 + L2 first** (config v1.9 retrieval-method + curated handles) — these change behavior on Monday's run with no engine code change.
2. **Apply L5 + L6 in the runbook** — instruct the next-week extractor to run Pass 3.1 for post-URLs and ISO dates.
3. **Apply L4 hard pre-emit check** — engine v1.5.5 patch — prevents the v1.5.4 class of "schema-shape soft drift" bug.
4. **Apply L8 + L9 verification flags** — engine v1.5.5 patch — closes anti-fabrication loophole around cross-LLM items.
5. **L11 (passes[] schema) is the biggest engine change** — defer to engine v1.6.0 if v1.5.5 is meant to be a patch release.

---

## Changelog

- **2026-06-22**: Initial capture from weekly run. Eleven lessons.
