## 2. Overall description

### 2.1 Product perspective

HAPRS is a new, self-contained web system that replaces paper registers and phone-based booking at a clinic. It follows a three-tier design: a React web frontend used from desktop and mobile browsers, a FastAPI backend that holds all business rules (booking, conflict prevention, access control), and a PostgreSQL database. It connects to one external system, an SMTP email gateway, for notifications. All parts communicate over HTTPS.

### 2.2 Major product functions

- **Accounts and roles:** patient self-registration, staff accounts created by the Admin, login, role-based menus, account lockout
- **Patient management:** patient profiles, MRN generation, duplicate warning, patient search
- **Doctor and schedule management:** doctor profiles, weekly availability, automatic slot generation, leave days
- **Appointment management:** search doctors and free slots, book, reschedule, cancel, check-in, completion and no-show tracking, conflict prevention
- **Medical records and prescriptions:** patient chart, consultation notes, vitals, diagnoses, prescriptions, PDF download, versioned records
- **Notifications and reports:** confirmations, cancellations, leave alerts, 24-hour reminders, admin dashboard, CSV export
- **Audit:** an append-only log of record access and admin actions

### 2.3 User roles and characteristics

| Role | Characteristics | Main goals |
|---|---|---|
| Patient | General public, any age; basic smartphone or computer skills; uses the system a few times a year | Book a convenient slot quickly, get reminders, see own prescriptions |
| Doctor | Medical professional, busy, uses the system all day during consultations | See today's schedule, open a patient's history in seconds, write notes and prescriptions fast |
| Receptionist | Front-desk staff, trained on the system, handles walk-ins and phone calls | Register patients, book on behalf of patients, check patients in |
| Admin (Hospital Administrator) | Trained staff member responsible for configuration and reporting | Manage staff accounts and doctor profiles, monitor utilisation, export reports |

### 2.4 Operating environment

- **Client:** latest two versions of Google Chrome, Microsoft Edge and Mozilla Firefox on Windows, macOS, Android and iOS; screen width 360 px and above
- **Server:** Ubuntu 22.04 LTS server or Docker containers; Python 3.11; FastAPI; PostgreSQL 15
- **Network:** internet or clinic LAN; HTTPS only
- **Email:** any SMTP provider with TLS; MailHog for testing

### 2.5 Constraints

- Personal and health data must be handled according to the principles of India's DPDP Act 2023: collection only for a stated purpose, consent, and access limited to people who need it. HIPAA-style safeguards (access control, audit, encryption) are used as a reference.
- Only open-source frameworks and tools may be used.
- Medical records must never be hard-deleted.
- The system is built by a four-person student team within one semester, which limits scope to the features in Section 1.2.
- Real patient data must not be used in development or testing; all test data is synthetic.
