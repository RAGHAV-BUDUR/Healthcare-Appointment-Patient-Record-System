## 6. Quality attributes & Acceptance tests

### 6.1 Exit criteria for acceptance

- All High-priority functional requirements (HAP-F-001–003, 010, 011, 020–022, 030–034, 040–044, 050) are implemented and their test cases pass.
- No open defect of severity Critical or High.
- No failed acceptance test for any NFR (HAP-NF-001–005) or security requirement (HAP-SR-001–007).
- The RTM (Section 8) shows every requirement linked to at least one passed test case or an accepted verification method.

### 6.2 Acceptance test suites

| Suite | Quality attribute | Measurable acceptance test |
|---|---|---|
| Authentication & Roles | Security, correctness | TC-AUTH-01 and TC-AUTH-02 pass; every role/endpoint pair in the permission matrix returns the expected 200 or 403. |
| Patients | Correctness | TC-PAT-01 passes; 1,000 registrations produce 1,000 unique MRNs. |
| Schedules | Correctness | TC-DOC-01 passes; generated slots match availability exactly for 30 days. |
| Appointments | Correctness, integrity | TC-APT-01–03 pass; 20 concurrent bookings of one slot give exactly one success. |
| Medical Records | Integrity, confidentiality | TC-MR-01–03 pass; every edit creates a new version; every chart view has an audit entry. |
| Notifications | Reliability | TC-NOT-01 passes; 100% of test events produce an email within 60 s. |
| Performance | Performance | TC-PERF-01 passes: API p95 ≤ 2 s at 200 users; slot search p95 ≤ 1 s. |
| Security | Security | TC-SEC-01 and TC-SEC-02 pass; OWASP ZAP baseline scan reports no High alerts; TLS scan shows TLS 1.2+ only. |
| Usability | Usability | ≥ 8 of 10 first-time users book in ≤ 3 minutes; UI usable at 360 px; no WCAG 2.1 AA contrast failures. |
| Maintainability | Maintainability | Service-layer unit-test coverage ≥ 70% in the CI report. |
| Reliability | Availability | Restore drill completes in ≤ 4 h from the last daily backup. |
