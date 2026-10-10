### 5.1 Security

#### 5.1.1 Security Objectives

| ID | Objective |
|---|---|
| HAP-SO-1 | **Confidentiality of patient data:** personal details and medical records (diagnoses, notes, prescriptions) can be read only by the patient, by doctors who have a care relationship with the patient, and by staff whose role requires it. |
| HAP-SO-2 | **Integrity and accountability:** medical records, prescriptions and appointments cannot be changed without detection, are never silently deleted, and every access or change can be traced to a specific user and time. |

#### 5.1.2 Security Requirements

| Req ID | Requirement (shall…) | Type | Priority | Acceptance criteria / Test case ref |
|---|---|---|---|---|
| HAP-SR-001 | The system shall store passwords only as bcrypt hashes with a cost factor of 12 and shall never log or return a password. | Security | High | The `password_hash` column starts with `$2b$12$` for every user; no plaintext password appears in the database, logs or API responses. Test: TC-SEC-01 |
| HAP-SR-002 | The system shall issue JWT access tokens that expire 30 minutes after issue and shall reject expired, unsigned or tampered tokens with 401. | Security | High | A token used 31 minutes after issue returns 401 `TOKEN_EXPIRED`; a token with a modified payload or signature returns 401 `UNAUTHENTICATED`. Test: TC-SEC-02 |
| HAP-SR-003 | The system shall serve all traffic over HTTPS using TLS 1.2 or higher and shall redirect HTTP requests to HTTPS. | Security | High | A TLS scan shows only TLS 1.2/1.3 enabled; `http://` requests receive a 301 redirect to `https://`. Test: TLS scan in Test Plan §5.1 |
| HAP-SR-004 | The system shall enforce role checks and record-level checks on the server for every API call: a Patient may access only their own data, a Doctor only patients with whom they have a care relationship, and staff only the functions of their role. | Security | High | Every endpoint in the role-permission matrix rejects a non-permitted role with 403; Patient A requesting Patient B's records gets 403; a doctor without a care relationship gets 403 `NO_CARE_RELATIONSHIP`. Test: TC-AUTH-02, TC-SEC-02, TC-MR-03 |
| HAP-SR-005 | The system shall lock an account for 15 minutes after 5 consecutive failed login attempts and shall reset the counter after a successful login. | Security | High | The 6th attempt within the lock period returns 423 `ACCOUNT_LOCKED` even with the correct password; login succeeds again after 15 minutes. Test: TC-SEC-01 |
| HAP-SR-006 | The system shall encrypt diagnoses, consultation notes and prescription items at rest using AES-256-GCM, with the key held outside the database. | Security | High | Reading the columns directly with SQL shows ciphertext only; the API returns the correct plaintext to an authorised doctor. Test: database inspection in Test Plan §5.1 |
| HAP-SR-007 | The system shall write every read or write of a medical record, every denied access attempt and every admin action (account changes, doctor profile edits, exports) to an append-only audit log containing user ID, role, action, record ID, timestamp and IP address. | Security | High | Opening a patient chart creates exactly one READ entry; a denied attempt creates a DENIED entry; the application database user cannot UPDATE or DELETE audit rows. Test: TC-MR-03 |
