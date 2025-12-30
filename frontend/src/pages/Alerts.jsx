/**
 * Alerts page.
 * Displays active financial alerts.
 */

import { useQuery } from "@tanstack/react-query";
import { fetchAlerts } from "../services/alertsApi";

export default function Alerts() {
  const { data = [], isLoading } = useQuery({
    queryKey: ["alerts"],
    queryFn: fetchAlerts,
  });

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
