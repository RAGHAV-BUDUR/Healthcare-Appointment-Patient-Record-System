#### 4.3.2 Medical Record Service

Same conventions as 4.3.1 (base path `/api/v1`, bearer JWT, standard error body; `401` and `500` apply to every endpoint). Every successful call and every denied call writes an Audit Log entry.

**1. Get patient chart**
- **Endpoint:** `/patients/{id}/records`
- **Method:** GET
- **Roles:** Doctor (care relationship required), Patient (own ID only)
- **Request:** path parameter; optional `?include=versions`
- **Response:** `200` `{ "patient": { "mrn": "HAP-P-000077", "name": "Asha Rao", "age": 34, "bloodGroup": "B+", "allergies": ["Penicillin"] }, "visits": [ { "appointmentId": "a-4810", "date": "2026-09-02", "doctor": "Dr. K. Menon", "diagnosis": "Viral fever", "version": 1 } ], "prescriptions": [ { "prescriptionId": "rx-311", "date": "2026-09-02" } ] }`
- **Errors:** `403 NO_CARE_RELATIONSHIP` (doctor), `403 FORBIDDEN` (patient asking for another ID), `404 NOT_FOUND`

**2. Record consultation**
- **Endpoint:** `/appointments/{id}/consultation`
- **Method:** POST
- **Roles:** Doctor of that appointment
- **Request:** `{ "symptoms": "Fever, headache", "vitals": { "bp": "120/80", "pulse": 88, "tempC": 38.4, "weightKg": 61 }, "diagnosis": "Viral fever", "notes": "Fluids, rest; review in 5 days" }`
- **Response:** `201` `{ "consultationId": "c-920", "version": 1, "appointmentStatus": "COMPLETED" }`
- **Errors:** `409 APPOINTMENT_NOT_CHECKED_IN`, `409 INVALID_STATUS_TRANSITION` (consultation already exists — use PUT), `422 VALIDATION_ERROR` (missing diagnosis, vitals out of range), `403 FORBIDDEN` (another doctor's appointment), `404 NOT_FOUND`

**3. Edit consultation (new version)**
- **Endpoint:** `/consultations/{id}`
- **Method:** PUT
- **Roles:** Doctor who wrote the consultation
- **Request:** same body as POST plus `"changeReason": "Corrected diagnosis after lab report"`
- **Response:** `200` `{ "consultationId": "c-920", "version": 2, "previousVersions": [1] }`
- **Errors:** `422 VALIDATION_ERROR` (no `changeReason`), `403 FORBIDDEN`, `404 NOT_FOUND`

**4. Issue prescription**
- **Endpoint:** `/appointments/{id}/prescriptions`
- **Method:** POST
- **Roles:** Doctor of that appointment
- **Request:** `{ "items": [ { "medicine": "Paracetamol 650 mg", "dosage": "1 tablet", "frequency": "3 times a day", "durationDays": 5, "instructions": "After food" } ] }`
- **Response:** `201` `{ "prescriptionId": "rx-312", "items": 1, "pdfUrl": "/api/v1/prescriptions/rx-312/pdf" }`
- **Errors:** `422 VALIDATION_ERROR` (no items, missing dosage or duration, durationDays < 1), `409 APPOINTMENT_NOT_CHECKED_IN` (appointment is BOOKED, CANCELLED or NO_SHOW), `403 FORBIDDEN`, `404 NOT_FOUND`

**5. Get prescription**
- **Endpoint:** `/prescriptions/{id}`
- **Method:** GET
- **Roles:** the prescription's patient; doctors with a care relationship
- **Response:** `200` `{ "prescriptionId": "rx-312", "date": "2026-10-20", "doctor": "Dr. K. Menon", "patientMrn": "HAP-P-000077", "items": [ … ], "version": 1 }`
- **Errors:** `403 FORBIDDEN` / `403 NO_CARE_RELATIONSHIP`, `404 NOT_FOUND`

**6. Download prescription PDF**
- **Endpoint:** `/prescriptions/{id}/pdf`
- **Method:** GET
- **Roles:** as for "Get prescription"
- **Response:** `200` with `Content-Type: application/pdf` and `Content-Disposition: attachment; filename="rx-312.pdf"`
- **Errors:** `403 FORBIDDEN`, `404 NOT_FOUND`, `500 INTERNAL_ERROR` (PDF generation failed; logged without patient data)
