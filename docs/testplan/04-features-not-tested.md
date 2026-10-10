## 4. Features Not to be Tested

| Item | Reason |
|---|---|
| Internals of the SMTP email provider (delivery to inboxes, spam filtering) | Third-party service; we test only that our system hands the message to SMTP (captured by MailHog) |
| ReportLab PDF library internals | Third-party library; we test only the content of the generated PDF |
| PostgreSQL engine internals (locking implementation, replication) | Vendor-tested; we test our transactions, constraints and indexes |
| Browser rendering engines | Vendor responsibility; we test our UI on the supported browsers listed in SRS §2.4 |
| Nginx / TLS library implementation | Vendor-tested; we verify configuration (TLS versions, redirects) only |
| Billing, payments, insurance, lab, radiology and pharmacy features | Out of scope for v1.0 (SRS §1.2) |
| HL7 / FHIR integration, telemedicine, native mobile apps | Out of scope for v1.0 |
| Hardware (printers, scanners) | No special hardware interface; printing uses the operating system |
