/**
 * Alerts page.
 * Displays active financial alerts.
 */

import { useQuery } from "@tanstack/react-query";
import { fetchAlerts } from "../services/alertsApi";
import posthog from "../analytics/posthog";
import { useEffect } from "react";


export default function Alerts() {
  const { data = [], isLoading } = useQuery({
    queryKey: ["alerts"],
    queryFn: fetchAlerts,
  });

  useEffect(() => {
    posthog.capture("alerts_viewed", {
      alert_count: data.length,
      has_alerts: data.length > 0,
    });
  }, [data]);

  if (isLoading) return <p>Loading alerts...</p>;

  if (!data.length) {
    return (
      <p className="text-gray-500 p-6">
        No alerts right now. You're doing well!
      </p>
    );
  }

  return (
    <div className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">Alerts</h1>

      {data.map((alert, index) => (
        <div
          key={index}
          className="bg-red-50 border border-red-200 p-4 rounded-xl"
        >
          {alert}
        </div>
      ))}
    </div>
  );
}
