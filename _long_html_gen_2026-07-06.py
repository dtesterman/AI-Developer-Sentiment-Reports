#!/usr/bin/env python3
"""Generate longitudinal-summary-2026-07-06.html from MD via blue-accent template."""

import re
import sys
import subprocess
try:
    import markdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown", "--break-system-packages", "--quiet"])
    import markdown
from pathlib import Path

OUTDIR = Path('/sessions/nifty-intelligent-wright/mnt/local_754ac9df-27cd-4e02-8ee2-7d29ecd49486--outputs')
SRC_MD = OUTDIR / 'longitudinal-summary-2026-07-06.md'
DST_HTML = OUTDIR / 'longitudinal-summary-2026-07-06.html'
TEMPLATE_HTML = OUTDIR / 'longitudinal-summary-2026-06-29.html'

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


def extract_design_system():
    html = TEMPLATE_HTML.read_text(encoding='utf-8')
    m = re.search(r'^(<!DOCTYPE html>.*?</style>\s*</head>)', html, re.DOTALL)
    head = m.group(1) if m else ''
    m2 = re.search(r'(<script>.*?</script>\s*)?</body>', html, re.DOTALL)
    scripts = m2.group(1) if m2 and m2.group(1) else ''
    return head, scripts


def normalize_md_links(html_body):
    def fix(m):
        attrs = m.group(1); href = m.group(2)
        if href.startswith('#'):
            return m.group(0)
        return f'<a{attrs}href="{href}" target="_blank" rel="noopener">'
    return re.sub(r'<a([^>]*?)href="([^"]+)"[^>]*>', fix, html_body)


def add_section_anchors(html_body):
    h2_re = re.compile(r'<h2>(.*?)</h2>', re.DOTALL)
    h2_positions = [(m.start(), m.end(), m.group(1).strip()) for m in h2_re.finditer(html_body)]
    if not h2_positions:
        return html_body
    out = [html_body[:h2_positions[0][0]]]
    for idx, (start, end, title_html) in enumerate(h2_positions):
        plain = re.sub(r'<[^>]+>', '', title_html).strip().replace('&amp;', '&')
        sid = snum = None
        for canonical, mapped_id, mapped_num in SECTION_MAP:
            if canonical.lower() in plain.lower():
                sid, snum = mapped_id, mapped_num
                break
        next_start = h2_positions[idx + 1][0] if idx + 1 < len(h2_positions) else len(html_body)
        inner = html_body[end:next_start]
        if sid:
            out.append(f'<section id="{sid}"><h2 data-section="{snum}">{title_html}</h2>')
        else:
            out.append(f'<section><h2>{title_html}</h2>')
        out.append(inner)
        out.append('</section>')
    return ''.join(out)


def render_nav():
    items = ''.join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV_ITEMS)
    return f'<nav><h1>Longitudinal Trend Report</h1><ul>{items}</ul></nav>'


def build_masthead():
    return '''<header>
<h1 class="title">Longitudinal Trend Report<br>AI Coding Tools &mdash; Extractions 1 &ndash; 16</h1>
<div class="subtitle">2026-03-20 &ndash; 2026-07-06 &nbsp;&middot;&nbsp; 101 days &nbsp;&middot;&nbsp; 16 weekly windows<br>Generated 2026-07-06 from analysis-summary-{date}.md files (--from-summaries mode)</div>
<div class="masthead-stats">
<div class="stat-item"><div class="stat-label">Extractions</div><div class="stat-value">16</div></div>
<div class="stat-item"><div class="stat-label">Items Tagged</div><div class="stat-value">~795</div></div>
<div class="stat-item"><div class="stat-label">Tracked Signals</div><div class="stat-value">30</div></div>
<div class="stat-item"><div class="stat-label">Promoted Signals</div><div class="stat-value">10</div></div>
<div class="stat-item"><div class="stat-label">NEW E16</div><div class="stat-value">6</div></div>
<div class="stat-item"><div class="stat-label">Confirmed Trends</div><div class="stat-value">5</div></div>
</div>
</header>'''


def main():
    head, scripts = extract_design_system()
    md_text = SRC_MD.read_text(encoding='utf-8')
    body = markdown.markdown(md_text, extensions=['extra', 'tables', 'sane_lists'], output_format='html5')
    body = re.sub(r'<h1>.*?</h1>', '', body, count=1, flags=re.DOTALL)
    body = normalize_md_links(body)
    body = add_section_anchors(body)
    body = re.sub(r'<hr\s*/?>', '', body)
    nav = render_nav()
    masthead = build_masthead()
    footer = '''<footer style="margin-top:4rem;padding-top:2rem;border-top:1px solid #2a3441;text-align:center;color:#7a8694;font-family:'JetBrains Mono',monospace;font-size:0.78rem;">
<p>Longitudinal Trend Report &mdash; Extractions 1 &ndash; 16 &mdash; Generated 2026-07-06</p>
<p>Longitudinal Engine v1.3 &middot; Domain Config v1.2 &middot; Bootloader v1.9 &middot; HTML Engine v1.2 (blue accent)</p>
</footer>'''
    head = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Longitudinal Trend Report — AI Coding Tools E1 - E16 (2026-03-20 to 2026-07-06). 16 weekly windows; ~795 tagged items; 30 tracked signals. E16 mints six new signals — export-control-regime, investor-as-regulator, open-weight-china-advantage, eval-cheating-frontier, tiered-model-strategy, control-vs-autonomy-split — program-record mint count.">',
        head,
    )
    head = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        '<meta property="og:title" content="Longitudinal Trend Report — E1 - E16 (2026-03-20 to 2026-07-06)">',
        head,
    )
    head = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        '<meta property="og:description" content="16 windows; export-control regime over frontier coding models becomes regime change, not anomaly; Amazon CEO triggered the crackdown; six new signals mint in a single window.">',
        head,
    )
    head = re.sub(
        r'<title>.*?</title>',
        '<title>Longitudinal Trend Report — E1 - E16 (2026-03-20 to 2026-07-06)</title>',
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
    DST_HTML.write_text(html, encoding='utf-8')
    print(f"Wrote {DST_HTML} ({len(html):,} bytes)")


if __name__ == '__main__':
    main()
