import sys, re, subprocess
import os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(root, "src", "toolkit.html")
dst = os.path.join(root, "index.html")
s = open(src).read()
js = re.search(r'<script>(.*)</script>', s, re.S).group(1)
open(dst + '.check.js', 'w').write(js)
subprocess.run(['node', '--check', dst + '.check.js'], check=True)
data = js[js.index('const TABS'):js.index('const all =')]
cardfn = js[js.index('function card('):js.index('function render(')]
node = data + cardfn + r'''
process.stdout.write(TABS.map(t => `<section class="static-tab" id="static-${t.id}"><h2>${esc(t.name)}</h2><p class="intro">${esc(t.intro)}</p><p><strong>Typical gain:</strong> ${esc(t.gain)} (${esc(t.gainNote)})</p><p><strong>Where AI fits best:</strong> ${esc(t.fit)}</p><p><strong>Integration notes:</strong> ${esc(t.integrate)}</p><div class="cards">${t.tools.map(x => card({...x, tab:t}, false)).join("")}</div></section>`).join("\n"));
'''
html = subprocess.run(['node', '-e', node], capture_output=True, text=True, check=True).stdout
marker = '<div class="cards" id="cards"></div>'
assert marker in s
s = s.replace(marker, '<div class="cards" id="cards">' + html + '</div>')
s = s.replace('.empty{', '.static-tab{grid-column:1/-1;display:grid;gap:12px;margin-bottom:28px}.static-tab h2{font-size:1.6rem}\n.empty{')
head, body = s.split('</style>', 1)
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
 '<meta name="description" content="Catalogue of AI tools for each game production discipline, with strengths, weaknesses and evidence-graded efficiency gains.">\n'
 + head + '</style>\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
open(dst, 'w').write(out)
import os; os.remove(dst + '.check.js')
print(html.count('<article'), 'cards; Room 8 left:', len(re.findall(r'room ?8|heroic', out, re.I)))
