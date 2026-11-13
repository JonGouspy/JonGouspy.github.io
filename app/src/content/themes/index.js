// Per-project themes: the label shown on cards and the decorative SVG (see ./<theme>.svg).
// Colors, fonts and patterns of each theme live in src/style.css (.theme-<name>).
import compilation from "./compilation.svg?raw";
import hardware from "./hardware.svg?raw";
import software from "./software.svg?raw";
import systeme from "./systeme.svg?raw";
import architecture from "./architecture.svg?raw";

export const themeLabels = {
  compilation: {
    fr: "Compilation",
    en: "Compilers",
    eu: "Konpilazioa",
  },
  hardware: {
    fr: "Hardware",
    en: "Hardware",
    eu: "Hardwarea",
  },
  software: {
    fr: "Software",
    en: "Software",
    eu: "Softwarea",
  },
  systeme: {
    fr: "Système",
    en: "Systems",
    eu: "Sistemak",
  },
  architecture: {
    fr: "Architecture",
    en: "Architecture",
    eu: "Arkitektura",
  },
};

export const themes = {
  compilation: { svg: compilation },
  hardware: { svg: hardware },
  software: { svg: software },
  systeme: { svg: systeme },
  architecture: { svg: architecture },
};
