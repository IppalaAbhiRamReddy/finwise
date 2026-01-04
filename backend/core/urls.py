from django.urls import path
from .health import health_check
from .views import (
    DashboardSummaryView,
    AlertsView,
    TransactionListCreateView,
    BudgetListCreateView,
    GoalListCreateView,
)

urlpatterns = [
    path("health/", health_check),

    path("transactions/", TransactionListCreateView.as_view()),
    path("budgets/", BudgetListCreateView.as_view()),
    path("goals/", GoalListCreateView.as_view()),
    path("dashboard/summary/", DashboardSummaryView.as_view()),
    path("alerts/", AlertsView.as_view()),
]
