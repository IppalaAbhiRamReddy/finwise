/**
 * Main dashboard page.
 * Displays summary metrics and insights.
 */

import { useEffect } from "react";
import { useQuery } from "@tanstack/react-query";
import { fetchDashboardSummary } from "../services/dashboardApi";
import SummaryCard from "../components/SummaryCard";
import InsightList from "../components/InsightList";
import posthog from "../analytics/posthog";

export default function Dashboard() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["dashboard"],
    queryFn: fetchDashboardSummary,
  });

  // ✅ Track dashboard view ONCE data is loaded
  useEffect(() => {
    if (data) {
      posthog.capture("dashboard_viewed");
    }
  }, [data]);

  if (isLoading) return <p>Loading dashboard...</p>;
  if (error) return <p>Failed to load dashboard</p>;

  const totals = data?.totals ?? {
    income: 0,
    expense: 0,
    savings: 0,
  };

  const insights = data?.insights ?? [];

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <SummaryCard label="Income" value={totals.income} />
        <SummaryCard label="Expense" value={totals.expense} />
        <SummaryCard label="Savings" value={totals.savings} />
      </div>

      <div className="bg-white p-4 rounded-xl shadow">
        <h2 className="text-lg font-semibold mb-2">Insights</h2>
        <InsightList insights={insights} />
      </div>
    </div>
  );
}
