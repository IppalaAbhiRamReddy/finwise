📘 PROJECT_BRAIN.md (Draft v1)

## 1️⃣ Project Vision
FinWise is a secure, high-performance personal finance management platform that helps users track income and expenses, manage budgets and savings goals, and receive intelligent insights and alerts. The system prioritizes financial awareness, reliability, and clean UX, while integrating external ML models safely with graceful fallbacks.

---

## 2️⃣ Core Assumptions
- Users manually enter all financial transactions  
- External ML models are read-only consumers (no in-app training)  
- Internet connectivity is required  
- Single-user personal finance (no shared accounts)  
- Data accuracy depends on user input  

---

## 3️⃣ System Architecture (Logical)

**Frontend (React)**
- Auth  
- Dashboard  
- Budgets  
- Goals  
- Transactions  
- Reports  

⬇️  

**Backend API (Django + DRF)**
- Auth & RBAC  
- Business Logic  
- Validation & Alerts  
- ML Adapter Layer  
- Caching (Redis)  
- Background Tasks (Celery)  

⬇️  

**Database**
- PostgreSQL  

⬇️  

**External ML Services / Models**

---

## 4️⃣ Data Domains (High-Level)
- User  
- Profile  
- Transaction  
- Budget  
- Goal  
- Alert  
- ML Insight (derived, not stored permanently)  
- Analytics Events (PostHog)

---

## 5️⃣ ML Integration Contract (CRITICAL)
- Backend calls ML only via adapter layer  
- ML responses are optional  
- If ML fails → rule-based insights are used  
- No ML call blocks dashboard rendering  
- ML outputs are never trusted blindly  

---

## 6️⃣ Non-Functional Invariants (DO NOT BREAK)
- Dashboard must load for new users (no empty-state crashes)  
- Auth tokens use JWT + HttpOnly refresh cookies  
- No ML failure can crash the app  
- Performance targets must be met (<200ms cached)  
- APIs remain stateless  

---

## 7️⃣ Out-of-Scope (Strict)
- Offline mode  
- Auto transaction categorization  
- In-app ML training  
- Forecast graphs  
- Attachments  

---

## 8️⃣ Success Metrics (Engineering Perspective)
- Zero 500 errors for new users  
- Dashboard renders with zero data  
- All alerts are explainable  
- ML fallback coverage = 100%  