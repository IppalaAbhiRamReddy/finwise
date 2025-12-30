/**
 * Alerts API client.
 */

import axios from "axios";

export const fetchAlerts = async () => {
  const response = await axios.get("/api/alerts/");
  return response.data.alerts;
};
