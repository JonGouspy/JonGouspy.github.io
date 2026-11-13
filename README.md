# Portfolio — Jon Gouspy

React portfolio (Vite + React 18 + React Router), in three languages (FR · EN · EU) with light/dark mode.
Deployed to **GitHub Pages** at `https://jongouspy.github.io/jon-gouspy.github.io/`.

```
app/                 the React site (source of truth)
  src/pages/         Home, Project
  src/components/    Layout (top bar, footer), Deco, Section
  src/content/       all text and data, plain files you edit by hand (see Content)
  src/content.js     loads src/content/* for the pages (rarely needs editing)
  src/style.css      styles, per-project themes, light/dark mode
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

Everything you read on the site is in `app/src/content/`, as plain JS files you edit by hand. There is no
generator and no build step for content: save, and the dev server reloads.

| File | What it holds |
|------|---------------|
| `site.js` | name, GitHub / e-mail / LinkedIn links, languages |
| `ui/fr.js`, `ui/en.js`, `ui/eu.js` | interface text: menu, hero, about, skills, buttons |
| `projects/NN-<slug>.js` | one project, with its French, English and Basque text side by side |
| `future.js` | the greyed-out "upcoming projects" cards |
| `themes/` | the label of each theme and its decorative `.svg` |

**Edit a project**: open its file in `content/projects/`. Fields are grouped per language (`fr`, `en`, `eu`).
Text with several lines (`context`, `code`) goes between backticks. `context` is HTML (rendered with
`dangerouslySetInnerHTML`): it is your own content, keep it that way.

**Add a project**: copy `content/projects/_template.js` to `NN-<slug>.js` (`NN` sets the display order) and
fill it in. It appears on the home page and gets its own page automatically. Delete the `repo` line to hide
the "View code" button (for a private repository). An optional `image` shows a picture on the project page
(put the file in `app/public/img/`).

**Add an upcoming project**: add an entry to `content/future.js`.

## Styles

Edit `app/src/style.css`.

## Themes

Each page sets a class on `<body>`:

| Class                 | Mood                                       | Projects                   |
|-----------------------|--------------------------------------------|----------------------------|
| `theme-home`          | default home page                          | —                          |
| `theme-compilation`   | code editor, purple, syntax tree           | Tiger Compiler             |
| `theme-hardware`      | green PCB, copper traces and pads          | Light Tracker, PCB Snake   |
| `theme-software`      | GPU, cyan/purple, pixel grid               | Object Detection GPU       |
| `theme-systeme`       | oscilloscope, phosphor green, signals      | Dérisquage ESP32           |
| `theme-architecture`  | blueprint, clock timing diagram            | CPU Monocycle              |

A project's theme is the `theme` field of its file in `content/projects/`. For a new theme, copy a `.theme-…`
block in the CSS and adjust its variables (`--bg`, `--accent`, `--pattern`…), then add its label and its SVG
(`content/themes/<name>.svg`) in `content/themes/index.js`. The font is JetBrains Mono everywhere (`:root` in the CSS).

## Deployment

`.github/workflows/deploy.yml` builds `app/` and publishes `app/dist` on every push to `main`.

## To customize

- The "View code" button of a project points to its `repo` field (see Content).
- Check the technical details and add your numbers (GPU speed-ups, measured drift…).
