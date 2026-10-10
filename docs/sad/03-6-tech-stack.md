### 3.6 Technology Stack & Data Stores

| Layer | Technology | Why |
|---|---|---|
| Frontend | React (mobile-responsive) | Component-based UI; one codebase for desktop and phone |
| Backend | Python 3.11, FastAPI, SQLAlchemy ORM, Pydantic | Fast REST APIs with automatic validation and Swagger docs |
| Database | PostgreSQL 15 | ACID transactions, row locking, partial unique indexes |
| Authentication | JWT bearer tokens (30 min), bcrypt (cost 12) | Stateless sessions; slow hashes resist password cracking |
| Encryption | TLS 1.2+ (Nginx reverse proxy); AES-256-GCM via Python `cryptography` | Data protected in transit and at rest |
| Background jobs | APScheduler | Nightly slot generation, 24-h reminders, NO_SHOW marking |
| Email | SMTP (MailHog in testing) | Standard, provider-independent |
| PDF | ReportLab | Prescription PDFs generated on the server |
| Deployment | Docker Compose (frontend, backend, database, Nginx) | Same setup on every laptop and the server |
| Tools | GitHub + GitHub Actions, PlantUML, Swagger, Postman, Pytest, Playwright, Locust, OWASP ZAP | Version control, CI, design, testing |

#### Data stores

Main tables: `users`, `patients`, `doctors`, `availability`, `slots`, `appointments`, `consultations`, `consultation_versions`, `prescriptions`, `prescription_items`, `notifications`, `audit_log`.

**Conflict prevention in the database (HAP-F-032):**

- Booking runs in one transaction: `SELECT … FROM slots WHERE id = :slotId FOR UPDATE` locks the slot row, so a second booking for the same slot waits until the first commits and then sees the slot as BOOKED.
- Inside the same transaction the service checks that the patient has no other appointment with status BOOKED or CHECKED_IN whose time overlaps the slot.
- A partial unique index is the final guard even if application code has a bug:
  `CREATE UNIQUE INDEX one_active_appt_per_slot ON appointments(slot_id) WHERE status IN ('BOOKED','CHECKED_IN');`

**Performance (HAP-NF-001, NF-002):** index on `slots(doctor_id, start)` for slot search; index on `appointments(patient_id, status)` for the overlap check; list endpoints are paginated (maximum 50 rows).

**Encryption at rest (HAP-SR-006):** diagnosis, symptoms, notes and medicine names are encrypted with AES-256-GCM before they are stored. The key is loaded from an environment variable / secrets file, never stored in the database.

**Versioning (HAP-F-044):** consultation edits insert a new row in `consultation_versions`; no UPDATE or DELETE is used on clinical data.

**Backups (HAP-NF-003):** nightly `pg_dump` to separate storage, kept for 30 days; a restore is tested monthly.
