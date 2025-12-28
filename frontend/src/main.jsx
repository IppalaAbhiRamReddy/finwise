/**
 * Application entry point.
 * Sets up global providers (React Query, StrictMode).
 */

import React from "react";
import ReactDOM from "react-dom/client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

import App from "./App";
import "./index.css";

/**
 * Create a single QueryClient instance
 * This manages caching, retries, and request deduplication
 */
const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  </React.StrictMode>
);
