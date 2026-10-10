## 4. Design

### 4.1 Design Overview

The system is designed as layered modules: a React frontend, a FastAPI backend made of seven service packages, and one PostgreSQL database.

**How a request flows**

1. The browser sends an HTTPS request with the JWT to `/api/v1/...`. Nginx terminates TLS and forwards it to FastAPI.
2. A shared authorisation dependency (from the Auth & User Service) validates the token's signature and expiry and loads the user's role. If the endpoint's allowed roles don't include it, the request stops with `403 FORBIDDEN`.
3. The router of the target service validates the request body with Pydantic models (`422 VALIDATION_ERROR` on failure).
4. The service function applies business rules, including **record-level checks**: a patient may only touch their own records; a doctor may open a chart only when a care relationship exists.
5. The repository layer reads and writes the database through SQLAlchemy inside a transaction. Sensitive medical fields are encrypted before writing and decrypted after reading.
6. Side effects that must not slow the user down (emails, in-app notifications) are handed to the Notification & Reporting Service and run in the background. Medical-record access and admin actions are written to the Audit Log in the same transaction.
7. A response is returned, or a standard error body (see 4.4).

**Key design decisions**

- **Slots as booking inventory:** availability rules are expanded into concrete slot rows, so conflict prevention becomes a simple row lock plus a unique index (see 3.6 and sequence diagram 1).
- **Immutable clinical records:** consultations and prescriptions are versioned instead of updated in place (HAP-F-044).
- **Server-side authorisation only:** the frontend hides menus for convenience, but every rule is enforced in the service layer (HAP-SR-004).
- **Scheduled jobs:** APScheduler generates slots nightly, sends reminders every 5 minutes for appointments 24 h away, and marks NO_SHOW 30 minutes after a slot ends.
