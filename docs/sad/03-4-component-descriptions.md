### 3.4 Component Descriptions

| Component | Responsibility | Main data | Requirements |
|---|---|---|---|
| **Web Frontend** | React single-page app for all four roles. Shows only the menus of the logged-in role, validates forms before sending, and displays API error messages in plain language. Holds the JWT in memory, never in local storage. | None persistent | All FRs, HAP-NF-004 |
| **Auth & User Service** | Registration, login, JWT issue and verification, password hashing, lockout, staff account creation and deactivation. Provides the shared authorisation dependency every other service calls before handling a request. | `users` | HAP-F-001–003, HAP-SR-001, 002, 004, 005 |
| **Patient Service** | Patient profiles, MRN generation, duplicate warning, patient search for staff. | `patients` | HAP-F-010–013 |
| **Doctor & Schedule Service** | Doctor profiles, weekly availability, nightly generation of slots for the next 30 days, leave days that block slots and trigger notifications. | `doctors`, `availability`, `slots` | HAP-F-020–022 |
| **Appointment Service** | Free-slot search, booking, rescheduling, cancellation, check-in, status transitions and automatic NO_SHOW. Owns the conflict-prevention transaction. Answers "does this doctor have a care relationship with this patient?" for the Medical Record Service. | `appointments` | HAP-F-030–035, HAP-NF-002 |
| **Medical Record Service** | Patient chart, consultation notes with versions, prescriptions, prescription PDFs, encryption and decryption of sensitive fields, care-relationship enforcement. | `consultations`, `consultation_versions`, `prescriptions`, `prescription_items` | HAP-F-040–044, HAP-SR-006 |
| **Notification & Reporting Service** | Turns appointment and leave events into email and in-app notifications, sends 24-hour reminders, computes dashboard figures and builds CSV exports. | `notifications` | HAP-F-050–052 |
| **Audit Log** | Append-only writer for READ, WRITE, DENIED and ADMIN events. The database role used by the application can only INSERT into this table. | `audit_log` | HAP-SR-007 |
| **Database (PostgreSQL)** | Single relational store for all components, with daily backups. | All tables | HAP-NF-003 |
| **Email Gateway (SMTP)** | External email provider reached over SMTP/STARTTLS. | – | HAP-F-050 |
