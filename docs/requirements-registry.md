# Requirements Registry – Healthcare Appointment & Patient Record System

Project: Healthcare Appointment & Patient Record System · Version 1.0 · Team 13 · 10-10-2026

This registry fixes every requirement and test case ID used in the SRS, SAD and Test Plan. IDs are not changed or added without updating this file first.

All IDs carry the prefix **`HAP-`** (e.g. `HAP-F-031`). Acceptance criteria IDs are `AC-HAP-F-031`, etc.

## 1. Functional requirements (24)

| ID | Requirement (short) | Priority | Owner | Test case |
|---|---|---|---|---|
| HAP-F-001 | Users register/login with email + password; 4 roles (Patient, Doctor, Receptionist, Admin); only Patients self-register | High | Manas | TC-AUTH-01 |
| HAP-F-002 | Role-based access: each role sees only its own menus and features | High | Manas | TC-AUTH-02 |
| HAP-F-003 | Admin creates/deactivates Doctor and Receptionist accounts; deactivated users can't log in | High | Manas | – |
| HAP-F-010 | Patient registration: full name, date of birth, gender, phone, email, address, blood group, allergies, emergency contact; system generates a unique Patient ID (MRN, format `HAP-P-000001`) | High | Raghav | TC-PAT-01 |
| HAP-F-011 | Patient views/edits own profile (not MRN or DOB); Receptionist registers walk-in patients | High | Raghav | TC-PAT-01 |
| HAP-F-012 | System warns of a possible duplicate (same phone + date of birth) before creating a new patient | Medium | Raghav | – |
| HAP-F-013 | Receptionist/Admin search patients by name, MRN or phone; results in ≤ 1 s, max 50 per page | Medium | Raghav | – |
| HAP-F-020 | Admin adds/edits doctor: name, specialization, department, qualification, slot duration (10/15/20/30 min, default 15) | High | Raghav | – |
| HAP-F-021 | Doctor sets weekly availability (days, start–end time); system generates bookable slots of the doctor's slot duration for the next 30 days | High | Raghav | TC-DOC-01 |
| HAP-F-022 | Doctor marks leave dates; those slots become BLOCKED; patients already booked on those dates are notified and asked to reschedule | High | Raghav | TC-DOC-01 |
| HAP-F-030 | Patient searches doctors by specialization or name and sees FREE slots for a chosen date | High | Prithviraj | TC-APT-01 |
| HAP-F-031 | Patient books a FREE slot with a reason for visit; appointment created with status BOOKED and appears in the doctor's schedule | High | Prithviraj | TC-APT-01 |
| HAP-F-032 | No appointment conflicts: one active appointment per slot; a patient can't hold two overlapping active appointments; of concurrent bookings for one slot exactly one succeeds, the rest get 409 | High | Prithviraj | TC-APT-02 |
| HAP-F-033 | Patient reschedules or cancels up to 2 hours before the slot start; old slot becomes FREE immediately; later than that → 409 `CHANGE_WINDOW_CLOSED` | High | Prithviraj | TC-APT-03 |
| HAP-F-034 | Status lifecycle BOOKED → CHECKED_IN → COMPLETED, or CANCELLED / NO_SHOW; Receptionist checks patients in; system marks NO_SHOW 30 min after slot end if not checked in; invalid transitions → 409 | High | Prithviraj | TC-APT-03 |
| HAP-F-035 | Receptionist books/reschedules/cancels on behalf of a patient with the same conflict rules | Medium | Prithviraj | – |
| HAP-F-040 | Doctor views own daily appointment list and opens the chart (profile, allergies, past visits, prescriptions) only of patients who have or had an appointment with that doctor | High | Parth | TC-MR-03 |
| HAP-F-041 | Doctor records consultation notes (symptoms, diagnosis, vitals, notes) for a CHECKED_IN appointment; saving sets the appointment to COMPLETED | High | Parth | TC-MR-01 |
| HAP-F-042 | Doctor issues a prescription (medicine, dosage, frequency, duration in days, instructions) linked to the appointment; downloadable as PDF | High | Parth | TC-MR-02 |
| HAP-F-043 | Patient views own medical history and prescriptions read-only and downloads prescription PDFs | High | Parth | TC-MR-02 |
| HAP-F-044 | Medical records are never deleted; an edit creates a new version with author and timestamp, and all earlier versions stay viewable | High | Parth | TC-MR-01 |
| HAP-F-050 | Patient notified (email + in-app) within 1 minute of booking, reschedule, cancellation or doctor leave, plus a reminder 24 h before the appointment | High | Manas | TC-NOT-01 |
| HAP-F-051 | Admin dashboard: today's appointments per doctor, no-show rate (last 30 days), doctor slot utilization % | Medium | Manas | – |
| HAP-F-052 | Admin exports an appointment report for a date range as CSV | Low | Manas | – |

"–" means no dedicated test case in this plan. In the SRS acceptance-criteria column, write a measurable acceptance criterion and "Test: covered in sprint testing". Owners may add extra test cases with their own prefix (e.g. TC-APT-04); tell Manas so the RTM is updated.

