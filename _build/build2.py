#!/usr/bin/env python3

"""Portfolio with custom theme by project category."""
import html, os, math, shutil
from projects_data import NAME, GITHUB, EMAIL, LINKEDIN, PROJECTS

OUT = "site"
e = html.escape

THEME_OF = {
    "tiger-compiler": "compilation",
    "light-tracker": "hardware",
    "object-detection-gpu": "software",
    "deriscage-esp32": "systeme",
    "pcb-snake": "hardware",
    "cpu-monocycle": "architecture",
}

# ---------- Hero illustrations (decorative SVGs) ----------
def svg_compilation():
    nodes = {"root": (170, 34, "LetExp"), "decs": (80, 104, "Decs"), "body": (262, 104, "CallExp"),
             "ty": (36, 176, "TypeDec"), "fn": (124, 176, "FunDec"), "pr": (262, 176, "print_int"),
             "if": (124, 240, "IfExp"), "arg": (262, 240, "sum(l)")}
    edges = [("root", "decs"), ("root", "body"), ("decs", "ty"), ("decs", "fn"), ("body", "pr"), ("fn", "if"), ("pr", "arg")]
    out = []
    for a, b in edges:
        x1, y1, _ = nodes[a]; x2, y2, _ = nodes[b]
        out.append(f'<path d="M{x1} {y1+12} C{x1} {(y1+y2)/2}, {x2} {(y1+y2)/2}, {x2} {y2-12}" class="d-line"/>')
    for k, (x, y, t) in nodes.items():
        w = len(t) * 7.6 + 18
        out.append(f'<rect x="{x-w/2}" y="{y-12}" width="{w}" height="24" rx="3" class="d-node{" d-hl" if k=="root" else ""}"/>'
                   f'<text x="{x}" y="{y+4}" class="d-txt">{t}</text>')
    return f'<svg viewBox="0 0 320 270">{"".join(out)}</svg>'

def svg_hardware():
    return """<svg viewBox="0 0 320 270">
<g class="d-trace">
<path d="M0 60 H80 L110 90 H150"/><path d="M0 120 H60 L90 150 H150"/><path d="M0 200 H100 L130 170 H150"/>
<path d="M250 90 H280 L320 50"/><path d="M250 130 H320"/><path d="M250 170 H270 L310 210 V270"/>
<path d="M190 70 V30 L220 0"/><path d="M210 190 V240 L240 270"/>
</g>
<rect x="150" y="70" width="100" height="120" rx="4" class="d-chip"/>
<g class="d-pin">""" + "".join(f'<rect x="142" y="{82+i*16}" width="10" height="6"/><rect x="248" y="{82+i*16}" width="10" height="6"/>' for i in range(7)) + """</g>
<circle cx="163" cy="83" r="4" class="d-dot"/>
<text x="200" y="135" class="d-txt">MCU</text>
<g class="d-via"><circle cx="80" cy="60" r="6"/><circle cx="60" cy="120" r="6"/><circle cx="100" cy="200" r="6"/><circle cx="280" cy="90" r="6"/><circle cx="270" cy="170" r="6"/><circle cx="190" cy="30" r="6"/><circle cx="210" cy="240" r="6"/></g>
</svg>"""

def svg_software():
    cells = []
    for y in range(9):
        for x in range(12):
            v = 0.08 + 0.5 * (math.sin(x * 0.9 + y * 0.6) * 0.5 + 0.5) ** 3
            inside = 5 <= x <= 9 and 2 <= y <= 6
            if inside: v = 0.55 + 0.4 * ((x + y) % 3) / 3
            cells.append(f'<rect x="{10+x*25}" y="{18+y*25}" width="21" height="21" rx="4" class="d-px" style="opacity:{v:.2f}"/>')
    return f"""<svg viewBox="0 0 320 270">{''.join(cells)}
<rect x="131" y="64" width="128" height="128" rx="6" class="d-box"/>
<rect x="131" y="44" width="78" height="18" rx="4" class="d-tagbg"/><text x="170" y="57" class="d-txt">object</text></svg>"""

def wave(f, n=160, x0=0, w=320, y0=0, a=1):
    pts = [f"{x0 + i*w/n:.1f},{y0 + a*f(i/n):.1f}" for i in range(n + 1)]
    return "M" + " L".join(pts)

