## 10. Risks and Mitigation

| Risk | Mitigation |
|---|---|
| Stable build delivered late, leaving little time for system testing | Run unit and integration tests in CI from the first sprint; request an early smoke build of each feature |
| Test environment or database unavailable | Docker Compose setup on every laptop as a backup environment; seed scripts to rebuild data in minutes |
| Concurrency defects are hard to reproduce manually | Automated concurrent booking script (TC-APT-02) run in every regression cycle |
| Email delivery cannot be verified with a real provider | MailHog captures all emails in the test environment |
| Performance test environment smaller than production | Document the difference; scale results; re-run on the production-like VM before release |
| Real patient data used by mistake | Only synthetic seed data allowed; review test data in PRs |
| Team member unavailable during execution | Every test case has an owner and a review partner who can run it |
| Scheduled jobs (reminders, NO_SHOW) take hours to trigger | Use a configurable test clock / manual job trigger in the test environment |
