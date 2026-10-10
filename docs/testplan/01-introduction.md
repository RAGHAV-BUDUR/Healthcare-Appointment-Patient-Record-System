# Software Test Plan (STP) – Healthcare Appointment & Patient Record System

**Project:** Healthcare Appointment & Patient Record System
**Version:** 1.0
**Authors:** Team 13 – P Manas Siddhardha, Prithviraj K, Parth Kale, Raghav Budur
**Date:** 10-10-2026
**Status:** Draft

## 1. Introduction

**Purpose:** This document defines the test plan for the Healthcare Appointment & Patient Record System (HAPRS) v1.0. It sets out the test objectives, scope, strategy, environment, schedule, deliverables, responsibilities, risks and traceability to the SRS, so that every functional, non-functional and security requirement is verified before release.

**Scope:** Testing covers authentication and roles, patient management, doctor schedules and slots, appointment booking with conflict prevention, rescheduling and cancellation, medical records and prescriptions, notifications and reminders, the admin dashboard and CSV export, performance, and security controls. Testing of third-party internals (SMTP provider, PDF library, PostgreSQL engine, browsers) and of out-of-scope features (billing, insurance, lab and pharmacy systems) is excluded.

**References:**
- HAPRS Software Requirements Specification (SRS) v1.0
- HAPRS Software Architecture & Design Specification (SAD) v1.0
- Requirements Registry (`docs/requirements-registry.md`)
- OWASP Top 10 (2021), OWASP ASVS 4.0
- IEEE 829 / ISO/IEC/IEEE 29119-3 (test documentation)
- Digital Personal Data Protection Act, 2023 (India)

**Definitions:**

| Term | Meaning |
|---|---|
| SRS | Software Requirements Specification |
| SAD | Software Architecture & Design Specification |
| RTM | Requirements Traceability Matrix |
| TC | Test case |
| MRN | Medical Record Number (Patient ID) |
| UAT | User Acceptance Testing |
| p95 | 95th-percentile response time |
| RBAC | Role-Based Access Control |
| JWT | JSON Web Token |
