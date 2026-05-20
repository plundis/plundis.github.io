#!/usr/bin/env python3
"""
Apply option-C termlog feature to your index.html.
Run:    python3 apply_termlog.py index.html
Output: index_patched.html   (your original is NOT modified)
"""
import sys, re

src = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
dst = src.replace('.html', '_patched.html')
html = open(src, encoding='utf-8').read()
ok = []

# PATCH 1: CSS - termlog styles before </style>
TERMLOG_CSS = """
  /* Option C: terminal log bio */
  .termlog{margin:12px 0 4px;border:1px solid var(--phos-deep);background:#080e0a;color:var(--paper);padding:10px 12px;font-family:var(--mono);font-size:11.5px;line-height:1.5;white-space:nowrap;overflow-x:auto;box-shadow:inset 0 0 24px rgba(124,245,138,.04);}
  .termlog .tl-line{display:block;}
  .termlog .tl-p  {color:var(--phos);margin-right:6px;}
  .termlog .tl-k  {color:var(--amber);letter-spacing:.1em;font-weight:600;display:inline-block;width:10ch;margin-right:8px;}
  .termlog .tl-at {color:var(--phos-dim);}
  .termlog .tl-hi {color:var(--phos);font-weight:700;text-shadow:0 0 6px rgba(124,245,138,.4);}
  .termlog a      {color:var(--paper);text-decoration:none;border-bottom:1px solid var(--phos-dim);}
  .termlog a:hover{border-bottom-color:var(--phos);color:#fff;}
  .termlog .tl-bar{color:var(--phos);letter-spacing:0;}
  .termlog .tl-dim{color:var(--phos-dim);font-size:10px;letter-spacing:.02em;display:block;padding-left:calc(10ch + 14px);margin-top:-1px;}
  .termlog .tl-sep{display:block;height:1px;background:rgba(124,245,138,.1);margin:6px 0;}
"""
html = html.replace('</style>', TERMLOG_CSS + '</style>', 1)
ok.append('CSS termlog styles')

# PATCH 2: CSS mobile overrides - append inside existing @media(max-width:900px)
OLD_MOB = '    .exp-top{padding-right:18px;}\n  }'
NEW_MOB = ('    .exp-top{padding-right:18px;}\n'
           '    .termlog{font-size:10.5px;padding:8px 10px;}\n'
           '    .termlog .tl-k{width:9ch;margin-right:6px;}\n'
           '    .termlog .tl-dim{padding-left:calc(9ch + 12px);}\n'
           '  }')
if OLD_MOB in html:
    html = html.replace(OLD_MOB, NEW_MOB, 1)
    ok.append('CSS mobile overrides')
else:
    print('WARN: mobile anchor not found - add termlog mobile rules manually')

# PATCH 3: HTML - replace .blurb with termlog div
TERMLOG_HTML = (
    '              <!-- Option C: terminal log -->\n'
    '              <div class="termlog" aria-label="Current status">'
    '<span class="tl-line"><span class="tl-p">&gt;</span><span class="tl-k">CURRENT</span>'
    'Research intern <span class="tl-at">@</span> '
    '<a href="https://www.lzh.de/en" target="_blank" rel="noopener">Laser Zentrum Hannover</a>'
    ' \u00b7 Hannover, DE</span>'
    '<span class="tl-line"><span class="tl-p">&gt;</span><span class="tl-k">MISSION</span>'
    '<span class="tl-hi">Moonrise</span> \u2014 ground-station comms for a lunar lander</span>'
    '<span class="tl-line"><span class="tl-p">&gt;</span><span class="tl-k">SHIPPING</span>'
    'YAMCS pipeline \u00b7 CCSDS/SLIP over RS-422 \u00b7 image downlink</span>'
    '<span class="tl-sep"></span>'
    '<span class="tl-line"><span class="tl-p">&gt;</span><span class="tl-k">RESIDENCY</span>'
    '<span class="tl-bar" data-termlog="bar">[\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7]</span>'
    '  <span data-termlog="day">day \u2026/\u2026</span></span>'
    '<span class="tl-dim">JAN 05 \u2014\u2014\u2192 JUL 31 2026 \u00b7 '
    '<span data-termlog="pct">\u2026</span>% complete</span>'
    '<span class="tl-sep"></span>'
    '<span class="tl-line"><span class="tl-p">&gt;</span><span class="tl-k">NEXT</span>'
    'UBC \u00b7 final year EE \u00b7 Fall 2026 \u2192 Spring 2027</span></div>'
)
blurb_pat = r'<p class="blurb".*?</p>'
if re.search(blurb_pat, html):
    html = re.sub(blurb_pat, TERMLOG_HTML, html, count=1)
    ok.append('HTML termlog replaces blurb')
else:
    print('WARN: .blurb paragraph not found - insert termlog HTML manually')

# PATCH 4: JS - add residency IIFE before TICKER
# Your file has a function named tick() inside the ticker block already,
# so this uses an anonymous IIFE to avoid any name collision.
BAR_CHAR = '\u2588'
DOT_CHAR = '\u00b7'
RESIDENCY_JS = (
    '  // residency progress (Jan 5 to Jul 31 2026)\n'
    '  (function(){\n'
    '    var S=new Date(2026,0,5),E=new Date(2026,6,31),W=20,now=new Date();\n'
    '    var total=Math.round((E-S)/86400000);\n'
    '    var dayN=Math.max(0,Math.min(total,Math.round((now-S)/86400000)));\n'
    '    var pct=Math.round((dayN/total)*100);\n'
    '    var filled=Math.round((pct/100)*W);\n'
    "    var bar='['+'" + BAR_CHAR + "'.repeat(filled)+'" + DOT_CHAR + "'.repeat(W-filled)+']';\n"
    '    document.querySelectorAll(\'[data-termlog="bar"]\').forEach(function(el){el.textContent=bar;});\n'
    '    document.querySelectorAll(\'[data-termlog="day"]\').forEach(function(el){el.textContent=\'day \'+dayN+\'/\'+total;});\n'
    '    document.querySelectorAll(\'[data-termlog="pct"]\').forEach(function(el){el.textContent=pct;});\n'
    '  })();\n\n'
    '  '
)
TICKER_ANCHOR = '  const TICKER = ['
if TICKER_ANCHOR in html:
    html = html.replace(TICKER_ANCHOR, RESIDENCY_JS + TICKER_ANCHOR, 1)
    ok.append('JS residency updater')
else:
    print('WARN: TICKER anchor not found - add residency IIFE just before: const TICKER = [')

open(dst, 'w', encoding='utf-8').write(html)
print('Patches applied:', ', '.join(ok))
print('Written to', dst)
