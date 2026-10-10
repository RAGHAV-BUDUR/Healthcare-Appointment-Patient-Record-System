### 3.8 Traceability to Requirements

| Requirement(s) | Component(s) | Design section |
|---|---|---|
| HAP-F-001 – F-003 (accounts, roles) | Auth & User Service, Web Frontend | 3.4, 3.9 |
| HAP-F-010 – F-013 (patients) | Patient Service | 3.4 |
| HAP-F-020 – F-022 (doctors, availability, leave) | Doctor & Schedule Service | 3.4, 3.6 |
| HAP-F-030 – F-035 (appointments, conflict prevention) | Appointment Service, Database | 3.6, 4.2 (diagram 1), 4.3 |
| HAP-F-040 – F-044 (records, prescriptions, versioning) | Medical Record Service, Audit Log | 4.2 (diagram 2), 4.3 |
| HAP-F-050 – F-052 (notifications, dashboard, CSV) | Notification & Reporting Service, Email Gateway (SMTP) | 3.4 |
| HAP-NF-001, NF-002 (performance) | All services, Database indexes | 3.6 |
| HAP-NF-003 (availability, backups) | Database, deployment | 3.6, 3.7 |
| HAP-NF-004 (usability) | Web Frontend | 4.5 |
| HAP-NF-005 (maintainability) | All services (one package each) | 3.5 |
| HAP-SR-001, SR-002, SR-005 (passwords, tokens, lockout) | Auth & User Service | 3.9 |
| HAP-SR-003 (TLS) | Reverse proxy in front of the backend | 3.6, 3.9 |
| HAP-SR-004 (role and record checks) | Every service (shared authorisation dependency) | 3.9, 4.4 |
| HAP-SR-006 (encryption at rest) | Medical Record Service, Database | 3.6, 3.9 |
| HAP-SR-007 (audit log) | Audit Log | 3.9, 4.4 |
