from django.urls import path
from .views import (
    TransactionListCreateView,
    BudgetListCreateView,
    GoalListCreateView,
)

urlpatterns = [
    path("transactions/", TransactionListCreateView.as_view()),
    path("budgets/", BudgetListCreateView.as_view()),
    path("goals/", GoalListCreateView.as_view()),
]
