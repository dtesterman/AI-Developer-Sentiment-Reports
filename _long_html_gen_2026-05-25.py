#!/usr/bin/env python3
"""Generate longitudinal-summary-2026-05-25.html from the markdown report.

Reuses the blue-accent design system from longitudinal-summary-2026-05-18.html.
"""

import re
import markdown
from pathlib import Path

OUTDIR = Path('/sessions/gracious-optimistic-davinci/mnt/local_754ac9df-27cd-4e02-8ee2-7d29ecd49486--outputs')
SRC_MD = OUTDIR / 'longitudinal-summary-2026-05-25.md'
TEMPLATE_HTML = OUTDIR / 'longitudinal-summary-2026-05-18.html'

NAV_ITEMS = [
    ("#summary", "01 Summary"),
    ("#composition", "02 Composition"),
    ("#trajectory", "03 Trajectory"),
    ("#momentum", "04 Momentum"),
    ("#signals", "05 Signals"),
    ("#contradictions", "06 Contradictions"),
    ("#vocabulary", "07 Vocabulary"),
    ("#gaps", "08 Gaps"),
    ("#watch", "09 Watch List"),
    ("#metadata", "10 Metadata"),
]

SECTION_MAP = [
    ("Executive Summary", "summary", "01"),
    ("Source Composition Audit", "composition", "02"),
    ("Sentiment Trajectory", "trajectory", "03"),
    ("Cluster Momentum", "momentum", "04"),
    ("Signal Evolution", "signals", "05"),
    ("Cross-Extraction Contradictions", "contradictions", "06"),
    ("Vocabulary & Framing Drift", "vocabulary", "07"),
    ("Gaps & Uncertainties", "gaps", "08"),
    ("Watch List for Next Extraction", "watch", "09"),
    ("Longitudinal Report Metadata", "metadata", "10"),
]


def extract_design_system() -> tuple[str, str]:
    html = TEMPLATE_HTML.read_text(encoding='utf-8')
    m = re.search(r'^(<!DOCTYPE html>.*?</style>\s*</head>)', html, re.DOTALL)
    head = m.group(1) if m else ''
    m2 = re.search(r'(<script>.*?</script>\s*)?</body>', html, re.DOTALL)
    scripts = m2.group(1) if m2 and m2.group(1) else ''
    return head, scripts


def normalize_md_links(html_body: str) -> str:
    def fix(m):
        attrs = m.group(1)
        href = m.group(2)
        if href.startswith('#'):
            return m.group(0)
        return f'<a{attrs}href="{href}" target="_blank" rel="noopener">'
    return re.sub(r'<a([^>]*?)href="([^"]+)"[^>]*>', fix, html_body)


def add_section_anchors(html_body: str) -> str:
    h2_re = re.compile(r'<h2>(.*?)</h2>', re.DOTALL)
    h2_positions = [(m.start(), m.end(), m.group(1).strip()) for m in h2_re.finditer(html_body)]
    if not h2_positions:
        return html_body

    out_parts = []
    out_parts.append(html_body[:h2_positions[0][0]])
    for idx, (start, end, title_html) in enumerate(h2_positions):
        plain_title = re.sub(r'<[^>]+>', '', title_html).strip()
        plain_title = plain_title.replace('&amp;', '&')
        sid, snum = None, None
        for canonical, mapped_id, mapped_num in SECTION_MAP:
            if canonical.lower() in plain_title.lower():
                sid, snum = mapped_id, mapped_num
                break
        next_start = h2_positions[idx + 1][0] if idx + 1 < len(h2_positions) else len(html_body)
        section_inner = html_body[end:next_start]
        if sid:
            out_parts.append(f'<section id="{sid}"><h2 data-section="{snum}">{title_html}</h2>')
        else:
            out_parts.append(f'<section><h2>{title_html}</h2>')
        out_parts.append(section_inner)
        out_parts.append('</section>')
    return ''.join(out_parts)


