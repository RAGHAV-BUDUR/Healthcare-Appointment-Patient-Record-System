## 8. Requirements Traceability Matrix (RTM)

Status: N = not tested yet, P = passed, A = accepted. Design spec references point to sections of the SAD v1.0.

| Req ID | Requirement short | Section ref / Design Spec | Module | Test case(s) | Status (N/P/A) | Comments |
|---|---|---|---|---|---|---|
| HAP-F-001 | Register / login, 4 roles | SRS 4.1 / SAD 3.4 | Auth & User Service | TC-AUTH-01 | N | |
| HAP-F-002 | Role-based access | SRS 4.1 / SAD 3.4, 3.9 | Auth & User Service | TC-AUTH-02 | N | |
| HAP-F-003 | Admin manages staff accounts | SRS 4.1 / SAD 3.4 | Auth & User Service | Sprint testing | N | |
| HAP-F-010 | Patient registration + MRN | SRS 4.2 / SAD 3.4 | Patient Service | TC-PAT-01 | N | |
| HAP-F-011 | Edit own profile; walk-in registration | SRS 4.2 / SAD 3.4 | Patient Service | TC-PAT-01 | N | |
| HAP-F-012 | Duplicate patient warning | SRS 4.2 / SAD 3.4 | Patient Service | Sprint testing | N | |
| HAP-F-013 | Patient search | SRS 4.2 / SAD 3.4 | Patient Service | Sprint testing | N | |
| HAP-F-020 | Doctor profiles | SRS 4.3 / SAD 3.4 | Doctor & Schedule Service | Sprint testing | N | |
| HAP-F-021 | Weekly availability → slots | SRS 4.3 / SAD 3.4 | Doctor & Schedule Service | TC-DOC-01 | N | |
| HAP-F-022 | Doctor leave | SRS 4.3 / SAD 3.4 | Doctor & Schedule Service | TC-DOC-01 | N | |
| HAP-F-030 | Search doctors and free slots | SRS 4.4 / SAD 4.3 Appointment API | Appointment Service | TC-APT-01 | N | |
| HAP-F-031 | Book appointment | SRS 4.4 / SAD 4.2 diagram 1, 4.3 | Appointment Service | TC-APT-01 | N | |
| HAP-F-032 | Conflict prevention | SRS 4.4 / SAD 3.6, 4.2 diagram 1 | Appointment Service | TC-APT-02 | N | |
| HAP-F-033 | Reschedule / cancel ≥ 2 h | SRS 4.4 / SAD 4.3 Appointment API | Appointment Service | TC-APT-03 | N | |
| HAP-F-034 | Status lifecycle, check-in, no-show | SRS 4.4 / SAD 4.3 Appointment API | Appointment Service | TC-APT-03 | N | |
| HAP-F-035 | Receptionist books for patient | SRS 4.4 / SAD 4.3 Appointment API | Appointment Service | Sprint testing | N | |
| HAP-F-040 | Doctor schedule and patient chart | SRS 4.5 / SAD 4.2 diagram 2, 4.3 | Medical Record Service | TC-MR-03 | N | |
| HAP-F-041 | Consultation notes | SRS 4.5 / SAD 4.2 diagram 2, 4.3 | Medical Record Service | TC-MR-01 | N | |
| HAP-F-042 | Prescriptions + PDF | SRS 4.5 / SAD 4.3 Medical Record API | Medical Record Service | TC-MR-02 | N | |
| HAP-F-043 | Patient views own records | SRS 4.5 / SAD 4.3 Medical Record API | Medical Record Service | TC-MR-02 | N | |
| HAP-F-044 | Versioned, never-deleted records | SRS 4.5 / SAD 3.6 | Medical Record Service | TC-MR-01 | N | |
| HAP-F-050 | Notifications and reminders | SRS 4.6 / SAD 3.4 | Notification & Reporting Service | TC-NOT-01 | N | |
| HAP-F-051 | Admin dashboard | SRS 4.6 / SAD 3.4 | Notification & Reporting Service | Sprint testing | N | |
| HAP-F-052 | CSV report export | SRS 4.6 / SAD 3.4 | Notification & Reporting Service | Sprint testing | N | |
| HAP-NF-001 | API p95 ≤ 2 s at 200 users | SRS 5 / SAD 3.1, 3.6 | All services | TC-PERF-01 | N | |
| HAP-NF-002 | Slot search p95 ≤ 1 s | SRS 5 / SAD 3.6 | Appointment Service, Database | TC-PERF-01 | N | |
| HAP-NF-003 | ≥ 99.5% availability, backups | SRS 5 / SAD 3.6, 3.7 | Database, deployment | Ops reports | N | |
| HAP-NF-004 | Booking in ≤ 3 min, 360 px | SRS 5 / SAD 4.5 | Web Frontend | Usability test | N | |
| HAP-NF-005 | ≥ 70% service-layer coverage | SRS 5 / SAD 3.5 | All services | Coverage report | N | |
| HAP-SR-001 | bcrypt password hashes | SRS 5.1 / SAD 3.9 | Auth & User Service | TC-SEC-01 | N | |
| HAP-SR-002 | JWT 30-minute expiry | SRS 5.1 / SAD 3.9 | Auth & User Service | TC-SEC-02 | N | |
| HAP-SR-003 | HTTPS / TLS 1.2+ | SRS 5.1 / SAD 3.9 | Deployment (reverse proxy) | TLS scan (TP 5.1) | N | |
| HAP-SR-004 | Server-side role and record checks | SRS 5.1 / SAD 3.9 | All services | TC-AUTH-02, TC-SEC-02, TC-MR-03 | N | |
| HAP-SR-005 | Lockout after 5 failures | SRS 5.1 / SAD 3.9 | Auth & User Service | TC-SEC-01 | N | |
| HAP-SR-006 | AES-256 encryption at rest | SRS 5.1 / SAD 3.6, 3.9 | Medical Record Service, Database | DB inspection (TP 5.1) | N | |
| HAP-SR-007 | Append-only audit log | SRS 5.1 / SAD 3.9 | Audit Log | TC-MR-03 | N | |
