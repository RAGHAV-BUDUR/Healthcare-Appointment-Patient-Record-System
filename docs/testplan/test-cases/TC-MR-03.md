### TC-MR-03 – Doctor without care relationship is denied and the attempt is logged

| Field | Content |
|---|---|
| TC ID | TC-MR-03 |
| Title | Doctor without care relationship is denied and the attempt is logged |
| Requirement(s) | HAP-F-040, HAP-SR-004, HAP-SR-007 |
| Type | Security |
| Preconditions | Patient P5 has appointments only with Dr. Menon. Dr. Shah has never seen P5. Read access to `audit_log`. |
| Test data | Dr. Menon JWT, Dr. Shah JWT, P5's patient ID. |
| Steps | 1. As Dr. Menon, `GET /api/v1/patients/P5/records`.<br>2. As Dr. Shah, `GET /api/v1/patients/P5/records`.<br>3. Query `audit_log` for P5 in the test window.<br>4. Try to `UPDATE` or `DELETE` an audit row using the application's database user. |
| Expected result | • Step 1: 200 with P5's chart.<br>• Step 2: 403 `NO_CARE_RELATIONSHIP`; no patient data in the body.<br>• Step 3: one READ entry for Dr. Menon and one DENIED entry for Dr. Shah, each with user ID, role, record ID, timestamp and IP.<br>• Step 4: permission denied by the database. |
| Actual result | |
| Status | Not run |
