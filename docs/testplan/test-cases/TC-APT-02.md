### TC-APT-02 – Double booking and patient overlap are prevented

| Field | Content |
|---|---|
| TC ID | TC-APT-02 |
| Title | Double booking and patient overlap are prevented |
| Requirement(s) | HAP-F-032 |
| Type | Functional |
| Preconditions | One FREE slot S (10:00–10:15) for Dr. Menon; 20 different Patient accounts; Patient P1 already BOOKED at 10:00 the same day with Dr. Shah. |
| Test data | 20 Patient JWTs; slot S; a script that sends 20 `POST /api/v1/appointments` requests at the same moment. |
| Steps | 1. Send the 20 concurrent booking requests for slot S.<br>2. Count the response codes.<br>3. Query active appointments for slot S in the database.<br>4. As P1, try to book a different doctor's slot at 10:00 the same day. |
| Expected result | • Step 2: exactly 1 × 201 and 19 × 409 `SLOT_TAKEN`.<br>• Step 3: exactly one row with status BOOKED for slot S.<br>• Step 4: 409 `PATIENT_OVERLAP`; no appointment created. |
| Actual result | |
| Status | Not run |
