# Portfolio — Jon Gouspy

React portfolio (Vite + React 18 + React Router), in three languages (FR · EN · EU) with light/dark mode.
Deployed to **GitHub Pages** at `https://jon-gouspy.github.io`.

```
app/                 the React site (source of truth)
  src/pages/         Home, Project
  src/components/    Layout (top bar, footer), Deco, Section
  src/data/          content.json — all text, generated from _build (see below)
  src/style.css      styles, per-project themes, light/dark mode
_build/              Python content sources + JSON exporter (legacy static generator)
.github/workflows/   build and deploy to GitHub Pages
```

## Develop

```bash
cd app
npm install
npm run dev        # http://localhost:5173
npm run build      # -> app/dist
```

No Node installed (NixOS)? Prefix with `nix-shell -p nodejs_22 --run "…"`.

## URLs

| Language | Home     | Project                     |
|----------|----------|-----------------------------|
| FR       | `/`      | `/projets/<slug>`           |
| EN       | `/en`    | `/en/projects/<slug>`       |
| EU       | `/eu`    | `/eu/proiektuak/<slug>`     |

GitHub Pages has no server-side routing, so the build also writes `404.html` (a copy of `index.html`)
and React Router resolves the path on the client.

## Languages and light/dark mode

- The **FR · EN · EU** switcher links to the same page in the other language. The choice is saved in
  `localStorage`; opening `/` then redirects to the saved language.
- The ☀/☾ button toggles light/dark. By default the site follows the system setting; the choice is saved.
  The mode is set on `<html data-mode>` by a small script in `app/index.html` (no flash on load).
- Each project theme has its own light variant (`html[data-mode="light"] .theme-…` blocks in the CSS).

## Content

All text is in `app/src/data/content.json`, generated from the Python sources:

- `_build/projects_data.py` — projects (French)
- `_build/i18n.py` — UI strings and EN / EU translations
- `_build/build2.py` — per-theme decorative SVGs and fonts

After editing them:

```bash
cd _build && python3 export_json.py
```

You can also drop the Python and edit `content.json` directly.
Project `context` fields are HTML (rendered with `dangerouslySetInnerHTML`): it is your own content, keep it that way.

## Styles

Edit `app/src/style.css`. (`_build/style.css` is only used by the old static generator and is no longer needed.)

## Themes

Each page sets a class on `<body>`:

| Class                 | Mood                                       | Projects                   |
|-----------------------|--------------------------------------------|----------------------------|
| `theme-home`          | default home page                          | —                          |
| `theme-compilation`   | code editor, purple, syntax tree           | Tiger Compiler             |
| `theme-hardware`      | green PCB, copper traces and pads          | Light Tracker, PCB Snake   |
| `theme-software`      | GPU, cyan/purple, pixel grid               | Object Detection GPU       |
| `theme-systeme`       | oscilloscope, phosphor green, signals      | Dériscage ESP32            |
| `theme-architecture`  | blueprint, clock timing diagram            | CPU Monocycle              |

A project's theme is set by `THEME_OF` in `_build/build2.py`. For a new theme, copy a `.theme-…` block in
the CSS, adjust its variables (`--bg`, `--accent`, `--pattern`, fonts…), and add its SVG and fonts in `build2.py`.

## Deployment

`.github/workflows/deploy.yml` builds `app/` and publishes `app/dist` on every push to `main`.

One-time setup: *Settings → Pages → Source: **GitHub Actions***.

## To customize

- "View code" buttons point to `github.com/jon-gouspy/<slug>`: adapt `<slug>` to your real repository names
  (`app/src/pages/Project.jsx`).
- To add a photo, GIF or screenshot to a project page, put it in `app/public/img/` and add an `<img>`
  in `Project.jsx` (served at `/img/<file>`).
- Check the technical details and add your numbers (GPU speed-ups, measured drift…).
