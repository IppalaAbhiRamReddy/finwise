# PHASE 3 — ALERTS & EXTERNAL ML INTEGRATION

## Phase Name
Phase 3 – Alerts Engine, External ML Integration & Reliability

## Phase Objective
Make FinWise proactive by generating alerts and integrating external ML
safely, without compromising system stability.

## Dependencies
- Phase 2 completed and committed
- Dashboard and insights stable
- Transactions, budgets, and goals populated

## Scope (IN)
- Rule-based alerts engine
- External ML adapter layer
- Alerts API
- Alerts frontend UI
- Background processing with Celery
- ML fallback logic

## Scope (OUT)
- In-app ML training
- Alert persistence in database
- Notifications (email/SMS/push)
- User-configurable alert rules
- Advanced scheduling

## Alert Types Implemented
- Budget overuse alerts
- Unusual spending alerts
- Low savings alerts
- Optional ML-generated insights

## ML Integration Rules
- ML is optional
- ML failure must not affect system
- ML must not write to database
- ML insights are advisory only
- Rule-based alerts always run

## Reliability Guarantees
- APIs never block on ML
- Background retries handled by Celery
- Silent ML failures
- Deterministic rule-based fallback

## Invariants (Must Not Break)
- No schema changes
- Dashboard unaffected by ML
- Alerts remain explainable
- Frontend independent of ML availability

## Exit Criteria
- Rule-based alerts work correctly
- ML adapter fails safely
- Alerts API aggregates rule + ML alerts
- Alerts UI renders correctly
- Celery tasks run without crashing
- Phase committed to Git

## Outcome
FinWise becomes proactive, ML-ready, and production-safe with asynchronous alerts.
