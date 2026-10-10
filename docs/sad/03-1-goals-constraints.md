## 3. Architecture

### 3.1 Goals & Constraints

**Goals**

| Goal | Measure | Requirement |
|---|---|---|
| Protect patient data | Only the patient, treating doctors and authorised staff can read records; sensitive fields encrypted at rest; every access logged | HAP-SO-1, HAP-SR-004, SR-006, SR-007 |
| Zero double bookings | One active appointment per slot and no overlapping appointments per patient, also under concurrent requests | HAP-F-032 |
| Responsive | 95% of API calls ≤ 2 s at 200 concurrent users; slot search ≤ 1 s | HAP-NF-001, NF-002 |
| Available | ≥ 99.5% monthly uptime; daily backup, RPO 24 h, RTO 4 h | HAP-NF-003 |
| Easy to use | First-time patient books in ≤ 3 minutes on a phone | HAP-NF-004 |
| Maintainable | One package per component; ≥ 70% service-layer test coverage | HAP-NF-005 |

**Constraints**

- Personal and health data handled according to the DPDP Act 2023 principles (purpose limitation, consent, need-to-know access).
- Medical records must never be deleted (versioning only).
- Open-source stack only: React, FastAPI, PostgreSQL.
- Single clinic deployment on one server or VM; no cloud-specific services.
- Four-person student team and one semester of development time.
- Only synthetic data may be used outside production.
