## 5. Test Approach / Strategy

**Levels**

| Level | What is tested | Tools | Who |
|---|---|---|---|
| Unit | Functions and classes in each service package (slot generation, overlap check, status transitions, validation, encryption helpers) | Pytest, pytest-cov | Developers |
| Integration | Service ↔ database (transactions, row locks, unique index, encryption), service ↔ service (Appointment ↔ Medical Record, Notification), API endpoints | Pytest with a test PostgreSQL, Postman / Newman | Developers, QA |
| System | End-to-end flows through the UI: register → book → check in → consult → prescribe → patient downloads PDF | Playwright | QA |
| Acceptance (UAT) | Real users from each role perform their main tasks against the acceptance criteria in SRS §6 | Manual scripts | Product Owner, sample users |

**Types**

- **Functional testing** of every FR using the acceptance criteria in the SRS
- **Regression testing:** the full Pytest suite runs in GitHub Actions on every Pull Request; a PR cannot be merged while the `test` check fails
- **Concurrency testing** of booking (TC-APT-02)
- **Performance testing** with Locust (TC-PERF-01)
- **Security testing** (§5.1)
- **Usability testing:** 10 first-time users book an appointment on a phone; time and errors are recorded (HAP-NF-004)
- **Accessibility checks** with an automated contrast checker and keyboard-only navigation

**Entry criteria**

- The build to test is merged to `main` and the CI `test` check is green
- Test environment (§6) is up with seeded synthetic data
- Test cases for the features in the build are reviewed and approved
- No open Critical defect from the previous cycle

**Exit criteria**

- 100% of planned test cases executed
- All High-priority test cases passed
- 0 Critical and 0 High defects open
- NFR targets met (p95 ≤ 2 s, slot search ≤ 1 s, coverage ≥ 70%)
- RTM shows every requirement verified
