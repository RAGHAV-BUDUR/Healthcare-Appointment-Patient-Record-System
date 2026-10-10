## 2. Test Items

The following modules of HAPRS v1.0 are under test (component names as in SAD §3.4):

- **Web Frontend** – screens and flows for Patient, Doctor, Receptionist and Admin
- **Auth & User Service** – registration, login, JWT, lockout, staff accounts
- **Patient Service** – patient profiles, MRN generation, duplicate warning, search
- **Doctor & Schedule Service** – doctor profiles, availability, slot generation, leave
- **Appointment Service** – slot search, booking, conflict prevention, reschedule, cancel, status changes
- **Medical Record Service** – charts, consultations, versioning, prescriptions, PDFs, care-relationship checks
- **Notification & Reporting Service** – email and in-app notifications, reminders, dashboard, CSV export
- **Audit Log** – logging of record access, denied attempts and admin actions
- **Database (PostgreSQL)** – constraints, indexes, encryption of sensitive columns, backup and restore
- **REST API** – all `/api/v1` endpoints, error formats and status codes
