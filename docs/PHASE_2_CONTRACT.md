# PHASE 2 — DASHBOARD & RULE-BASED INSIGHTS

## Phase Name
Phase 2 – Dashboard Aggregations and Rule-Based Insights

## Phase Objective
Transform raw financial data into meaningful summaries and explainable insights
without using Machine Learning.

## Dependencies
- Phase 1 completed and committed
- Core models (Profile, Transaction, Budget, Goal) stable
- CRUD APIs working correctly

## Scope (IN)
- Backend aggregation services
- Dashboard summary API
- Rule-based insights engine
- Frontend dashboard UI
- Charts and summary cards
- Empty-state handling

## Scope (OUT)
- Alerts
- Notifications
- Machine Learning
- Background jobs
- Caching
- Performance optimization

## Functional Deliverables
- Monthly income, expense, and savings calculation
- Category-wise expense breakdown
- Budget usage computation
- Goal progress computation
- Rule-based insights (trend & category)
- Read-only dashboard API
- Dashboard frontend page

## Non-Functional Constraints
- No database writes
- No new database tables
- Dashboard must work for new users
- Backend performs all calculations
- Frontend must not recompute business logic

## Invariants (Must Not Break)
- Dashboard API contract is immutable
- Derived data is not stored
- ML is not called
- APIs remain read-only

## Exit Criteria
- Dashboard API returns correct data
- Empty users do not cause errors
- Rule-based insights work deterministically
- Frontend dashboard renders correctly
- Phase committed to Git

## Outcome
FinWise now converts stored financial data into clear visual summaries
and explainable insights via a real dashboard.
