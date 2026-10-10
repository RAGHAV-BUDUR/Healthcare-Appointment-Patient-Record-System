### 3.9 Security Architecture

**Security layers**

1. **Transport:** Nginx terminates TLS 1.2/1.3; HTTP is redirected to HTTPS (HAP-SR-003).
2. **Identity:** bcrypt-hashed passwords (cost 12), 30-minute JWTs signed with HS256 and a server secret, lockout after 5 failures (HAP-SR-001, 002, 005).
3. **Authorisation:** a shared FastAPI dependency checks the role for every endpoint; services check record ownership and the doctor–patient care relationship (HAP-SR-004).
4. **Data protection:** AES-256-GCM encryption of diagnoses, notes and prescription items; key outside the database (HAP-SR-006).
5. **Accountability:** append-only audit log of record access, denied attempts and admin actions (HAP-SR-007).

#### Threat model (STRIDE)

| STRIDE category | Example threat in our system | Mitigation | Requirement |
|---|---|---|---|
| **Spoofing** | Attacker guesses a doctor's password or reuses a stolen token to pose as the doctor | bcrypt hashes; lockout after 5 failed logins for 15 min; JWT expiry 30 min; staff accounts only created by Admin | HAP-SR-001, SR-002, SR-005, HAP-F-003 |
| **Tampering** | A user edits a request to change someone else's appointment, or alters a diagnosis after the fact | Server-side validation of every field; ownership checks; clinical records are versioned, never updated in place; TLS prevents in-transit changes; ORM parameterised queries block SQL injection | HAP-SR-003, SR-004, HAP-F-044 |
| **Repudiation** | A doctor denies having viewed or changed a patient's record | Every READ, WRITE and DENIED event is written to an append-only audit log with user, role, record, time and IP; the app's DB role cannot UPDATE or DELETE audit rows | HAP-SR-007 |
| **Information disclosure** | A patient opens another patient's prescriptions by changing the ID in the URL; a database dump leaks diagnoses; logs contain health data | Record-level checks (403); care-relationship rule for doctors; AES-256 encryption at rest; no patient data or tokens in logs; error messages never reveal whether an email exists | HAP-SR-004, SR-006 |
| **Denial of service** | Bots flood the login or slot-search endpoints | Rate limiting at Nginx (10 login attempts per minute per IP, 100 requests per minute per user), pagination limits (50 rows), request size limits, lockout | HAP-SR-005, HAP-NF-001 |
| **Elevation of privilege** | A patient calls an admin endpoint, or sends `"role": "ADMIN"` in the registration body | Role is taken only from the signed token, never from the request body; self-registration always creates a Patient; every endpoint declares its allowed roles and is covered by the RBAC test matrix | HAP-SR-004, HAP-F-001, HAP-F-002 |
