# PHASE 4 — PERFORMANCE, SECURITY & OBSERVABILITY

## Phase Name
Phase 4 – Performance Optimization, Security Hardening & Analytics

## Phase Objective
Harden FinWise into a production-ready system by improving performance,
security, reliability, and observability without adding new features.

## Dependencies
- Phase 3 completed and committed
- Alerts, ML integration, and dashboard stable
- JWT-based authentication in place
- Frontend and backend integrated

---

## Scope (IN)

### Performance
- Redis caching for dashboard and alerts
- Cache invalidation on data changes
- Graceful fallback when Redis is unavailable

### Security
- JWT authentication with access + refresh tokens
- HttpOnly refresh token cookies
- Silent token refresh on frontend
- CSRF and CORS tightening
- Secure cookie configuration

### Abuse Protection
- Rate limiting for authentication endpoints
- Throttling for dashboard and alerts APIs
- Brute-force and refresh abuse prevention

### Analytics & Observability
- PostHog integration (frontend)
- Tracking core product events
- Privacy-safe, non-PII analytics

---

## Scope (OUT)

- New product features
- UI redesign
- ML model changes
- Database schema changes
- Notification systems (email/SMS/push)

---

## Performance Deliverables

- Redis cache for:
  - `/api/dashboard/summary/`
  - `/api/alerts/`
- User-scoped and time-scoped cache keys
- Cache invalidation on transaction creation
- System functions correctly if Redis is down

---

## Security Deliverables

- JWT access tokens (short-lived)
- Refresh tokens stored in HttpOnly cookies
- Token rotation and logout support
- No tokens stored in localStorage
- Secure default authentication enforcement

---

## Abuse Protection Deliverables

- Strict throttling on:
  - Login endpoint
  - Refresh endpoint
- User-scoped throttling on:
  - Dashboard API
  - Alerts API
- Proper HTTP 429 responses on abuse

---

## Analytics Deliverables (PostHog)

### Events Tracked
- `login_success`
- `dashboard_viewed`
- `alerts_viewed`
- `alert_clicked`
- `logout`

### Analytics Rules
- No usernames, emails, or identifiers
- No financial values
- Only counts and boolean flags
- Analytics accessible only to project admins

---

## Non-Functional Constraints

- No breaking changes to APIs
- No database writes for analytics
- System must degrade gracefully on failures
- Frontend logic remains thin
- Backend remains source of truth

---

## Invariants (Must Not Break)

- Dashboard contract remains unchanged
- Alerts behavior remains deterministic
- ML remains optional and non-blocking
- Authentication remains secure under failure
- End users cannot access analytics

---

## Exit Criteria

- Redis caching verified with fallback
- JWT login, refresh, and logout tested end-to-end
- Silent token refresh working in frontend
- Rate limiting triggers correctly under abuse
- PostHog events visible in dashboard
- No PII captured
- Phase committed to Git

---

## Outcome

FinWise is now fast, secure, observable, and production-ready, with
industry-grade authentication, abuse protection, and analytics.
