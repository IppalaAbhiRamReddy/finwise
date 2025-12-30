from django.urls import path
from .views import DashboardSummaryView
from .views import AlertsView
from .views import (
    TransactionListCreateView,
    BudgetListCreateView,
    GoalListCreateView,
)

urlpatterns = [
    path("transactions/", TransactionListCreateView.as_view()),
    path("budgets/", BudgetListCreateView.as_view()),
    path("goals/", GoalListCreateView.as_view()),
    path("dashboard/summary/", DashboardSummaryView.as_view()),
    path("alerts/", AlertsView.as_view()),
]
