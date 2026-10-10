## 9. Roles and Responsibilities

| Role | Name | Responsibility |
|---|---|---|
| QA Lead | Prithviraj K | Prepare and maintain the test plan, coordinate execution, run performance tests, publish daily status and the Test Summary Report |
| Test Engineer | Prithviraj K, Parth Kale, Raghav Budur, P Manas Siddhardha | Design and execute their own test cases, log defects in GitHub Issues, re-test fixes |
| Security Test Engineer | Raghav Budur | Run the security validation in §5.1 (RBAC matrix, token, lockout, TLS, ZAP scan, encryption checks) |
| Dev Lead / Developer | Parth Kale (with all members as developers) | Keep the CI pipeline green, triage and fix defects, support test data setup |
| Product Owner | P Manas Siddhardha | Approve test results, run UAT with users, sign off release readiness |

Each test case owner is the person listed in the Requirements Registry §4; Pull Requests that change test cases are reviewed by the owner's review partner.
