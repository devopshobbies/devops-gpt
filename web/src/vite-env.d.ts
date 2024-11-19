/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_PORT?: string; // Add other VITE_ variables as needed
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
