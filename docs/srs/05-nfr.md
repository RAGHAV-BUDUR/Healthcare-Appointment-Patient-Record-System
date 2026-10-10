## 5. Non-functional requirements (detailed)

NFRs below are measurable and tied to the Test Plan. IDs follow HAP-NF-###.

| Req ID | Requirement | Category | Priority | Acceptance criteria / Measurement |
|---|---|---|---|---|
| HAP-NF-001 | 95% of API responses shall complete within 2 seconds with 200 concurrent users performing a realistic mix of logins, slot searches, bookings and chart views. | Performance | High | Locust run of 10 minutes at 200 users on the test environment: 95th-percentile response time ≤ 2 s and error rate < 1%. Test: TC-PERF-01 |
| HAP-NF-002 | A free-slot search for one doctor and one date shall return within 1 second (95th percentile) with 500 doctors and 50,000 appointments in the database. | Performance | High | Measured during TC-PERF-01 on a seeded database of 500 doctors and 50,000 appointments: p95 ≤ 1 s for `GET /slots`. Test: TC-PERF-01 |
| HAP-NF-003 | The system shall be available at least 99.5% of each month, and the database shall be backed up daily with a recovery point objective (RPO) of 24 hours and a recovery time objective (RTO) of 4 hours. | Reliability | High | Uptime monitoring shows ≥ 99.5% per month (≤ 3 h 39 min downtime); a monthly restore drill rebuilds the database from the latest backup in ≤ 4 h. Test: operations reports |
| HAP-NF-004 | A first-time patient shall be able to book an appointment within 3 minutes without training; the UI shall work on screens 360 px wide and above and meet WCAG 2.1 AA colour-contrast rules. | Usability | Medium | In a usability session, at least 8 of 10 first-time users complete a booking in ≤ 3 min; no horizontal scrolling at 360 px; an accessibility checker reports no contrast failures. Test: usability test (sprint testing) |
| HAP-NF-005 | Each service shall be a separate module with its own tests, and unit tests shall cover at least 70% of service-layer code. | Maintainability | Medium | `pytest --cov` report on the service layer shows ≥ 70% line coverage; each component in SAD §3.4 maps to its own package. Test: coverage report in CI |
