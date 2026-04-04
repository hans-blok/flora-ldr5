# Generates schets-kaart-zon-schaduw.svg:
# - Original map (1280x720) with unchanged content
# - Right panel (x=1292-1600) showing zon/schaduw per zone per dagdeel
# - Referentiedatum: 1 mei  ~  11 augustus (zelfde zondeclinatie ~+15 graden)
# Kleuren afgestemd op borders-zon-schaduw.md:
#   zon  = geel  #FFD700  (matches oranje-geel zonneschijn)
#   half = oranje #FFA040 (matches gedeeltelijke bewolking)
#   scha = donker #555555 (matches zwarte 🌑 in md)

SRC = r'c:\git\flora\artefacten\schets-kaart\schets-kaart\schets-kaart.SVG'
DST = r'c:\git\flora\artefacten\schets-kaart-zon-schaduw.svg'

# Zone data: (id, naam, ochtend 8-10u, middag 12-14u, namiddag 16-18u)
# Symbols: zon=U+2600  half=U+26C5  scha=U+25CF (zwarte cirkel, ~🌑)
ZON   = '\u2600'   # zon     -- geel
HALF  = '\u26C5'   # halve zon/wolk -- oranje
SCHA  = '\u25CF'   # zwarte cirkel (donker, ~🌑) -- donkergrijs

def em_color(sym):
    if sym == ZON:  return '#FFD700'   # geel
    if sym == HALF: return '#FFA040'   # oranje
    return '#555555'                   # donkergrijs

# Zones conform borders-zon-schaduw.md (incl. Z4* = PPTX-origineel zone 4)
zones = [
    ("Z1",  "W-zijde",    SCHA, HALF, ZON ),
    ("Z2",  "NW-gevel",   HALF, HALF, ZON ),
    ("Z3",  "NO-kant",    ZON,  HALF, SCHA),
    ("Z4*", "NO/O-mid",   ZON,  HALF, SCHA),  # PPTX zone 4, ontbrak in werkkaart
    ("Z4W", "O-kant",     ZON,  HALF, SCHA),  # werkkaart zone 4 (PPTX zone 5)
    ("Z5",  "ZO-kant",    ZON,  ZON,  HALF),
    ("Z6",  "Z/ZO",       ZON,  ZON,  ZON ),
    ("Z7",  "Z-kant",     HALF, ZON,  ZON ),
    ("Z8",  "Centrum",    SCHA, HALF, HALF),
    ("Z10", "NW-rand",    HALF, HALF, ZON ),
    ("Z11", "W-grens",    SCHA, HALF, ZON ),
    ("Z12", "Sloot",      HALF, HALF, ZON ),
]

PANEL_X  = 1292
ROW_H    = 50     # verkleind: 12 rijen x 50 + 95 header = 695px < 720px
HEADER_Y = 95
CX_OC    = 1410   # ochtend  col center x
CX_MI    = 1480   # middag   col center x
CX_NA    = 1550   # namiddag col center x

# ── build zone rows ──────────────────────────────────────────────────────────
rows = []
for i, (zid, zname, oc, mi, na) in enumerate(zones):
    y   = HEADER_Y + i * ROW_H
    bg  = "#EDF7E9" if i % 2 == 0 else "#FFFFFF"
    y_id   = y + 16
    y_name = y + 28
    y_em   = y + 38
    sep_y2 = y + ROW_H
    rows.append(f"""
  <rect x="{PANEL_X}" y="{y}" width="308" height="{ROW_H}" fill="{bg}"/>
  <line x1="{PANEL_X}" y1="{y}" x2="1600" y2="{y}" stroke="#DDDDDD" stroke-width="0.5"/>
  <text x="1296" y="{y_id}"   font-family="Aptos,sans-serif" font-size="11" font-weight="700" fill="#275317">{zid}</text>
  <text x="1296" y="{y_name}" font-family="Aptos,sans-serif" font-size="9"  fill="#666">{zname}</text>
  <line x1="1372" y1="{y}" x2="1372" y2="{sep_y2}" stroke="#DDDDDD" stroke-width="0.5"/>
  <text x="{CX_OC}" y="{y_em}" font-family="Aptos,sans-serif" font-size="18" text-anchor="middle" fill="{em_color(oc)}">{oc}</text>
  <line x1="1446" y1="{y}" x2="1446" y2="{sep_y2}" stroke="#DDDDDD" stroke-width="0.5"/>
  <text x="{CX_MI}" y="{y_em}" font-family="Aptos,sans-serif" font-size="18" text-anchor="middle" fill="{em_color(mi)}">{mi}</text>
  <line x1="1516" y1="{y}" x2="1516" y2="{sep_y2}" stroke="#DDDDDD" stroke-width="0.5"/>
  <text x="{CX_NA}" y="{y_em}" font-family="Aptos,sans-serif" font-size="18" text-anchor="middle" fill="{em_color(na)}">{na}</text>""")

