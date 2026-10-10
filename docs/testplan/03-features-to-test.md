## 3. Features to be Tested

Features mapped to SRS requirement IDs:

**Authentication & Roles**
- HAP-F-001: Register / log in with email and password; JWT with role
- HAP-F-002: Role-based access to screens and endpoints
- HAP-F-003: Admin creates and deactivates staff accounts

**Patient Management**
- HAP-F-010: Patient registration and MRN generation
- HAP-F-011: Patient edits own profile; Receptionist registers walk-ins
- HAP-F-012: Duplicate patient warning
- HAP-F-013: Patient search

**Doctor & Schedule Management**
- HAP-F-020: Doctor profiles and slot duration
- HAP-F-021: Weekly availability and slot generation
- HAP-F-022: Doctor leave blocks slots and notifies patients

**Appointment Management**
- HAP-F-030: Search doctors and free slots
- HAP-F-031: Book a slot
- HAP-F-032: No double booking, no patient overlap, concurrency safety
- HAP-F-033: Reschedule / cancel up to 2 hours before
- HAP-F-034: Status lifecycle, check-in, automatic NO_SHOW
- HAP-F-035: Receptionist books on behalf of a patient

**Medical Records & Prescriptions**
- HAP-F-040: Doctor's daily list and chart access with care-relationship rule
- HAP-F-041: Consultation notes complete the appointment
- HAP-F-042: Prescriptions and PDF
- HAP-F-043: Patient's read-only view of own records
- HAP-F-044: Versioned, never-deleted records

**Notifications & Reports**
- HAP-F-050: Email / in-app notifications and 24-hour reminder
- HAP-F-051: Admin dashboard figures
- HAP-F-052: CSV export

**Non-functional**
- HAP-NF-001: 95% of API responses ≤ 2 s at 200 concurrent users
- HAP-NF-002: Free-slot search ≤ 1 s with 500 doctors / 50,000 appointments
- HAP-NF-003: ≥ 99.5% availability; backup restore within 4 h
- HAP-NF-004: First-time booking ≤ 3 minutes; works at 360 px; WCAG 2.1 AA contrast
- HAP-NF-005: ≥ 70% service-layer unit-test coverage

**Security**
- HAP-SR-001 to HAP-SR-007 (see §5.1 Security Validation)
