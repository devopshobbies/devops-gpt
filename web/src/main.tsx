import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import { Toaster } from 'sonner';
import { BrowserRouter } from 'react-router';
import QueryProvider from '@/providers/react-query-provider';

import './index.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <QueryProvider>
        <App />
      </QueryProvider>
    </BrowserRouter>
    <Toaster />
  </StrictMode>,
);
