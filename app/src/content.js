// Single entry point for all site content. Edit the files in ./content, not this one.
//
//   content/site.js           name, links, languages, URL segment for "projects"
//   content/ui/<lang>.js      interface text for each language
//   content/projects/*.js     one file per project, with fr / en / eu text side by side
//   content/future.js         upcoming projects (greyed cards on the home page)
//   content/themes/           theme labels and the decorative SVG of each theme
import { site, langs, langNames, projDir } from "./content/site.js";
import fr from "./content/ui/fr.js";
import en from "./content/ui/en.js";
import eu from "./content/ui/eu.js";
import { themeLabels, themes } from "./content/themes/index.js";
import futureList from "./content/future.js";

// Projects are listed in file-name order (01-..., 02-...). _template.js is skipped.
const projectFiles = import.meta.glob("./content/projects/[0-9]*.js", { eager: true });
const projectList = Object.entries(projectFiles)
  .sort(([a], [b]) => a.localeCompare(b))
  .map(([, m]) => m.default);

// Per-language views: the shared fields (slug, num, theme, repo, image) merged with that language's text.
const byLang = (list, pick) => Object.fromEntries(langs.map((l) => [l, list.map((item) => pick(item, l))]));

export const ui = { fr, en, eu };
export const projects = byLang(projectList, ({ fr, en, eu, ...shared }, l) => ({ ...shared, ...{ fr, en, eu }[l] }));
export const future = byLang(futureList, ({ fr, en, eu, ...shared }, l) => ({ ...shared, ...{ fr, en, eu }[l] }));
export { site, langs, langNames, projDir, themeLabels, themes };

export const homePath = (lang) => (lang === "fr" ? "/" : `/${lang}`);
export const projectPath = (lang, slug) => `${lang === "fr" ? "" : `/${lang}`}/${projDir[lang]}/${slug}`;
