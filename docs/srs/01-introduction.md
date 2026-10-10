# Software Requirements Specification (SRS)

**Project:** Healthcare Appointment & Patient Record System
**Version:** 1.0
**Authors:** Team 13 – P Manas Siddhardha, Prithviraj K, Parth Kale, Raghav Budur
**Date:** 10-10-2026
**Status:** Draft

## Revision history

| Version | Date | Author | Change summary | Approval |
|---|---|---|---|---|
| 1.0 | 10-10-2026 | Team 13 | Initial draft with diagrams | Pending |

## Approvals

| Role | Name | Signature / Email | Date |
|---|---|---|---|
| Course Coordinator | | | |
| Project Lead | P Manas Siddhardha | | |

## Table of contents

1. Introduction
2. Overall description
3. External interface requirements
4. System features (detailed)
5. Non-functional requirements (detailed)
6. Quality attributes & acceptance tests
7. UML use-case diagrams
8. Requirements Traceability Matrix (RTM)

---

## 1. Introduction

### 1.1 Purpose

This document is the Software Requirements Specification for the Healthcare Appointment & Patient Record System (HAPRS). It defines the functional requirements, non-functional requirements, security requirements, external interfaces and acceptance criteria of the system. It is the baseline for the Software Architecture & Design document (SAD) and the Software Test Plan, and every requirement in it carries an ID that is traced to design components and test cases.

### 1.2 Scope

HAPRS is a web application used by a clinic or small hospital to run outpatient appointments and keep patient records.

In scope:

- Patient registration and profiles with a unique Patient ID (MRN)
- Doctor profiles, weekly availability, bookable time slots and leave
- Appointment search, booking, rescheduling, cancellation, check-in and status tracking, with automatic prevention of double bookings and overlapping appointments
- Medical records: consultation notes, diagnoses, vitals and prescriptions, with versioning and downloadable prescription PDFs
- Role-based access for four roles (Patient, Doctor, Receptionist, Admin) and record-level access rules
- Email and in-app notifications, appointment reminders, an admin dashboard and CSV reports
- An audit log of every medical-record access and every administrative action

Out of scope for version 1.0:

- Billing, payments and insurance claims
- Laboratory, radiology and pharmacy stock systems
- Video consultations (telemedicine)
- Integration with external health-record standards (HL7 / FHIR)
- Native mobile apps (the web UI is mobile-responsive instead)

### 1.3 Audience

- Developers who build the frontend, backend services and database
- QA engineers who design and run the tests in the Test Plan
- The project team and reviewers who check requirement coverage
- Course instructors and assessment evaluators

### 1.4 Definitions and acronyms

| Term | Meaning |
|---|---|
| HAPRS | Healthcare Appointment & Patient Record System |
| MRN | Medical Record Number – the unique Patient ID, format `HAP-P-000001` |
| EHR | Electronic Health Record |
| PHI | Protected Health Information – any health data linked to an identifiable patient |
| Slot | A bookable time interval of one doctor (default 15 minutes) |
| Care relationship | A doctor has a care relationship with a patient when the patient has or had an appointment with that doctor |
| RBAC | Role-Based Access Control |
| JWT | JSON Web Token used as the login session token |
| TLS | Transport Layer Security |
| API | Application Programming Interface |
| UI | User Interface |
| CSV | Comma-Separated Values file |
| SMTP | Simple Mail Transfer Protocol (email delivery) |
| DPDP Act | India's Digital Personal Data Protection Act, 2023 |
| RTO / RPO | Recovery Time Objective / Recovery Point Objective |
