### 4.4 Error Handling, Logging & Monitoring

#### Error handling

All errors use one JSON body:

```json
{ "error": { "code": "SLOT_TAKEN", "message": "This slot was just booked. Please choose another time." } }
```

| HTTP status | Error code(s) | When |
|---|---|---|
| 400 | `VALIDATION_ERROR` | Malformed request or bad query parameter |
| 401 | `UNAUTHENTICATED`, `TOKEN_EXPIRED` | No token, invalid signature, or token older than 30 minutes |
| 403 | `FORBIDDEN`, `NO_CARE_RELATIONSHIP` | Role not allowed; record belongs to someone else; doctor has no care relationship |
| 404 | `NOT_FOUND` | Resource does not exist (also used instead of 403 where revealing existence would leak data) |
| 409 | `SLOT_TAKEN`, `PATIENT_OVERLAP`, `CHANGE_WINDOW_CLOSED`, `INVALID_STATUS_TRANSITION`, `APPOINTMENT_NOT_CHECKED_IN` | Business-rule conflicts |
| 422 | `VALIDATION_ERROR` | Body fails field validation; the message names the field |
| 423 | `ACCOUNT_LOCKED` | 5 failed logins within the lock window |
| 429 | `RATE_LIMITED` | Rate limit exceeded |
| 500 | `INTERNAL_ERROR` | Unexpected failure; the message is generic and includes a request ID only |

Rules: messages are written for the end user and never contain stack traces, SQL, tokens or patient data; every response includes an `X-Request-ID` header so support staff can find the matching log line; database transactions are rolled back on any error; email failures never fail the user's request (they are retried in the background).

#### Logging

- Structured JSON logs with timestamp, level, request ID, user ID, role, endpoint, status code and duration.
- **Never logged:** passwords, JWTs, diagnoses, notes, prescription items, allergies, phone numbers.
- Security events (failed logins, lockouts, 403s, token errors) are logged at WARNING level.
- The audit log (HAP-SR-007) is separate from application logs and stored in its own append-only table.
- Application logs are kept for 90 days.

#### Monitoring

| Metric | Alert threshold |
|---|---|
| API p95 response time | > 2 s for 5 minutes (HAP-NF-001) |
| Error rate (5xx) | > 1% of requests over 5 minutes |
| Failed logins | > 50 per minute (possible attack) |
| 403 / `NO_CARE_RELATIONSHIP` rate | Sudden spike above normal daily level |
| Uptime check on `/health` | 2 consecutive failures, 1 minute apart (HAP-NF-003) |
| Email queue length | > 100 unsent messages |
| Nightly backup job | Any failure |