## 2. Non-functional requirements (owner: Prithviraj)

| ID | Requirement | Category | Priority | Test case |
|---|---|---|---|---|
| HAP-NF-001 | 95% of API responses ≤ 2 s with 200 concurrent users | Performance | High | TC-PERF-01 |
| HAP-NF-002 | Free-slot search for one doctor and date returns in ≤ 1 s (95th percentile) with 500 doctors and 50,000 appointments in the database | Performance | High | TC-PERF-01 |
| HAP-NF-003 | ≥ 99.5% monthly availability; daily database backup with RPO ≤ 24 h and RTO ≤ 4 h | Reliability | High | – |
| HAP-NF-004 | A first-time patient can book an appointment in ≤ 3 minutes without training; UI works on screens ≥ 360 px wide and meets WCAG 2.1 AA colour contrast | Usability | Medium | – |
| HAP-NF-005 | Modular services; ≥ 70% unit-test coverage of the service layer | Maintainability | Medium | – |

## 3. Security (owner: Raghav)

| ID | Item | Priority | Test case |
|---|---|---|---|
| HAP-SO-1 | **Objective:** confidentiality of patient personal and medical data — only the patient, their treating doctors and authorised staff can see it | – | – |
| HAP-SO-2 | **Objective:** integrity and accountability of medical records, prescriptions and appointments — no undetected changes, every access traceable to a user | – | – |
| HAP-SR-001 | Passwords stored only as bcrypt hashes (cost factor 12) | High | TC-SEC-01 |
| HAP-SR-002 | JWT access tokens expire after 30 minutes; expired or tampered tokens get 401 | High | TC-SEC-02 |
| HAP-SR-003 | All traffic over HTTPS (TLS 1.2+); HTTP redirected to HTTPS | High | – |
| HAP-SR-004 | Role checks **and record-level checks** enforced on the server for every API call (a patient sees only own data; a doctor only patients with a care relationship) | High | TC-AUTH-02, TC-SEC-02, TC-MR-03 |
| HAP-SR-005 | Account locked for 15 minutes after 5 consecutive failed logins | High | TC-SEC-01 |
| HAP-SR-006 | Diagnosis, consultation notes and prescriptions encrypted at rest with AES-256 | High | – |
| HAP-SR-007 | Every read/write of a medical record and every admin action (account changes, doctor edits, exports) written to an append-only audit log with user ID, action, record ID, timestamp and IP | High | TC-MR-03 |

## 4. Test cases (14)

| TC ID | Covers | Type | Owner |
|---|---|---|---|
| TC-AUTH-01 | F-001 valid login returns JWT; wrong password → 401 | Functional | Manas |
| TC-AUTH-02 | F-002, SR-004 Patient token on an admin endpoint → 403 | Security | Manas |
| TC-NOT-01 | F-050 booking confirmation within 1 min; 24-h reminder sent | Functional | Manas |
| TC-PAT-01 | F-010, F-011 register patient → MRN generated; missing mandatory field → 422; patient edits own phone | Functional | Raghav |
| TC-DOC-01 | F-021, F-022 weekly availability generates correct slots; leave date shows no FREE slots and booked patient is notified | Functional | Raghav |
| TC-SEC-01 | SR-001, SR-005 password stored as bcrypt hash; lockout after 5 failures for 15 min | Security | Raghav |
| TC-SEC-02 | SR-002, SR-004 expired/forged token → 401; Patient A requesting Patient B's records → 403 | Security | Raghav |
| TC-APT-01 | F-030, F-031 search shows FREE slots; booking → BOOKED and visible in doctor's schedule | Functional | Prithviraj |
| TC-APT-02 | F-032 20 concurrent bookings of one slot → exactly 1 × 201, 19 × 409 `SLOT_TAKEN`; overlapping booking by same patient → 409 `PATIENT_OVERLAP` | Functional | Prithviraj |
| TC-APT-03 | F-033, F-034 cancel ≥ 2 h before → slot FREE; cancel < 2 h → 409; check-in/complete transitions; COMPLETED → BOOKED rejected | Functional | Prithviraj |
| TC-PERF-01 | NF-001, NF-002 Locust load test, 200 users, 10 min | Performance | Prithviraj |
| TC-MR-01 | F-041, F-044 consultation saved → appointment COMPLETED; edit creates version 2, version 1 still readable | Functional | Parth |
| TC-MR-02 | F-042, F-043 prescription created; patient sees it read-only and downloads PDF | Functional | Parth |
| TC-MR-03 | F-040, SR-004, SR-007 doctor with no care relationship → 403 `NO_CARE_RELATIONSHIP`; attempt recorded in audit log | Security | Parth |

**Test case format** (one file per test case, `docs/testplan/test-cases/TC-XXX-NN.md`):

| Field | Content |
|---|---|
| TC ID | TC-APT-01 |
| Title | … |
| Requirement(s) | HAP-F-030, HAP-F-031 |
| Type | Functional / Performance / Security |
| Preconditions | … |
| Test data | … (made-up data only) |
| Steps | 1. … 2. … |
| Expected result | … (measurable) |
| Actual result | (blank) |
| Status | Not run |
