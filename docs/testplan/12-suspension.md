## 12. Suspension & Resumption Criteria

**Suspend testing if:**

- The test environment or database is unavailable for more than 4 hours
- The build is too unstable: more than 30% of the planned test cases are blocked
- A Critical defect blocks login, booking or chart access (core flows)
- A security defect is found that exposes patient data (testing of the affected area stops and the defect is escalated immediately)
- Test data is found to be corrupted or to contain real personal data

**Resume testing when:**

- The environment is restored and a smoke test (login, book, view chart) passes
- The blocking defects are fixed, merged and the CI `test` check is green
- The database is reset from the seed scripts
- Test cases affected by the fix are re-run first, followed by the regression suite