# ── full panel ────────────────────────────────────────────────────────────────
panel = f"""<g id="zon-panel">
  <!-- achtergrond -->
  <rect x="{PANEL_X}" y="0" width="308" height="720" fill="#F9F9F9"/>
  <line x1="{PANEL_X}" y1="0" x2="{PANEL_X}" y2="720" stroke="#AAAAAA" stroke-width="2"/>

  <!-- titel -->
  <text x="1446" y="24" font-family="Aptos,sans-serif" font-size="14" font-weight="700" text-anchor="middle" fill="#1A3A1A">Zon per zone</text>
  <text x="1446" y="40" font-family="Aptos,sans-serif" font-size="11" text-anchor="middle" fill="#444">1 mei \u2248 11 augustus</text>
  <text x="1446" y="54" font-family="Aptos,sans-serif" font-size="9"  text-anchor="middle" fill="#888">(zelfde zondeclinatie \u224815\u00b0; aug \u223c30 min korter)</text>

  <!-- legenda -->
  <text x="1296" y="70" font-family="Aptos,sans-serif" font-size="10" fill="{em_color(ZON)}">{ZON} zon</text>
  <text x="1340" y="70" font-family="Aptos,sans-serif" font-size="10" fill="{em_color(HALF)}">{HALF} half</text>
  <text x="1395" y="70" font-family="Aptos,sans-serif" font-size="10" fill="{em_color(SCHA)}">{SCHA} schaduw</text>
  <text x="1490" y="70" font-family="Aptos,sans-serif" font-size="8"  fill="#999">Z4*=PPTX orig</text>
  <line x1="{PANEL_X}" y1="76" x2="1600" y2="76" stroke="#CCCCCC" stroke-width="1"/>

  <!-- kolomkoppen -->
  <rect x="{PANEL_X}" y="77" width="308" height="18" fill="#275317"/>
  <text x="1296" y="90" font-family="Aptos,sans-serif" font-size="9" font-weight="700" fill="#FFFFFF">Zone</text>
  <text x="{CX_OC}" y="90" font-family="Aptos,sans-serif" font-size="9" font-weight="700" text-anchor="middle" fill="#FFFFFF">8\u201310u</text>
  <text x="{CX_MI}" y="90" font-family="Aptos,sans-serif" font-size="9" font-weight="700" text-anchor="middle" fill="#FFFFFF">12\u201314u</text>
  <text x="{CX_NA}" y="90" font-family="Aptos,sans-serif" font-size="9" font-weight="700" text-anchor="middle" fill="#FFFFFF">16\u201318u</text>
{"".join(rows)}
  <!-- onderrand -->
  <line x1="{PANEL_X}" y1="720" x2="1600" y2="720" stroke="#AAAAAA" stroke-width="1"/>
</g>"""

# ── patch SVG ─────────────────────────────────────────────────────────────────
with open(SRC, 'r', encoding='utf-8') as f:
    svg = f.read()

# expand canvas width
svg = svg.replace('width="1280" height="720"', 'width="1600" height="720"', 1)

# insert panel before </svg>
svg = svg.replace('</svg>', panel + '\n</svg>')

with open(DST, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"Geschreven: {DST}")
