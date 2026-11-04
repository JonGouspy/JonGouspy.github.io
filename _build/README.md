# Portfolio — Jon Gouspy

Site statique (HTML/CSS, sans dépendance) prêt pour **GitHub Pages**.

```
index.html, projets/          version française (par défaut)
en/index.html, en/projects/   version anglaise
eu/index.html, eu/proiektuak/ version basque
assets/style.css              styles, thèmes, mode clair/sombre
assets/img/                   (à créer) tes photos / schémas
```

## Langues et mode clair/sombre

- Le sélecteur **FR · EN · EU** (en haut à droite) renvoie vers la même page dans l'autre langue.
  Le choix est mémorisé : la page d'accueil racine redirige vers la langue choisie.
- Le bouton ☀/☾ bascule entre clair et sombre. Par défaut, le site suit le réglage du système ;
  le choix de l'utilisateur est ensuite mémorisé.
- Chaque thème de projet a sa variante claire (bloc `html[data-mode="light"] .theme-…` dans le CSS).
- Les pages sont générées par `_build/build3.py` à partir de `projects_data.py` (FR) et `i18n.py` (EN, EU) :
  modifie le texte là, lance `cd _build && python3 build3.py`, puis recopie `_build/site/` à la racine — ou édite directement les fichiers HTML.

## Thèmes

Chaque page projet porte une classe sur `<body>` :

| Classe                | Ambiance                                   | Projets                    |
|-----------------------|--------------------------------------------|----------------------------|
| `theme-compilation`   | éditeur de code, violet, arbre syntaxique  | Tiger Compiler             |
| `theme-hardware`      | PCB vert, pistes et pastilles cuivre       | Light Tracker, PCB Snake   |
| `theme-software`      | GPU, cyan/violet, grille de pixels         | Object Detection GPU       |
| `theme-systeme`       | oscilloscope, vert phosphore, signaux      | Dériscage ESP32            |
| `theme-architecture`  | plan bleu, chronogramme d'horloge          | CPU Monocycle              |

## Mise en ligne

1. Crée un dépôt nommé **`jon-gouspy.github.io`** (remplace par ton pseudo).
2. Copie le contenu de ce dossier à la racine du dépôt, puis :
   ```bash
   git add . && git commit -m "Portfolio" && git push
   ```
3. Dans *Settings → Pages*, choisis la branche `main` / dossier `/ (root)`.
4. Le site est en ligne sur `https://jon-gouspy.github.io`.

## À personnaliser

- Remplace partout `jon-gouspy` et `jon-gouspy-futur-ingenieur` (rechercher/remplacer dans tout le dossier).
- Les boutons « Voir le code » pointent vers `github.com/jon-gouspy/<nom-du-projet>` :
  adapte-les au vrai nom de tes dépôts.
- Chaque page projet contient un commentaire `<!-- Add image here -->`
  pour insérer une photo, un GIF ou une capture.
- Vérifie les détails techniques et ajoute tes chiffres (gains de perf GPU, dérive mesurée…).
