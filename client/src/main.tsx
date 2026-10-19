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
    el.innerHTML = "";
    const container = document.createElement("div");
    container.style.padding = "20px";
    container.style.color = "red";
    const header = document.createElement("h1");
    header.textContent = "Failed to start app";
    const pre = document.createElement("pre");
    pre.textContent = e instanceof Error ? e.message : String(e);
    container.appendChild(header);
    container.appendChild(pre);
    el.appendChild(container);
  }
}
