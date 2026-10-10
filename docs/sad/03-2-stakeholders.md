### 3.2 Stakeholders & Concerns

| Stakeholder | Concerns | Addressed by |
|---|---|---|
| Patients | Privacy of their health data; quick and simple booking; reminders; access to their own prescriptions | RBAC + care-relationship checks (3.9), booking flow in ≤ 4 screens (4.5), Notification & Reporting Service |
| Doctors | Accurate schedule; no double bookings; fast access to patient history; quick note and prescription entry | Conflict-prevention transaction (3.6), chart view with allergies first, sequence diagram 2 (4.2) |
| Receptionists | Fast walk-in registration and check-in; booking on behalf of patients | Patient Service, Appointment Service status API (4.3) |
| Admin / Hospital management | Doctor utilisation, no-show rate, staff account control, reports, compliance | Dashboard and CSV export, Audit Log |
| Regulators / auditors | Traceability of every access to health data; records never lost | Append-only audit log, versioned records, backups |
| Developers | Clear module boundaries, testability, simple deployment | Layered architecture (3.5), one package per component, Docker Compose |
| Testers | Stable APIs, seed data, measurable acceptance criteria | API design (4.3), Test Plan, synthetic data set |
