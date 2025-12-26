# 📕 PHASE_0_CONTRACT.md

## 🔖 Phase Name
**Phase 0 – Foundations & Scaffolding**

---

## 🔗 Dependencies from Previous Phases
- None  
- This is the starting point of the project

---

## 📥 Inputs (What We Assume True)
- `PROJECT_BRAIN.md` is approved and frozen
- Tech stack is clearly defined in the PRD
- Solo developer workflow
- External ML models will **NOT** be implemented in this phase

---

## 📤 Outputs (What This Phase Must Guarantee)
By the end of **Phase 0**, the system must have:

- ✅ Working backend project bootstrapped
- ✅ Working frontend project bootstrapped
- ✅ Authentication skeleton (no full flows yet)
- ✅ Environment configuration in place
- ✅ Repository structure ready for future phases

---

## 🔒 Invariants (Must NOT Break Later)
The following rules must always hold true:

- Authentication approach = **JWT + HttpOnly Refresh Cookie**
- Backend must remain **stateless**
- No business logic in the frontend
- No ML calls in this phase
- No database schema changes without proper migration discipline

---

## 🧪 Test Criteria (Phase Exit Conditions)
**Phase 0 is considered DONE only if:**

- Backend server starts with **no errors**
- Frontend application starts and loads successfully
- Health check endpoint responds correctly
- Authentication endpoints respond (even if dummy responses)
- Environment variables load correctly

---

## ✅ Phase Status  
- ⬜ Completed  

