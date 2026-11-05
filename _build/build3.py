#!/usr/bin/env python3
"""Multilingual portfolio (FR/EN/EU) + per-project themes + light/dark mode."""
import html, os, shutil
from projects_data import NAME, GITHUB, EMAIL, LINKEDIN, PROJECTS
from build2 import THEME_OF, THEMES, ALL_FONTS
from i18n import LANGS, LANG_NAMES, PROJ_DIR, THEME_LABELS, UI, CODE_EN, TR

OUT = "site"
e = html.escape
BASE = "https://jon-gouspy.github.io/"

def localized(p, lang):
    if lang == "fr":
        return p
    q = dict(p); q.update(TR[lang].get(p["slug"], {}))
    code = q["code"]
    for a, b in CODE_EN:
        code = code.replace(a, b)
    q["code"] = code
    return q

def rel_root(lang, is_project):
    """Relative path to the site root."""
    depth = (0 if lang == "fr" else 1) + (1 if is_project else 0)
    return "../" * depth

def page_path(lang, slug=None):
    """Path of a page from the site root."""
    pre = "" if lang == "fr" else f"{lang}/"
    return pre + (f"{PROJ_DIR[lang]}/{slug}.html" if slug else "index.html")

ICONS = """<svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg><svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z"/></svg>"""

