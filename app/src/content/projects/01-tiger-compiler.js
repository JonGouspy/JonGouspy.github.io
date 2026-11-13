// Project 01: Tiger Compiler.
// Text is written per language (fr, en, eu). See projects/_template.js for the fields.
export default {
  slug: "tiger-compiler",
  num: "01",
  theme: "compilation",
  fr: {
    title: "Tiger Compiler",
    tagline: "Un compilateur complet pour le langage Tiger, écrit en C++.",
    domain: "Compilation",
    tags: ["C++", "Flex", "Bison", "AST", "IR"],
    facts: [
      ["Langage", "C++17"],
      ["Outils", "Flex · Bison · Make"],
      ["Cible", "LLVM ou back-end maison"],
      ["Type", "Projet d'équipe"],
    ],
    context: `<p>Tiger est un petit langage impératif typé, issu du livre <em>Modern Compiler Implementation</em> d'Andrew Appel. Il possède des types structurés (records, tableaux), des fonctions imbriquées, des portées lexicales et une gestion explicite de <code>let … in … end</code>.</p>
<p>L'objectif : partir d'un fichier source <code>.tig</code> et produire du code exécutable, en traversant toutes les étapes d'un vrai compilateur — de l'analyse lexicale jusqu'à l'allocation de registres.</p>`,
    pipeline: [
      "Source .tig",
      "Lexer (Flex)",
      "Parser (Bison)",
      "AST",
      "Binding",
      "Type-checking",
      "Pattern matching",
      "Traduction IR",
      "Canonisation",
      "Sélection d'instructions",
      "Allocation de registres",
      "Assembleur",
    ],
    pipeline_caption: "Chaîne de compilation, du texte source au code machine.",
    points: [
      ["Analyse lexicale & syntaxique", "Scanner Flex et grammaire Bison, avec gestion des conflits, des priorités d'opérateurs et des messages d'erreur localisés (ligne / colonne)."],
      ["AST & visiteurs", "Arbre syntaxique abstrait en C++ parcouru via le design pattern Visitor : pretty-printer, binder, type-checker et traducteur partagent la même hiérarchie."],
      ["Liaison des noms", "Résolution des identifiants avec tables de symboles à portées imbriquées, détection des variables qui « s'échappent » vers des fonctions internes."],
      ["Vérification de types", "Typage des expressions, des records récursifs et des tableaux ; erreurs sémantiques claires plutôt qu'un crash."],
      ["Pattern matching & IR", "Après le typage, mon propre pattern matching déstructure les records et réordonne les conditions des plus utilisées aux moins utilisées (disponible uniquement avec LLVM). Puis traduction en arbre IR, linéarisation et canonisation des blocs de base avant la génération de code."],
      ["Deux back-ends", "Le projet se lie soit à LLVM, soit à mon propre back-end : sélection d'instructions par tuilage de motifs, analyse de vivacité et allocation de registres par coloration de graphe."],
    ],
    code_lang: "Tiger",
    code: `let
  type intlist = { head: int, tail: intlist }
  function sum(l: intlist): int =
    if l = nil then 0
    else l.head + sum(l.tail)
  var l := intlist { head = 1,
           tail = intlist { head = 2, tail = nil } }
in
  print_int(sum(l))
end`,
    learned: [
      "Comprendre ce qui se passe réellement entre le code source et le binaire.",
      "Concevoir une grosse base de code C++ modulaire et testable (suites de tests par étape).",
      "Travailler en équipe sur un projet long avec revues de code et intégration continue.",
    ],
  },
  en: {
    title: "Tiger Compiler",
    tagline: "A complete compiler for the Tiger language, written in C++.",
    domain: "Compilers",
    tags: ["C++", "Flex", "Bison", "AST", "IR"],
    facts: [
      ["Language", "C++17"],
      ["Tools", "Flex · Bison · Make"],
      ["Target", "LLVM or own back end"],
      ["Type", "Team project"],
    ],
    context: `<p>Tiger is a small, statically typed imperative language from Andrew Appel's book <em>Modern Compiler Implementation</em>. It has structured types (records, arrays), nested functions, lexical scoping and explicit <code>let … in … end</code> blocks.</p>
<p>The goal: take a <code>.tig</code> source file and produce executable code, going through every stage of a real compiler — from lexical analysis all the way to register allocation.</p>`,
    pipeline: [
      "Source .tig",
      "Lexer (Flex)",
      "Parser (Bison)",
      "AST",
      "Binding",
      "Type checking",
      "Pattern matching",
      "IR translation",
      "Canonicalization",
      "Instruction selection",
      "Register allocation",
      "Assembly",
    ],
    pipeline_caption: "Compilation pipeline, from source text to machine code.",
    points: [
      ["Lexing & parsing", "Flex scanner and Bison grammar, with conflict resolution, operator precedence and located error messages (line / column)."],
      ["AST & visitors", "C++ abstract syntax tree traversed with the Visitor pattern: pretty-printer, binder, type checker and translator share the same hierarchy."],
      ["Name binding", "Identifier resolution with nested-scope symbol tables, and detection of variables that escape into inner functions."],
      ["Type checking", "Typing of expressions, recursive records and arrays; clear semantic errors instead of crashes."],
      ["Pattern matching & IR", "After type checking, my own pattern matching destructures records and reorders conditions from most used to least used (only available with LLVM). Then translation to an IR tree, linearization and canonicalization into basic blocks before code generation."],
      ["Two back ends", "The project can be linked either with LLVM or with my own back end: instruction selection by tree-pattern tiling, liveness analysis and register allocation by graph coloring."],
    ],
    code_lang: "Tiger",
    code: `let
  type intlist = { head: int, tail: intlist }
  function sum(l: intlist): int =
    if l = nil then 0
    else l.head + sum(l.tail)
  var l := intlist { head = 1,
           tail = intlist { head = 2, tail = nil } }
in
  print_int(sum(l))
end`,
    learned: [
      "Understanding what really happens between source code and binary.",
      "Designing a large, modular and testable C++ codebase (test suites for every stage).",
      "Working as a team on a long project with code reviews and continuous integration.",
    ],
  },
  eu: {
    title: "Tiger Compiler",
    tagline: "Tiger lengoaiarako konpilatzaile osoa, C++-n idatzia.",
    domain: "Konpilazioa",
    tags: ["C++", "Flex", "Bison", "AST", "IR"],
    facts: [
      ["Lengoaia", "C++17"],
      ["Tresnak", "Flex · Bison · Make"],
      ["Helburua", "LLVM edo back-end propioa"],
      ["Mota", "Talde-proiektua"],
    ],
    context: `<p>Tiger lengoaia inperatibo txiki eta tipatua da, Andrew Appel-en <em>Modern Compiler Implementation</em> liburutik datorrena. Datu-mota egituratuak (erregistroak, arrayak), funtzio habiaratuak, esparru lexikoak eta <code>let … in … end</code> blokeak ditu.</p>
<p>Helburua: <code>.tig</code> iturburu-fitxategi batetik abiatuta kode exekutagarria sortzea, benetako konpilatzaile baten urrats guztiak zeharkatuz — analisi lexikotik erregistroen esleipeneraino.</p>`,
    pipeline: [
      "Iturburua .tig",
      "Lexerra (Flex)",
      "Parserra (Bison)",
      "AST",
      "Izenen lotura",
      "Tipo-egiaztapena",
      "Pattern matching",
      "IR itzulpena",
      "Kanonizazioa",
      "Agindu-hautaketa",
      "Erregistro-esleipena",
      "Mihiztadura",
    ],
    pipeline_caption: "Konpilazio-katea, iturburu-testutik makina-kodera.",
    points: [
      ["Analisi lexikoa eta sintaktikoa", "Flex eskanerra eta Bison gramatika, gatazken kudeaketarekin, eragileen lehentasunekin eta kokatutako errore-mezuekin (lerroa / zutabea)."],
      ["AST eta bisitariak", "C++-ko zuhaitz sintaktiko abstraktua, Visitor diseinu-ereduaren bidez korritua: pretty-printerrak, binderrak, tipo-egiaztatzaileak eta itzultzaileak hierarkia bera partekatzen dute."],
      ["Izenen lotura", "Identifikatzaileen ebazpena esparru habiaratuetako ikur-taulekin, eta barneko funtzioetara «ihes egiten» duten aldagaien detekzioa."],
      ["Tipo-egiaztapena", "Adierazpenen, erregistro errekurtsiboen eta arrayen tipatzea; errore semantiko argiak, programa kraskatu beharrean."],
      ["Pattern matching eta IR", "Tipo-egiaztapenaren ondoren, neuk egindako pattern matching-ak erregistroak deskonposatzen ditu eta baldintzak berrordenatzen ditu, gehien erabiltzenetik gutxien erabiltzenera (LLVMrekin soilik erabilgarri). Ondoren IR zuhaitzera itzultzea, eta ondoren oinarrizko blokeen linealizazioa eta kanonizazioa, kodea sortu aurretik."],
      ["Bi back-end", "Proiektua LLVMrekin edo neure back-endarekin lotu daiteke: agindu-hautaketa zuhaitz-ereduen bidez, bizitasun-analisia eta erregistro-esleipena grafoen koloreztatzearen bidez."],
    ],
    code_lang: "Tiger",
    code: `let
  type intlist = { head: int, tail: intlist }
  function sum(l: intlist): int =
    if l = nil then 0
    else l.head + sum(l.tail)
  var l := intlist { head = 1,
           tail = intlist { head = 2, tail = nil } }
in
  print_int(sum(l))
end`,
    learned: [
      "Iturburu-kodearen eta bitarraren artean benetan gertatzen dena ulertzea.",
      "C++ kode-base handi, modular eta probagarri bat diseinatzea (proba-multzoak urrats bakoitzeko).",
      "Taldean lan egitea proiektu luze batean, kode-berrikuspenekin eta integrazio jarraituarekin.",
    ],
  },
};
