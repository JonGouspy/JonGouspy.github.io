import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// BASE_PATH is set by the deploy workflow: "/" for a user site (<name>.github.io repository),
// "/<repository>/" for a project site. Local development uses "/".
export default defineConfig({ base: process.env.BASE_PATH || "/", plugins: [react()] });
