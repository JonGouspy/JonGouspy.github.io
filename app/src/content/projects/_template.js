// Template for a new project. Copy it to NN-your-slug.js (NN = display order) and fill it in.
// Files starting with "_" are ignored by the site.
export default {
  slug: "my-project",           // used in the URL: /projets/my-project
  num: "07",                    // number shown on the card
  theme: "software",            // compilation | hardware | software | systeme | architecture
  repo: "https://github.com/JonGouspy/my-project", // "View code" button; delete the line if the code is private
  // image: "/img/my-project.png", // optional picture shown on the project page (file in public/img)

  // Write the same fields for each language. `fr` is the reference, `en` and `eu` are translations.
  fr: {
    title: "My project",
    tagline: "One sentence under the title and on the card.",
    domain: "Domain",
    tags: ["Tag 1", "Tag 2"],
    facts: [                    // key facts box: [label, value]
      ["Language", "C"],
    ],
    context: `<p>HTML paragraphs: what the project is and why.</p>
<p>Second paragraph.</p>`,
    pipeline: ["Step 1", "Step 2", "Step 3"],
    pipeline_caption: "Caption under the steps.",
    points: [                   // cards: [title, text]
      ["Point title", "Point text."],
    ],
    code_lang: "C",
    code: `int main(void)
{
    return 0;
}`,
    learned: ["What I learned."],
  },
  en: {
    title: "My project",
    tagline: "",
    domain: "",
    tags: [],
    facts: [],
    context: ``,
    pipeline: [],
    pipeline_caption: "",
    points: [],
    code_lang: "C",
    code: ``,
    learned: [],
  },
  eu: {
    title: "My project",
    tagline: "",
    domain: "",
    tags: [],
    facts: [],
    context: ``,
    pipeline: [],
    pipeline_caption: "",
    points: [],
    code_lang: "C",
    code: ``,
    learned: [],
  },
};
