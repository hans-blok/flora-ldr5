import re

with open(r'c:\git\flora\artefacten\schets-kaart\schets-kaart\schets-kaart.SVG', encoding='utf-8') as f:
    svg = f.read()

# Find all text elements (multi-attr order variants)
pattern = r'<text([^>]*)>([^<]*)</text>'
matches = re.findall(pattern, svg)

print('x, y, label:')
for attrs, content in matches:
    content = content.strip()
    if not content:
        continue
    mx = re.search(r'x="([^"]+)"', attrs)
    my = re.search(r'y="([^"]+)"', attrs)
    x = mx.group(1) if mx else '?'
    y = my.group(1) if my else '?'
    print(f'  x={x:>10}  y={y:>10}  {repr(content)}')
