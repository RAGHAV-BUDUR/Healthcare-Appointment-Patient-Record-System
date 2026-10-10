### TC-PERF-01 – Load and response-time test

| Field | Content |
|---|---|
| TC ID | TC-PERF-01 |
| Title | Load and response-time test |
| Requirement(s) | HAP-NF-001, HAP-NF-002 |
| Type | Performance |
| Preconditions | Test environment matching production size; database seeded with 500 doctors, 10,000 patients and 50,000 appointments; Locust installed. |
| Test data | Locust script: 40% slot search, 20% booking, 20% list appointments, 10% login, 10% chart view; 200 users; ramp-up 2 min; duration 10 min. |
| Steps | 1. Start the Locust run with 200 concurrent users.<br>2. Record p95 response time per endpoint and the error rate.<br>3. Run 1,000 `GET /api/v1/slots` requests for random doctors and dates and record p95. |
| Expected result | • Step 2: overall p95 ≤ 2 s; error rate < 1%.<br>• Step 3: slot search p95 ≤ 1 s.<br>• No double bookings in the database after the run. |
| Actual result | |
| Status | Not run |