def head(title, desc, lang, slug, fonts, body_class, redirect=False):
    root = rel_root(lang, slug is not None)
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{page_path(l, slug)}">' for l in LANGS)
    redir = ""
    if redirect:  # FR home page: redirects to the remembered language
        redir = "try{var l=localStorage.getItem('lang');if(l==='en'||l==='eu')location.replace(l+'/index.html'+location.hash)}catch(e){}"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>(function(){{var m;try{{m=localStorage.getItem('mode')}}catch(e){{}}if(m!=='light'&&m!=='dark')m=matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';document.documentElement.dataset.mode=m;{redir}}})()</script>
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{alts}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fonts}&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%23101318'/><text x='16' y='22' font-family='monospace' font-size='16' font-weight='700' fill='%23ffb547' text-anchor='middle'>JG</text></svg>">
</head>
<body class="{body_class}">
"""

ACTIVE = ' class="active" aria-current="true"'

def nav(lang, slug):
    U = UI[lang]
    root = rel_root(lang, slug is not None)
    home = root + page_path(lang)
    langs = "".join(
        f'<a href="{root}{page_path(l, slug)}" hreflang="{l}" lang="{l}" title="{LANG_NAMES[l]}" data-lang="{l}"'
        f'{ACTIVE if l == lang else ""}>{l.upper()}</a>' for l in LANGS)
    return f"""<header class="topbar">
  <a class="logo" href="{home}"><span class="logo-mark">JG</span><span class="logo-text">{e(NAME)}</span></a>
  <nav>
    <a class="nl" href="{home}#projets">{e(U["nav_projects"])}</a>
    <a class="nl" href="{home}#apropos">{e(U["nav_about"])}</a>
    <a class="nl" href="{home}#contact">{e(U["nav_contact"])}</a>
    <a class="btn-gh" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a>
    <div class="lang-switch" role="group" aria-label="{e(U["lang"])}">{langs}</div>
    <button class="mode-toggle" type="button" aria-label="{e(U["mode"])}" title="{e(U["mode"])}">{ICONS}</button>
  </nav>
</header>
"""

COMMON_JS = """<script>
(function(){
  var b=document.querySelector('.mode-toggle');
  if(b)b.addEventListener('click',function(){
    var m=document.documentElement.dataset.mode==='light'?'dark':'light';
    document.documentElement.dataset.mode=m;try{localStorage.setItem('mode',m)}catch(e){}
  });
  document.querySelectorAll('.lang-switch a').forEach(function(a){
    a.addEventListener('click',function(){try{localStorage.setItem('lang',a.dataset.lang)}catch(e){}});
  });
  document.querySelectorAll('.chip').forEach(function(c){c.addEventListener('click',function(){
    document.querySelectorAll('.chip').forEach(function(x){x.classList.toggle('active',x===c)});
    var f=c.dataset.f;
    document.querySelectorAll('.card').forEach(function(k){k.hidden=!(f==='all'||k.dataset.theme===f)});
  })});
})();
</script>
"""

def footer(lang):
    return f"""<footer class="footer">
  <div class="wrap footer-in">
    <span>© 2026 {e(NAME)}</span>
    <span class="mono dim">{e(UI[lang]["footer"])}</span>
  </div>
</footer>
{COMMON_JS}</body>
</html>
"""

def tags(ts):
    return "".join(f'<span class="tag">{e(t)}</span>' for t in ts)

def sec(title):
    return f'<h2 class="h-sec"><span class="sec-mark"></span>{e(title)}</h2>'

def project_page(i, lang):
    U = UI[lang]
    p = localized(PROJECTS[i], lang)
    th = THEME_OF[p["slug"]]; T = THEMES[th]
    prev_p = localized(PROJECTS[i - 1], lang); next_p = localized(PROJECTS[(i + 1) % len(PROJECTS)], lang)
    steps = "".join(f'<li><span class="step-n">{k+1:02d}</span>{e(s)}</li>' for k, s in enumerate(p["pipeline"]))
    points = "".join(f'<div class="point"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in p["points"])
    facts = "".join(f'<div class="fact"><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in p["facts"])
    learned = "".join(f"<li>{e(l)}</li>" for l in p["learned"])
    home = "../index.html"
    return head(f'{p["title"]} — {NAME}', p["tagline"], lang, p["slug"], T["font"], f"theme-{th}") + nav(lang, p["slug"]) + f"""
<main>
  <section class="p-hero wrap">
    <a class="back mono" href="{home}#projets">{e(U["back"])}</a>
    <div class="p-hero-grid">
      <div class="p-hero-main">
        <p class="eyebrow"><span class="theme-badge">{e(THEME_LABELS[th][lang])}</span><span class="mono dim">{p["num"]} / {e(p["domain"])}</span></p>
        <h1>{e(p["title"])}</h1>
        <p class="lead">{e(p["tagline"])}</p>
        <div class="tags">{tags(p["tags"])}</div>
        <div class="actions">
          <a class="btn" href="{GITHUB}/{p["slug"]}" target="_blank" rel="noopener">{e(U["view_code"])}</a>
        </div>
      </div>
      <div class="p-hero-side">
        <div class="deco" aria-hidden="true">{T["svg"]()}</div>
        <dl class="facts">{facts}</dl>
      </div>
    </div>
  </section>

  <section class="wrap section">
    {sec(U["s_context"])}
    <div class="prose">{p["context"]}</div>
  </section>

  <section class="wrap section">
    {sec(U["s_arch"])}
    <ol class="pipeline">{steps}</ol>
    <p class="caption">{e(p["pipeline_caption"])}</p>
    <!-- Image / GIF / demo :
    <figure class="media"><img src="{rel_root(lang, True)}assets/img/{p["slug"]}.jpg" alt="{e(p["title"])}"><figcaption>…</figcaption></figure>
    -->
  </section>

  <section class="wrap section">
    {sec(U["s_points"])}
    <div class="points">{points}</div>
  </section>

  <section class="wrap section">
    {sec(U["s_code"])}
    <div class="code">
      <div class="code-bar mono"><span class="dots"><i></i><i></i><i></i></span>{e(p["code_lang"])}</div>
      <pre><code>{e(p["code"])}</code></pre>
    </div>
  </section>

  <section class="wrap section">
    {sec(U["s_learned"])}
    <ul class="learned">{learned}</ul>
  </section>

  <nav class="wrap pager">
    <a class="theme-{THEME_OF[prev_p["slug"]]}" href="{prev_p["slug"]}.html"><span class="mono dim">{e(U["prev"])}</span><strong>{e(prev_p["title"])}</strong></a>
    <a class="next theme-{THEME_OF[next_p["slug"]]}" href="{next_p["slug"]}.html"><span class="mono dim">{e(U["next"])}</span><strong>{e(next_p["title"])}</strong></a>
  </nav>
</main>
""" + footer(lang)

def index_page(lang):
    U = UI[lang]
    cards = ""
    used = []
    for p0 in PROJECTS:
        p = localized(p0, lang)
        th = THEME_OF[p["slug"]]
        if th not in used: used.append(th)
        cards += f"""
      <a class="card theme-{th}" data-theme="{th}" href="{PROJ_DIR[lang]}/{p["slug"]}.html">
        <div class="card-deco" aria-hidden="true">{THEMES[th]["svg"]()}</div>
        <div class="card-top"><span class="theme-badge">{e(THEME_LABELS[th][lang])}</span><span class="mono dim">{p["num"]}</span></div>
        <h3>{e(p["title"])}</h3>
        <p>{e(p["tagline"])}</p>
        <div class="tags">{tags(p["tags"][:4])}</div>
        <span class="card-go mono">{e(U["discover"])}</span>
      </a>"""
    filters = f'<button class="chip active" data-f="all">{e(U["filter_all"])}</button>' + "".join(
        f'<button class="chip theme-{t}" data-f="{t}"><i></i>{e(THEME_LABELS[t][lang])}</button>' for t in used)
    sk = "".join(f'<div class="skill"><h3 class="mono">{e(t)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in xs)}</ul></div>' for t, xs in U["skills"])
    about = "".join(f"<p>{e(x)}</p>" for x in U["about"])
    return head(f"{NAME} — Portfolio", U["site_desc"], lang, None, ALL_FONTS, "theme-home", redirect=(lang == "fr")) + nav(lang, None) + f"""
<main>
  <section class="hero wrap">
    <p class="eyebrow mono"><span class="pulse"></span> Portfolio · 2026</p>
    <h1>{e(U["hero_a"])}<br><span class="accent">{e(U["hero_b"])}</span></h1>
    <p class="lead">{e(U["hero_lead"].format(name=NAME))}</p>
    <div class="actions">
      <a class="btn" href="#projets">{e(U["btn_projects"])}</a>
      <a class="btn ghost" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a>
    </div>
    <div class="stack mono">
      <span>C</span><span>C++</span><span>CUDA</span><span>VHDL</span><span>ESP-IDF</span><span>KiCad</span>
    </div>
  </section>

  <section id="projets" class="wrap section">
    <div class="sec-head">
      {sec(U["nav_projects"])}
      <div class="filters">{filters}</div>
    </div>
    <div class="grid">{cards}
    </div>
  </section>

  <section id="apropos" class="wrap section">
    {sec(U["nav_about"])}
    <div class="about">
      <div class="prose">{about}</div>
      <div class="skills">{sk}</div>
    </div>
  </section>

  <section id="contact" class="wrap section contact">
    <h2>{e(U["contact_h"])}</h2>
    <p class="dim">{e(U["contact_p"])}</p>
    <div class="actions center">
      <a class="btn" href="mailto:{EMAIL}">{e(EMAIL)}</a>
      <a class="btn ghost" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a>
      <a class="btn ghost" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a>
    </div>
  </section>
</main>
""" + footer(lang)

def main():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(f"{OUT}/assets")
    shutil.copy("style.css", f"{OUT}/assets/style.css")
    shutil.copy("README.md", f"{OUT}/README.md")
    open(f"{OUT}/.nojekyll", "w").write("")
    for lang in LANGS:
        base = OUT if lang == "fr" else f"{OUT}/{lang}"
        os.makedirs(f"{base}/{PROJ_DIR[lang]}", exist_ok=True)
        open(f"{base}/index.html", "w").write(index_page(lang))
        for i, p in enumerate(PROJECTS):
            open(f"{base}/{PROJ_DIR[lang]}/{p['slug']}.html", "w").write(project_page(i, lang))
    print("ok")

if __name__ == "__main__":
    main()
