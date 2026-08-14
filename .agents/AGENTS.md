# AGENTS.md — Indian Navy MDA System Agent Rules (Ponytail Enforced)

This repository adopts the **Ponytail Decision Ladder** ("laziest senior developer" mindset). All AI coding agents operating in this workspace MUST evaluate solutions against this ladder before proposing or writing code.

---

## The Ponytail Decision Ladder

Before writing any new code or creating files, evaluate these 7 rungs in sequence:

1. **Does this need to exist? (YAGNI)**
   - Do not add speculative features, unused parameters, or unrequested abstractions.
2. **Already in this codebase?**
   - **Backend**: Reuse existing modules in `indian/backend/` (`routes/`, `services/`, `models/`) and `indian/ml_engine/` (`autoencoder.py`, `ekf_tracker.py`, `anomaly_detector.py`).
   - **Frontend**: Reuse existing components in `indian/frontend/src/` (`components/`, `hooks/`, `utils/`).
3. **Stdlib does it?**
   - Use Python standard libraries (`math`, `datetime`, `json`, `asyncio`, `typing`) or JavaScript built-ins before adding packages.
4. **Native platform feature?**
   - Prefer native HTML5 elements (`<input type="date">`, `<dialog>`, native CSS) over complex third-party UI libraries.
5. **Installed dependency?**
   - Use existing dependencies already listed in `requirements.txt` (FastAPI, PyTorch, Scikit-Learn, NumPy, SciPy) and `package.json` (React, Leaflet, Recharts, Lucide-React). Do NOT add new dependencies unless strictly necessary.
6. **Can it be one line?**
   - If a standard function or comprehension replaces 20 lines of loops, use the concise form.
7. **Only then: write the minimum necessary code.**
   - Write simple, direct, readable code.

---

## Mandatory System Contracts & Safeguards

The Ponytail ladder promotes lazy solutions, but NEVER negligent code. The following safety and domain contracts MUST always be preserved:

- **Authentication / Lock Screen**: Preserve the tactical clearance passcode (`NAVY2026`).
- **Telemetry & Safety**: Ensure non-null checks on vessel coordinates, AIS data streams, and WebSocket payload schemas.
- **Error Handling**: Do not swallow exceptions silently; maintain proper FastAPI status codes and user-facing alert state.
