# Reddit Reconnaissance Script
## Window: 2026-04-27 to 2026-05-04 (Mon–Mon)
## For: AI Dev Sentiment Extraction (extraction-weekly-2026-04-27-to-2026-05-04.jsonc)

This script asks you to pull a small amount of data per post (title, URL, upvotes, comment count, top-comment gist) so the items can be lifted directly into the JSONC report's `tier1.reddit[]` array. Reddit's "top this week" approximation matches our 7-day window today.

---

## Tier A — Highest-value subreddits (do these first)

For each of the URLs below: open it, glance at the top 5–10 posts, and copy back any post that's **about AI coding tools, agents, productivity, incidents, or hiring** (skip tool-update announcements, memes, and off-topic posts). For each kept post, paste:

- Subreddit (e.g., `r/ClaudeCode`)
- Title
- URL (the post's permalink)
- Upvotes
- Comment count
- Top comment's main point (one sentence is fine)
- Optional: tag the topic — quality, productivity, pricing, incident, burnout, hiring, deskilling, architecture

### 1. r/ClaudeCode (top this week)
https://www.reddit.com/r/ClaudeCode/top/?t=week

### 2. r/cursor (top this week)
https://www.reddit.com/r/cursor/top/?t=week

### 3. r/ExperiencedDevs (top this week)
https://www.reddit.com/r/ExperiencedDevs/top/?t=week

### 4. r/vibecoding (top this week)
https://www.reddit.com/r/vibecoding/top/?t=week

### 5. r/ClaudeAI (top this week)
https://www.reddit.com/r/ClaudeAI/top/?t=week

---

## Tier B — Secondary subreddits (do these if you have time)

### 6. r/cscareerquestions (top this week)
https://www.reddit.com/r/cscareerquestions/top/?t=week
*Filter for AI-coding hiring / junior-developer / entry-level threads only.*

### 7. r/programming (top this week)
https://www.reddit.com/r/programming/top/?t=week
*Filter for AI / Copilot / Cursor / Claude / vibe-coding / agent threads.*

### 8. r/devops (top this week)
https://www.reddit.com/r/devops/top/?t=week
*Filter for AI-coding incident, agent-in-pipeline, or AI-in-production threads.*

### 9. r/webdev (top this week)
https://www.reddit.com/r/webdev/top/?t=week
*Filter for AI-coding / Copilot / Cursor threads.*

### 10. r/softwarearchitecture (top this week)
https://www.reddit.com/r/softwarearchitecture/top/?t=week
*Filter for AI-code maintainability / architecture-with-agents threads.*

---

## Tier C — Targeted searches (do these only if a topic seems thin)

These use Reddit's search to surface posts referencing specific in-window news items.

### 11. PocketOS / Cursor database deletion incident
https://www.reddit.com/search/?q=PocketOS&t=week
https://www.reddit.com/search/?q=%22Cursor%22+%22deleted%22+%22database%22&t=week

### 12. Uber 2026 AI budget / Claude Code cost
https://www.reddit.com/search/?q=Uber+%22AI+budget%22+%22Claude+Code%22&t=week

### 13. Claude Code / OpenClaw refusal controversy
https://www.reddit.com/search/?q=%22Claude+Code%22+%22OpenClaw%22&t=week

### 14. Zig anti-AI contribution policy
https://www.reddit.com/search/?q=Zig+%22anti-AI%22&t=week

### 15. VS Code "Co-Authored-by Copilot" inserting itself
https://www.reddit.com/search/?q=%22Co-Authored-by+Copilot%22&t=week

### 16. MCP vulnerability / RCE / prompt injection
https://www.reddit.com/search/?q=MCP+vulnerability&t=week

### 17. Cognitive debt / ThoughtWorks Radar v34
https://www.reddit.com/search/?q=%22cognitive+debt%22+AI&t=week

### 18. Lovable data leak (April 20 incident, ongoing discussion)
https://www.reddit.com/search/?q=Lovable+%22data+leak%22&t=week

---

## What to paste back

You don't need to format anything — just paste raw. A reasonable shape per post:

```
SUBREDDIT: r/ClaudeCode
TITLE: <title text>
URL: https://www.reddit.com/r/ClaudeCode/comments/.../...
UPVOTES: 234
COMMENTS: 87
TOP COMMENT: <one-sentence gist>
TAGS: quality, pricing
```

…or just paste the raw post pages in plain text and I'll parse them. Anything you give me I can fold into `tier1.reddit[]` in the JSONC report.

---

## What to skip

- Tool-update / changelog announcement posts (we're tracking *sentiment*, not feature lists)
- Pure memes / image-only posts
- Posts where the only AI-coding mention is a tangent
- Anything older than 7 days (outside the window)
- Anything that looks like vendor self-promotion (low signal for the practitioner-discourse target)

---

## Stopping rule

Five to ten high-quality posts across Tier A is enough to materially fill the gap. If a subreddit returns nothing in-window or nothing AI-coding-related, just say "r/foo: nothing in window" and skip it.
