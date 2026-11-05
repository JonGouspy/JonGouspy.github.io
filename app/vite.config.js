import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// User site (jon-gouspy.github.io): served from the domain root.
export default defineConfig({ plugins: [react()] });
