## 11. Assumptions & Dependencies

**Assumptions**

- All test data is synthetic; no real patient data is available or needed.
- MailHog (or another SMTP sandbox) is available in the test environment.
- A stable build is merged to `main` with a green CI check before each test cycle.
- The test clock or job triggers can be adjusted so that time-based features (24-hour reminder, 2-hour change window, NO_SHOW after 30 minutes) can be tested without waiting.
- Testers have access to the test database for inspection (hashes, encryption, audit log).

**Dependencies**

- Docker, Python 3.11 and Node.js 20 installed on the test machines
- GitHub Actions minutes available for CI runs
- Locust, OWASP ZAP and testssl.sh installed for performance and security testing
- Developers available to fix Critical and High defects within the ageing targets in §14
- Sample users (fellow students acting as patients and staff) available for UAT and the usability session
