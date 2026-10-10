## 13. Test Case Management & Traceability

Test cases are stored one per file in `docs/testplan/test-cases/` and tracked in GitHub Issues during execution. The full RTM is SRS §8; the mapping below shows requirement → test cases.

| Requirement(s) | Test case(s) |
|---|---|
| HAP-F-001 (login, roles) | TC-AUTH-01 |
| HAP-F-002 (role-based access) | TC-AUTH-02 |
| HAP-F-010, F-011 (patient registration, profile) | TC-PAT-01 |
| HAP-F-021, F-022 (availability, leave) | TC-DOC-01 |
| HAP-F-030, F-031 (search, book) | TC-APT-01 |
| HAP-F-032 (conflict prevention) | TC-APT-02 |
| HAP-F-033, F-034 (reschedule/cancel window, status lifecycle) | TC-APT-03 |
| HAP-F-040 (care relationship) | TC-MR-03 |
| HAP-F-041, F-044 (consultation, versioning) | TC-MR-01 |
| HAP-F-042, F-043 (prescriptions, patient view) | TC-MR-02 |
| HAP-F-050 (notifications, reminder) | TC-NOT-01 |
| HAP-NF-001, NF-002 (performance) | TC-PERF-01 |
| HAP-SR-001, SR-005 (bcrypt, lockout) | TC-SEC-01 |
| HAP-SR-002, SR-004 (token expiry, record access) | TC-SEC-02 |
| HAP-SR-004 (server-side role checks) | TC-AUTH-02, TC-SEC-02, TC-MR-03 |
| HAP-SR-007 (audit log) | TC-MR-03 |

**Covered in sprint testing (no dedicated test case in this plan):** HAP-F-003, F-012, F-013, F-020, F-035, F-051, F-052. **Verified by other methods:** HAP-NF-003 (uptime reports, restore drill), HAP-NF-004 (usability session), HAP-NF-005 (coverage report), HAP-SR-003 (TLS scan), HAP-SR-006 (database inspection) — see §5 and §5.1.

New test cases use the owner's prefix (e.g. TC-APT-04) and are added to this table and to the RTM before execution.
