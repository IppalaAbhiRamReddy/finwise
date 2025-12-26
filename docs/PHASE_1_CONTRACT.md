# 📕 PHASE_1_CONTRACT.md

## 🔖 Phase Name
**Phase 1 – Core Financial Data Models & CRUD APIs**

---

## 🔗 Dependencies from Previous Phases
- Phase 0 completed and committed
- Backend & frontend scaffolding is stable
- Authentication skeleton exists

---

## 📥 Inputs (Assumptions)
- Single-user personal finance per account
- All transactions are manually entered
- Categories are user-defined (not auto-generated)
- External ML systems do **NOT** write data

---

## 📤 Outputs (Must Be True at End of Phase 1)
By the end of **Phase 1**, the system must have:

- ✅ Persistent database schema
- ✅ Validated core data models
- ✅ CRUD APIs for:
  - Profile
  - Transactions
  - Budgets
  - Goals
- ✅ Basic API-level tests
- ✅ Clean, reproducible migrations
- ✅ Phase 1 committed to Git

---

## 🔒 Invariants (DO NOT BREAK)
The following rules must always hold:

- No business logic in frontend
- Backend validates **all** inputs
- No derived or aggregated data stored
- No alerts or ML logic
- Transactions are **append-only** (no silent mutation)

---

## 🧪 Phase Exit Criteria
**Phase 1 is complete only if:**

- Database migrations run cleanly
- All CRUD APIs work via Postman
- Invalid inputs are rejected with proper errors
- A new user with zero data does not error
- Database schema reflects **PRD scope only**

---

# 🧠 PHASE 1 — DATA MODEL DESIGN (VERY IMPORTANT)
**Design before coding. No exceptions.**

---

## 1️⃣ Core Models (Final List)

| Model        | Purpose                          |
|-------------|----------------------------------|
| User (Django) | Authentication                   |
| Profile     | User metadata                    |
| Transaction | Income & expense records         |
| Budget      | Spending limits                  |
| Goal        | Savings targets                  |

📌 **No more. No less.**

---

## 2️⃣ Model Responsibilities (Clear Separation)

### 👤 Profile
- Belongs to exactly one user
- Stores preferences and metadata
- Stores **no financial calculations**

---

### 💳 Transaction
- Atomic financial event
- Immutable by default
- Single source of truth for all calculations

---

### 📊 Budget
- Constraint, not enforcement
- Compared against transactions
- No alerting or enforcement logic

---

### 🎯 Goal
- Target-based saving intent
- Progress is **derived**, not stored
- No auto-tracking logic yet

---

## 3️⃣ Data Model Definitions (Conceptual)

### Profile
- user (OneToOne)
- monthly_income (decimal)
- currency
- created_at

---

### Transaction
- user (ForeignKey)
- type (income | expense)
- category
- amount
- date
- note (optional)
- created_at

---

### Budget
- user (ForeignKey)
- category
- limit_amount
- start_date
- end_date
- created_at

---

### Goal
- user (ForeignKey)
- name
- target_amount
- saved_amount
- deadline
- created_at

---

### ⚠️ Intentional Design Choices
- ❌ No computed fields stored
- ❌ No ML-related fields
- ❌ No alert-related fields

This is **intentional and non-negotiable**.

---

## 4️⃣ API Scope for Phase 1 (ONLY THESE)

| Entity      | APIs            |
|------------|------------------|
| Profile     | GET, UPDATE     |
| Transaction | CREATE, LIST    |
| Budget      | CREATE, LIST    |
| Goal        | CREATE, LIST    |

🚫 No DELETE  
🚫 No UPDATE for transactions  

---

## ⛔ WHAT WE DO NOT DO IN PHASE 1
Explicitly out of scope:

- ❌ Dashboards
- ❌ Aggregations
- ❌ Alerts
- ❌ Machine Learning
- ❌ Charts
- ❌ Analytics

---

## ✅ Phase Status
 
- ⬜ In Progress  