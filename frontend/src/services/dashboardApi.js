/**
 * Dashboard API client.
 * Purpose:
 * - Fetch dashboard summary from backend
 * - Keep API logic out of UI components
 */

import axios from "axios";

export const fetchDashboardSummary = async () => {
  const response = await axios.get("/api/dashboard/summary/");
  return response.data;
};
