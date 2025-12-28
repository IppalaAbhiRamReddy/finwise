/**
 * Renders list of textual insights.
 */

export default function InsightList({ insights }) {
  if (!insights.length) {
    return (
      <p className="text-gray-500 text-sm">
        No insights available yet. Add more transactions.
      </p>
    );
  }

  return (
    <ul className="list-disc pl-5 space-y-2">
      {insights.map((insight, index) => (
        <li key={index} className="text-gray-700">
          {insight}
        </li>
      ))}
    </ul>
  );
}
