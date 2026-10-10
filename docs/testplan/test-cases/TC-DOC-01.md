### TC-DOC-01 – Availability generates slots; leave blocks them

| Field | Content |
|---|---|
| TC ID | TC-DOC-01 |
| Title | Availability generates slots; leave blocks them |
| Requirement(s) | HAP-F-021, HAP-F-022 |
| Type | Functional |
| Preconditions | Doctor account with slot duration 15 min and no availability; one Patient account. |
| Test data | Availability: Monday 09:00–12:00. Leave: next Monday. Patient booked at 09:30 next Monday before leave is marked. |
| Steps | 1. As the Doctor, save Monday 09:00–12:00 availability.<br>2. Call `GET /api/v1/slots?doctorId=&date=<next Monday>`.<br>3. As the Patient, book 09:30 next Monday.<br>4. As the Doctor, mark next Monday as leave.<br>5. Call the slot search again and check the patient's notifications. |
| Expected result | • Step 2: exactly 12 FREE slots, 09:00 to 11:45 in 15-minute steps.<br>• Step 5: no FREE slots for that date; remaining slots are BLOCKED; the booked patient has a leave notification within 60 s; the 09:30 appointment is still BOOKED and listed for rescheduling. |
| Actual result | |
| Status | Not run |