def svg_systeme():
    grid = "".join(f'<path d="M{x} 0 V270" class="d-grid"/>' for x in range(0, 321, 40)) + \
           "".join(f'<path d="M0 {y} H320" class="d-grid"/>' for y in range(15, 271, 40))
    def acc(t):  # no walking steps: impulses + noise
        return -math.exp(-((t * 4 % 1) - .35) ** 2 * 60) * 38 + math.sin(t * 90) * 2.5
    def vel(t):
        p = t * 4 % 1
        return -(28 * math.sin(math.pi * min(p / .6, 1))) if p < .6 else 0
    return f"""<svg viewBox="0 0 320 270">{grid}
<path d="M160 0 V270 M0 135 H320" class="d-axis"/>
<path d="{wave(acc, y0=95)}" class="d-ch1"/>
<path d="{wave(vel, y0=215)}" class="d-ch2"/>
<text x="8" y="30" class="d-txt d-c1">CH1 a_z</text><text x="8" y="160" class="d-txt d-c2">CH2 v · ZUPT</text></svg>"""

def svg_architecture():
    clk = "M10 40 " + " ".join(f"H{30+i*40} V15 H{50+i*40} V40" for i in range(7)) + " H310"
    def bus(y, labels):
        s = []
        for i, l in enumerate(labels):
            x = 10 + i * 80
            s.append(f'<path d="M{x} {y} L{x+6} {y-12} H{x+74} L{x+80} {y} L{x+74} {y+12} H{x+6} Z" class="d-bus"/>'
                     f'<text x="{x+40}" y="{y+4}" class="d-txt">{l}</text>')
        return "".join(s)
    return f"""<svg viewBox="0 0 320 270">
<text x="10" y="8" class="d-lbl">CLK</text><path d="{clk}" class="d-wave"/>
<text x="10" y="72" class="d-lbl">PC</text>{bus(95, ["0x00", "0x04", "0x08", "0x0C"])}
<text x="10" y="137" class="d-lbl">INSTR</text>{bus(160, ["ADD", "LDR", "SUB", "BEQ"])}
<text x="10" y="202" class="d-lbl">WE</text><path d="M10 250 H90 V225 H170 V250 H250 V225 H310" class="d-wave d-w2"/>
</svg>"""

THEMES = {
    "compilation": dict(label="Compilation", font="family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@400;500;600",
                        svg=svg_compilation, mark="//"),
    "hardware": dict(label="Hardware", font="family=Chakra+Petch:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600",
                     svg=svg_hardware, mark="◎"),
    "software": dict(label="Software", font="family=Sora:wght@400;600;700&family=Inter:wght@400;500;600",
                     svg=svg_software, mark="▸"),
    "systeme": dict(label="Système", font="family=Share+Tech+Mono&family=IBM+Plex+Sans:wght@400;500;600",
                    svg=svg_systeme, mark="›"),
    "architecture": dict(label="Architecture", font="family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600",
                         svg=svg_architecture, mark="■"),
}
BASE_FONT = "family=IBM+Plex+Sans:wght@400;500;600;700"
ALL_FONTS = "family=JetBrains+Mono:wght@400;500;700&family=Chakra+Petch:wght@600;700&family=Sora:wght@600;700&family=Share+Tech+Mono&family=Space+Grotesk:wght@600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600"

def head(title, desc, depth, fonts, body_class=""):
    p = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fonts}&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%23101318'/><text x='16' y='22' font-family='monospace' font-size='16' font-weight='700' fill='%23ffb547' text-anchor='middle'>JG</text></svg>">
</head>
<body class="{body_class}">
"""

def nav(depth):
    p = "../" * depth
    return f"""<header class="topbar">
  <a class="logo" href="{p}index.html"><span class="logo-mark">JG</span><span class="logo-text">{e(NAME)}</span></a>
  <nav>
    <a href="{p}index.html#projets">Projets</a>
    <a href="{p}index.html#apropos">À propos</a>
    <a href="{p}index.html#contact">Contact</a>
    <a class="btn-gh" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a>
  </nav>
</header>
"""

def footer(extra=""):
    return f"""<footer class="footer">
  <div class="wrap footer-in">
    <span>© 2026 {e(NAME)}</span>
    <span class="mono dim">Fait main · hébergé sur GitHub Pages</span>
  </div>
