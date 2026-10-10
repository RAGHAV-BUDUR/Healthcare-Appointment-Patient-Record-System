## 4. System features (detailed)

Each requirement below includes acceptance criteria and a reference test case. IDs follow HAP-F-###.

### 4.1 Authentication & Roles

**Description:** Let every user sign in securely with an email and password, assign each account exactly one of four roles (Patient, Doctor, Receptionist, Admin), and show each role only the features it is allowed to use.

| Req ID | Requirement (The system shall…) | Type | Priority | Source/Stakeholder | Acceptance criteria / Test case ref | Comments / Dependencies |
|---|---|---|---|---|---|---|
| HAP-F-001 | The system shall let a Patient self-register with email, password and mobile number, and shall let any active user log in with email and password, returning a JWT access token that carries the user's ID and role. | Functional | High | Patients, Clinic staff | AC-HAP-F-001: A valid email/password returns HTTP 200 with a JWT whose role claim matches the account; a wrong password returns 401 `UNAUTHENTICATED` without saying which field was wrong; Doctor, Receptionist and Admin accounts cannot be self-registered (403). Test: TC-AUTH-01 | Password rules: ≥ 8 characters with at least one letter and one digit. Depends on HAP-SR-001, HAP-SR-002, HAP-SR-005. |
| HAP-F-002 | The system shall restrict every screen and API endpoint to the roles listed for it, so that each role sees only its own menus and features. | Functional | High | Security, Admin | AC-HAP-F-002: For every endpoint in the role-permission matrix, a token of a non-permitted role receives 403 `FORBIDDEN` and the UI hides the corresponding menu items. Test: TC-AUTH-02 | Role checks run on the server (HAP-SR-004); hiding menus is only a convenience. |
| HAP-F-003 | The system shall let an Admin create Doctor and Receptionist accounts and deactivate or reactivate any non-Admin account; a deactivated user shall not be able to log in. | Functional | High | Admin | AC-HAP-F-003: An account created by the Admin can log in within 1 minute; after deactivation, login returns 403 and existing tokens are rejected on the next request; each change appears in the audit log. Test: covered in sprint testing | New staff receive a one-time password and must change it at first login. Logged per HAP-SR-007. |
