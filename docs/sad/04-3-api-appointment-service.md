### 4.3 API Design

All endpoints use base path `/api/v1`, JSON bodies and the header `Authorization: Bearer <JWT>`. Errors use the body `{ "error": { "code": "STRING_CODE", "message": "Readable message" } }`. Every endpoint can also return `401 UNAUTHENTICATED / TOKEN_EXPIRED` and `500 INTERNAL_ERROR`; these are not repeated below.

#### 4.3.1 Appointment Service

**1. List free slots**
- **Endpoint:** `/slots?doctorId={doctorId}&date={YYYY-MM-DD}`
- **Method:** GET
- **Roles:** Patient, Receptionist
- **Request:** query parameters only
- **Response:** `200` `{ "doctorId": "d-12", "date": "2026-10-20", "slots": [ { "slotId": "s-901", "start": "09:00", "end": "09:15" }, … ] }`
- **Errors:** `400 VALIDATION_ERROR` (date in the past or more than 30 days ahead), `404 NOT_FOUND` (doctor), `403 FORBIDDEN`

**2. Book an appointment**
- **Endpoint:** `/appointments`
- **Method:** POST
- **Roles:** Patient (books for self), Receptionist (must send `patientId`)
- **Request:** `{ "slotId": "s-901", "reason": "Fever for 3 days", "patientId": "p-77" }`
- **Response:** `201` `{ "appointmentId": "a-5001", "status": "BOOKED", "slot": { "slotId": "s-901", "doctorId": "d-12", "start": "2026-10-20T09:00:00+05:30" } }`
- **Errors:** `409 SLOT_TAKEN`, `409 PATIENT_OVERLAP`, `422 VALIDATION_ERROR` (reason shorter than 5 or longer than 300 characters), `404 NOT_FOUND` (slot or patient), `403 FORBIDDEN` (Patient sending another `patientId`)

**3. List appointments**
- **Endpoint:** `/appointments?date=&doctorId=&patientId=&status=&page=`
- **Method:** GET
- **Roles:** Patient (own only), Doctor (own only), Receptionist, Admin
- **Request:** optional query filters; 50 results per page
- **Response:** `200` `{ "items": [ { "appointmentId": "a-5001", "patientMrn": "HAP-P-000077", "doctorId": "d-12", "start": "…", "status": "BOOKED" } ], "page": 1, "total": 1 }`
- **Errors:** `403 FORBIDDEN` (filtering on another patient or doctor), `422 VALIDATION_ERROR`

**4. Get one appointment**
- **Endpoint:** `/appointments/{id}`
- **Method:** GET
- **Roles:** the appointment's patient or doctor, Receptionist, Admin
- **Response:** `200` full appointment object including `reason`, `status`, `createdBy`, `history` (status changes with time)
- **Errors:** `404 NOT_FOUND`, `403 FORBIDDEN`

**5. Reschedule**
- **Endpoint:** `/appointments/{id}/reschedule`
- **Method:** PATCH
- **Roles:** the appointment's patient, Receptionist
- **Request:** `{ "newSlotId": "s-950" }`
- **Response:** `200` `{ "appointmentId": "a-5001", "status": "BOOKED", "slot": { "slotId": "s-950", … } }` — the old slot is FREE again
- **Errors:** `409 CHANGE_WINDOW_CLOSED` (patient, less than 2 h before start), `409 SLOT_TAKEN`, `409 PATIENT_OVERLAP`, `409 INVALID_STATUS_TRANSITION` (not BOOKED), `404 NOT_FOUND`, `403 FORBIDDEN`

**6. Change status**
- **Endpoint:** `/appointments/{id}/status`
- **Method:** PATCH
- **Roles:** Receptionist (CHECKED_IN), Doctor (COMPLETED — normally set automatically by the Medical Record Service), system job (NO_SHOW)
- **Request:** `{ "status": "CHECKED_IN" }` — one of `CHECKED_IN`, `COMPLETED`, `NO_SHOW`
- **Response:** `200` `{ "appointmentId": "a-5001", "status": "CHECKED_IN" }`
- **Errors:** `409 INVALID_STATUS_TRANSITION`, `422 VALIDATION_ERROR` (unknown status), `403 FORBIDDEN`, `404 NOT_FOUND`

**7. Cancel**
- **Endpoint:** `/appointments/{id}`
- **Method:** DELETE
- **Roles:** the appointment's patient, Receptionist
- **Request:** optional `{ "reason": "Travelling" }`
- **Response:** `200` `{ "appointmentId": "a-5001", "status": "CANCELLED" }` — the record is kept with status CANCELLED and the slot becomes FREE
- **Errors:** `409 CHANGE_WINDOW_CLOSED`, `409 INVALID_STATUS_TRANSITION` (already COMPLETED / CANCELLED / NO_SHOW), `404 NOT_FOUND`, `403 FORBIDDEN`