</footer>
{extra}</body>
</html>
"""

def tags(ts):
    return "".join(f'<span class="tag">{e(t)}</span>' for t in ts)

def sec(title):
    return f'<h2 class="h-sec"><span class="sec-mark"></span>{e(title)}</h2>'

def project_page(i, p):
    th = THEME_OF[p["slug"]]; T = THEMES[th]
    prev_p = PROJECTS[i - 1]; next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    steps = "".join(f'<li><span class="step-n">{k+1:02d}</span>{e(s)}</li>' for k, s in enumerate(p["pipeline"]))
    points = "".join(f'<div class="point"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in p["points"])
    facts = "".join(f'<div class="fact"><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in p["facts"])
    learned = "".join(f"<li>{e(l)}</li>" for l in p["learned"])
    return head(f'{p["title"]} — {NAME}', p["tagline"], 1, T["font"], f"theme-{th}") + nav(1) + f"""
<main>
  <section class="p-hero wrap">
    <a class="back mono" href="../index.html#projets">← Tous les projets</a>
    <div class="p-hero-grid">
      <div class="p-hero-main">
        <p class="eyebrow"><span class="theme-badge">{e(T["label"])}</span><span class="mono dim">{p["num"]} / {e(p["domain"])}</span></p>
        <h1>{e(p["title"])}</h1>
        <p class="lead">{e(p["tagline"])}</p>
        <div class="tags">{tags(p["tags"])}</div>
        <div class="actions">
          <a class="btn" href="{GITHUB}/{p["slug"]}" target="_blank" rel="noopener">Voir le code ↗</a>
        </div>
      </div>
      <div class="p-hero-side">
        <div class="deco" aria-hidden="true">{T["svg"]()}</div>
        <dl class="facts">{facts}</dl>
      </div>
    </div>
  </section>

  <section class="wrap section">
    {sec("Contexte")}
    <div class="prose">{p["context"]}</div>
  </section>

  <section class="wrap section">
    {sec("Architecture")}
    <ol class="pipeline">{steps}</ol>
    <p class="caption">{e(p["pipeline_caption"])}</p>
    <!-- Add image here :
    <figure class="media"><img src="../assets/img/{p["slug"]}.jpg" alt="{e(p["title"])}"><figcaption>Légende</figcaption></figure>
    -->
  </section>

  <section class="wrap section">
    {sec("Points techniques")}
    <div class="points">{points}</div>
  </section>

  <section class="wrap section">
    {sec("Extrait de code")}
    <div class="code">
      <div class="code-bar mono"><span class="dots"><i></i><i></i><i></i></span>{e(p["code_lang"])}</div>
      <pre><code>{e(p["code"])}</code></pre>
    </div>
  </section>

  <section class="wrap section">
    {sec("Ce que j'en retiens")}
    <ul class="learned">{learned}</ul>
  </section>

  <nav class="wrap pager">
    <a class="theme-{THEME_OF[prev_p["slug"]]}" href="{prev_p["slug"]}.html"><span class="mono dim">← Précédent</span><strong>{e(prev_p["title"])}</strong></a>
    <a class="next theme-{THEME_OF[next_p["slug"]]}" href="{next_p["slug"]}.html"><span class="mono dim">Suivant →</span><strong>{e(next_p["title"])}</strong></a>
  </nav>
</main>
""" + footer()

def index_page():
    cards = ""
    for p in PROJECTS:
        th = THEME_OF[p["slug"]]
        cards += f"""
      <a class="card theme-{th}" data-theme="{th}" href="projets/{p["slug"]}.html">
        <div class="card-deco" aria-hidden="true">{THEMES[th]["svg"]()}</div>
        <div class="card-top"><span class="theme-badge">{e(THEMES[th]["label"])}</span><span class="mono dim">{p["num"]}</span></div>
        <h3>{e(p["title"])}</h3>
        <p>{e(p["tagline"])}</p>
        <div class="tags">{tags(p["tags"][:4])}</div>
        <span class="card-go mono">Découvrir →</span>
      </a>"""
    used = []
    for p in PROJECTS:
        t = THEME_OF[p["slug"]]
        if t not in used: used.append(t)
    filters = '<button class="chip active" data-f="all">Tous</button>' + "".join(
        f'<button class="chip theme-{t}" data-f="{t}"><i></i>{e(THEMES[t]["label"])}</button>' for t in used)
    skills = [
        ("Embarqué", ["C", "ESP32 / ESP-IDF", "FreeRTOS", "I²C · ADC · PWM"]),
        ("Électronique", ["Conception PCB", "KiCad", "Capteurs", "Moteurs"]),
        ("Matériel numérique", ["VHDL", "Architecture CPU", "Simulation", "FPGA"]),
        ("Logiciel", ["C++", "CUDA", "Compilation", "Flex · Bison"]),
    ]
    sk = "".join(f'<div class="skill"><h3 class="mono">{e(t)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in xs)}</ul></div>' for t, xs in skills)
    script = """<script>
