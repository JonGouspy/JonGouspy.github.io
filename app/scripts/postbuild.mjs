// GitHub Pages has no server-side routing: serve index.html for unknown paths via 404.html.
import { copyFileSync } from "node:fs";
copyFileSync("dist/index.html", "dist/404.html");
