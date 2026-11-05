import data from "./data/content.json";

export const { site, langs, langNames, projDir, themeLabels, ui, themes, projects } = data;

export const homePath = (lang) => (lang === "fr" ? "/" : `/${lang}`);
export const projectPath = (lang, slug) => `${lang === "fr" ? "" : `/${lang}`}/${projDir[lang]}/${slug}`;
