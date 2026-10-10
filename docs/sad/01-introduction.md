# Software Architecture and Design Specification (SAD)

**Project:** Healthcare Appointment & Patient Record System
**Version:** 1.0
**Authors:** Team 13 – P Manas Siddhardha, Prithviraj K, Parth Kale, Raghav Budur
**Date:** 10-10-2026
**Status:** Draft

## Revision history

| Version | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | 10-10-2026 | Team 13 | Initial architecture and design with diagrams |

## Approvals

| Role | Name | Signature / Date |
|---|---|---|
| Course Coordinator | | |
| Project Lead | P Manas Siddhardha | |

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software architecture and detailed design of the Healthcare Appointment & Patient Record System (HAPRS). It explains how the requirements in the SRS v1.0 are realised: the components and their responsibilities, the architecture pattern, the technology stack, the security architecture, the main interaction sequences and the API contracts.

### 1.2 Scope

The document covers the whole of version 1.0: authentication and roles, patient management, doctor schedules and slots, appointment booking with conflict prevention, medical records and prescriptions, notifications, reporting and audit logging. Billing, insurance, lab/pharmacy integration, telemedicine and HL7/FHIR interfaces are out of scope, as in the SRS.

### 1.3 Audience

Developers, QA engineers, security reviewers, the project team, course instructors and anyone maintaining the system later.

### 1.4 Definitions

| Term | Meaning |
|---|---|
| HAPRS | Healthcare Appointment & Patient Record System |
| MRN | Medical Record Number (Patient ID) |
| PHI | Protected Health Information |
| Slot | Bookable time interval of one doctor |
| Care relationship | The patient has or had an appointment with the doctor |
| RBAC | Role-Based Access Control |
| JWT | JSON Web Token |
| STRIDE | Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege |
| ORM | Object-Relational Mapper (SQLAlchemy) |
| TLS | Transport Layer Security |
| ADR | Architecture Decision Record |