document.querySelectorAll('.chip').forEach(c => c.addEventListener('click', () => {
  document.querySelectorAll('.chip').forEach(x => x.classList.toggle('active', x === c));
  const f = c.dataset.f;
  document.querySelectorAll('.card').forEach(k => k.hidden = !(f === 'all' || k.dataset.theme === f));
}));
</script>
"""
    return head(f"{NAME} — Portfolio", "Portfolio : systèmes embarqués, électronique, compilation et calcul GPU.", 0, ALL_FONTS, "theme-home") + nav(0) + f"""
<main>
  <section class="hero wrap">
    <p class="eyebrow mono"><span class="pulse"></span> Portfolio · 2026</p>
    <h1>Je construis des systèmes,<br><span class="accent">du transistor au compilateur.</span></h1>
    <p class="lead">Je m'appelle {e(NAME)}. J'aime les projets où le logiciel rencontre le matériel : firmware embarqué, conception de PCB, processeurs en VHDL, compilateurs et calcul sur GPU.</p>
    <div class="actions">
      <a class="btn" href="#projets">Voir les projets</a>
      <a class="btn ghost" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a>
    </div>
    <div class="stack mono">
      <span>C</span><span>C++</span><span>CUDA</span><span>VHDL</span><span>ESP-IDF</span><span>KiCad</span>
    </div>
  </section>

  <section id="projets" class="wrap section">
    <div class="sec-head">
      {sec("Projets")}
      <div class="filters">{filters}</div>
    </div>
    <div class="grid">{cards}
    </div>
  </section>

  <section id="apropos" class="wrap section">
    {sec("À propos")}
    <div class="about">
      <div class="prose">
        <p>Mes projets couvrent toute la pile : concevoir une carte électronique, écrire le firmware qui tourne dessus, décrire un processeur en VHDL, ou au contraire monter dans les couches pour écrire un compilateur.</p>
        <p>Ce qui me motive : comprendre comment les choses fonctionnent vraiment, et les faire marcher en conditions réelles — avec du bruit, des contraintes de temps et des ressources limitées.</p>
      </div>
      <div class="skills">{sk}</div>
    </div>
  </section>

  <section id="contact" class="wrap section contact">
    <h2>On en parle ?</h2>
    <p class="dim">Stage, projet ou simple question technique : écris-moi.</p>
    <div class="actions center">
      <a class="btn" href="mailto:{EMAIL}">{e(EMAIL)}</a>
      <a class="btn ghost" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a>
      <a class="btn ghost" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a>
    </div>
  </section>
</main>
""" + footer(script)

README = f"""# Portfolio - {NAME}

Static site (HTML/CSS, no dependencies) ready for **GitHub Pages**.

```
index.html              home page (filter by theme)
projets/*.html          one page per project, each with its own theme
assets/style.css        styles + themes
assets/img/             (to create) your photos / diagrams
```

## Themes

Each project page carries a class on `<body>`:

| Class                 | Mood                                       | Projects                   |
|-----------------------|--------------------------------------------|----------------------------|
| `theme-compilation`   | code editor, purple, syntax tree           | Tiger Compiler             |
| `theme-hardware`      | green PCB, copper traces and pads          | Light Tracker, PCB Snake   |
| `theme-software`      | GPU, cyan/purple, pixel grid               | Object Detection GPU       |
| `theme-systeme`       | oscilloscope, phosphor green, signals      | Dérisquage ESP32           |
| `theme-architecture`  | blueprint, clock timing diagram            | CPU Monocycle              |

To change a project's theme: edit the `theme-…` class on its page's `<body>`
(and on its card in `index.html`). For a new theme: copy a `.theme-…` block in
`assets/style.css` and adjust its variables (`--bg`, `--accent`, `--pattern`, fonts…).
"""

def main():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(f"{OUT}/projets"); os.makedirs(f"{OUT}/assets")
    open(f"{OUT}/index.html", "w").write(index_page())
    shutil.copy("style.css", f"{OUT}/assets/style.css")
    open(f"{OUT}/README.md", "w").write(README)
    open(f"{OUT}/.nojekyll", "w").write("")
    for i, p in enumerate(PROJECTS):
        open(f"{OUT}/projets/{p['slug']}.html", "w").write(project_page(i, p))
    print("ok")

if __name__ == '__main__':
    main()
