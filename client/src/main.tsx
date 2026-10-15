import { StrictMode } from "react"
import * as ReactDOMClient from "react-dom/client"
import { BrowserRouter } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { AuthProvider, configureApi } from '@rhino-dev/rhino-react';
import App from "./App"
import "./index.css"
import { ErrorBoundary } from "./components/ErrorBoundary";

try {
  configureApi({
    baseURL: '/api',
    tenancy: 'path'
  });

  const queryClient = new QueryClient();

  const el = document.getElementById("root")
  if (!el) {
    throw new Error("root element not found")
  }
  const root = ReactDOMClient.createRoot(el)
  root.render(
    <StrictMode>
      <ErrorBoundary>
        <QueryClientProvider client={queryClient}>
          <AuthProvider>
            <BrowserRouter>
              <App />
            </BrowserRouter>
          </AuthProvider>
        </QueryClientProvider>
      </ErrorBoundary>
    </StrictMode>
  )
} catch (e) {
  const el = document.getElementById("root");
  if (el) {
    el.innerHTML = `<div style="padding: 20px; color: red;"><h1>Failed to start app</h1><pre>${e instanceof Error ? e.message : String(e)}</pre></div>`;
  }
}
