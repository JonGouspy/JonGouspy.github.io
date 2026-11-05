#!/usr/bin/env python3
"""Exports the portfolio content (projects, UI strings, SVG decos) to JSON for the React app."""
import json
from projects_data import NAME, GITHUB, EMAIL, LINKEDIN, PROJECTS
from build2 import THEME_OF, THEMES, ALL_FONTS
from build3 import localized
from i18n import LANGS, LANG_NAMES, PROJ_DIR, THEME_LABELS, UI

data = dict(
    site=dict(name=NAME, github=GITHUB, email=EMAIL, linkedin=LINKEDIN, fonts=ALL_FONTS),
    langs=LANGS, langNames=LANG_NAMES, projDir=PROJ_DIR, themeLabels=THEME_LABELS,
    ui={l: {k: ([list(x) for x in v] if k == "skills" else v) for k, v in UI[l].items()} for l in LANGS},
    themes={t: dict(font=T["font"], svg=T["svg"]()) for t, T in THEMES.items()},
    projects={l: [dict(localized(p, l), theme=THEME_OF[p["slug"]],
                       points=[list(x) for x in localized(p, l)["points"]],
                       facts=[list(x) for x in localized(p, l)["facts"]]) for p in PROJECTS] for l in LANGS},
)
with open("../app/src/data/content.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("ok")