def render_nav() -> str:
    items = ''.join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV_ITEMS)
    return f'<nav><h1>Longitudinal Trend Report</h1><ul>{items}</ul></nav>'


def build_masthead() -> str:
    return '''<header>
<h1 class="title">Longitudinal Trend Report<br>AI Coding Tools — Extractions 1 – 11</h1>
<div class="subtitle">2026-03-20 &ndash; 2026-05-25 &nbsp;&middot;&nbsp; 66 days &nbsp;&middot;&nbsp; 11 weekly windows<br>Generated 2026-05-25 from analysis-summary-{date}.md files (--from-summaries mode)</div>
<div class="masthead-stats">
<div class="stat-item"><div class="stat-label">Extractions</div><div class="stat-value">11</div></div>
<div class="stat-item"><div class="stat-label">Items Tagged</div><div class="stat-value">548</div></div>
<div class="stat-item"><div class="stat-label">Tracked Signals</div><div class="stat-value">25</div></div>
<div class="stat-item"><div class="stat-label">Promoted Signals</div><div class="stat-value">10</div></div>
<div class="stat-item"><div class="stat-label">NEW E11</div><div class="stat-value">2</div></div>
<div class="stat-item"><div class="stat-label">Promotion Candidates</div><div class="stat-value">3</div></div>
</div>
</header>'''


def main():
    head, scripts = extract_design_system()
    md_text = SRC_MD.read_text(encoding='utf-8')

    body = markdown.markdown(
        md_text,
        extensions=['extra', 'tables', 'sane_lists'],
        output_format='html5',
    )
    body = re.sub(r'<h1>.*?</h1>', '', body, count=1, flags=re.DOTALL)
    body = normalize_md_links(body)
    body = add_section_anchors(body)
    body = re.sub(r'<hr\s*/?>', '', body)

    nav = render_nav()
    masthead = build_masthead()

    footer = '''<footer style="margin-top:4rem;padding-top:2rem;border-top:1px solid #2a3441;text-align:center;color:#7a8694;font-family:'JetBrains Mono',monospace;font-size:0.78rem;">
<p>Longitudinal Trend Report &mdash; Extractions 1 &ndash; 11 &mdash; Generated 2026-05-25</p>
<p>Longitudinal Engine v1.3 &middot; Domain Config v1.2 &middot; Bootloader v1.9 &middot; HTML Engine v1.2 (blue accent)</p>
</footer>'''

    head = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Longitudinal Trend Report &mdash; AI Coding Tools E1 - E11 (2026-03-20 to 2026-05-25). 11 weekly windows; 548 tagged items; 25 tracked signals (10 Promoted, 12 Tracking, 3 retire-or-merge candidates). E11 adds review-cost-inversion + agent-infrastructure-inflection; junior-pipeline-collapse reaches promotion threshold.">',
        head,
    )
    head = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        '<meta property="og:title" content="Longitudinal Trend Report &mdash; E1 - E11 (2026-03-20 to 2026-05-25)">',
        head,
    )
    head = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        '<meta property="og:description" content="11 windows; review-cost-inversion crystallizes; junior-pipeline-collapse meets promotion threshold; mcp-attack-surface graduates production-confirmed pending second source.">',
        head,
    )
    head = re.sub(
        r'<title>.*?</title>',
        '<title>Longitudinal Trend Report &mdash; E1 - E11 (2026-03-20 to 2026-05-25)</title>',
        head,
    )

    html = f'''{head}
<body>
{nav}
<div class="container">
{masthead}
{body}
{footer}
</div>
{scripts}
</body>
</html>'''

    tmp = Path('/tmp/longitudinal-summary-2026-05-25.html')
    tmp.write_text(html, encoding='utf-8')
    print(f"Wrote {tmp} ({len(html):,} bytes)")


if __name__ == '__main__':
    main()
