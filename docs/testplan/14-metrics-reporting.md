## 14. Test Metrics & Reporting

**Metrics collected**

| Metric | Definition | Target at exit |
|---|---|---|
| % test cases executed | executed ÷ planned × 100 | 100% |
| % passed / failed | passed ÷ executed × 100 | 100% of High-priority TCs passed |
| Defect density | defects found ÷ number of API endpoints (or KLOC) | Tracked per module |
| Defect ageing | days from defect opened to closed | Critical ≤ 1 day, High ≤ 3 days |
| Open defects by severity | count of Critical / High / Medium / Low | 0 Critical, 0 High |
| Requirement coverage | requirements with ≥ 1 passed test or accepted verification ÷ total requirements | 100% |
| Unit-test coverage | service-layer line coverage from `pytest --cov` | ≥ 70% (HAP-NF-005) |
| Performance | p95 response times from Locust | ≤ 2 s API, ≤ 1 s slot search |

**Reports**

- **Daily execution status** (during execution): test cases run / passed / failed / blocked, new defects, blockers — posted by the QA Lead in the team channel and as a GitHub Issue comment.
- **CI report:** every Pull Request shows the GitHub Actions test result and coverage.
- **Final Test Summary Report:** results per test case, open defects, metrics above, deviations from this plan and a release recommendation, signed off as in §15.
