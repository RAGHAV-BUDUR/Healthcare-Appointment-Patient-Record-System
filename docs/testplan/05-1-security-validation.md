### 5.1 Security Validation

| # | Check | How it is tested | Tool | Pass criterion | Req / TC |
|---|---|---|---|---|---|
| 1 | Password hashing | Inspect `users.password_hash`; search logs and API responses for test passwords | SQL, grep | Every hash starts with `$2b$12$`; no plaintext anywhere | HAP-SR-001 / TC-SEC-01 |
| 2 | Account lockout | 5 wrong passwords, then the correct one; retry after 15 min | Postman | 6th attempt → 423; success after 15 min | HAP-SR-005 / TC-SEC-01 |
| 3 | Token expiry and forgery | Reuse a token after 31 min; change payload; sign with a wrong key; send `alg: none` | Postman, jwt.io-style script | All rejected with 401 | HAP-SR-002 / TC-SEC-02 |
| 4 | RBAC matrix | Call every endpoint with every role's token (4 roles × all endpoints) | Pytest parametrised test | Each pair returns the expected 2xx or 403 | HAP-SR-004 / TC-AUTH-02 |
| 5 | Record-level access | Patient A requests B's records/prescriptions by ID; doctor without care relationship opens a chart | Pytest | 403 for every attempt; no data leaked | HAP-SR-004 / TC-SEC-02, TC-MR-03 |
| 6 | Audit logging | Perform chart view, edit, denied access and an admin export; inspect `audit_log`; try UPDATE/DELETE as the app DB user | SQL | One entry per action with all fields; UPDATE/DELETE refused | HAP-SR-007 / TC-MR-03 |
| 7 | Transport security | Scan the server; request `http://` URLs | testssl.sh | Only TLS 1.2/1.3; HTTP → 301 to HTTPS | HAP-SR-003 |
| 8 | Encryption at rest | Read `consultation_versions.diagnosis`, `notes`, `prescription_items.medicine` directly from the database | SQL | Ciphertext only; API shows plaintext to authorised doctor | HAP-SR-006 |
| 9 | Input validation and injection | Send SQL/HTML/script payloads in every text field (`' OR 1=1 --`, `<script>`); run an active scan | OWASP ZAP, Pytest | No SQL errors, no stored script executed, no High ZAP alerts | OWASP A03 |
| 10 | Sensitive data in logs and errors | Trigger errors and search logs/responses for tokens, diagnoses, phone numbers | grep | None found; 500 errors show only a request ID | HAP-SR-004, SAD §4.4 |
| 11 | Privilege escalation via request body | Register with `"role": "ADMIN"`; send `patientId` of someone else as a Patient | Postman | Role ignored (Patient created) or 403 | HAP-F-001, HAP-SR-004 |
| 12 | Rate limiting | 50 login requests in 1 minute from one IP | Locust | Requests above the limit get 429 `RATE_LIMITED` | SAD §3.9 (DoS) |
