/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_PORT?: string; // Add other VITE_ variables as needed
  readonly VITE_API_CLIENT_BASE_URL?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
