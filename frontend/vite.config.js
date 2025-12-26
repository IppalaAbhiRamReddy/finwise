/**
 * Vite configuration
 * Enables Tailwind CSS via official plugin (v4)
 */
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(), // ✅ THIS is what activates Tailwind
  ],
});
