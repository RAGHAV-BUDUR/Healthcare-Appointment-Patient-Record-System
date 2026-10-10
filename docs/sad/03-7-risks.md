### 3.7 Risks & Mitigations

| # | Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|---|
| 1 | Two users book the same slot at the same moment (race condition) | Double booking, angry patients | High | Row lock (`SELECT … FOR UPDATE`) in one transaction plus a partial unique index on active appointments per slot; concurrency test TC-APT-02 |
| 2 | Breach of patient data (stolen database dump, SQL injection, stolen token) | Legal and reputational damage | Medium | AES-256 encryption of sensitive fields, parameterised queries through the ORM, TLS everywhere, 30-minute tokens, RBAC and record-level checks, OWASP ZAP scans |
| 3 | Email provider outage or emails marked as spam | Patients miss confirmations and reminders | Medium | Background retry 3 × at 5-minute intervals, in-app notifications as fallback, SPF/DKIM on the sending domain |
| 4 | Doctor marks leave on a busy day | Many patients must be moved at once | Medium | Leave blocks free slots immediately, affected patients are notified and listed for the Receptionist to reschedule (HAP-F-022) |
| 5 | Loss of the encryption key | Encrypted records become unreadable | Low | Key kept outside the database with an offline backup copy held by the Admin; documented restore procedure |
| 6 | Server or database failure | System unavailable during clinic hours | Low | Docker Compose redeploy in minutes, nightly backups with monthly restore drill (RTO 4 h, RPO 24 h) |
| 7 | Performance drops as appointment history grows | Slow slot search and charts | Medium | Indexes on `slots(doctor_id, start)` and `appointments(patient_id, status)`, pagination, load test TC-PERF-01 |
| 8 | A team member becomes unavailable near a deadline | Sections or features left unfinished | Medium | One owner and one reviewer per area, small commits, shared requirement registry so anyone can pick up a section |
