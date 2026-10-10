### 4.6 Open Issues & Next Steps

**Open issues**

| # | Issue | Proposed handling |
|---|---|---|
| 1 | Key management for AES-256 encryption (rotation, backup of the key) | Store the key in a secrets file outside the repo for v1.0; evaluate a key vault before production |
| 2 | Email deliverability (spam filters, provider limits) | Use a transactional email provider with SPF/DKIM; in-app notifications remain the fallback |
| 3 | Time zones if the clinic serves patients outside IST | All times stored in UTC, displayed in the clinic's time zone; confirm with stakeholders |
| 4 | Doctors on emergency duty need to override the 15-minute slot grid | Allow Receptionist "urgent" bookings outside slots in a later sprint |
| 5 | Retention period for audit logs | Keep for at least 3 years; confirm with the course/clinic policy |

**Future enhancements**

- OTP-based login and two-factor authentication for staff
- SMS / WhatsApp appointment reminders
- Video consultations (telemedicine)
- Lab results upload and viewing
- Online payments and invoices
- HL7 / FHIR interfaces to exchange records with other hospitals
- Native Android and iOS apps
