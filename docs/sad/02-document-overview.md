## 2. Document Overview

### 2.1 How to use this document

- **Section 3 – Architecture** gives the big picture: goals and constraints, stakeholders, the component and domain class diagrams, component descriptions, the chosen pattern with its rationale, the technology stack, risks, traceability to requirements and the STRIDE threat model. Read this first to understand where each requirement lives.
- **Section 4 – Design** goes one level deeper: the design overview, two UML sequence diagrams (appointment booking and consultation/prescription), the REST API of the Appointment Service and the Medical Record Service, error handling and logging, UX design and open issues.
- **Section 5 – Appendices** holds the glossary, references and tools.

Every requirement ID (HAP-F, HAP-NF, HAP-SR) refers to the SRS, and component names are used identically in all three project documents.

### 2.2 Related documents

| Document | Version | Relationship |
|---|---|---|
| Software Requirements Specification (SRS) | 1.0 | Source of every requirement this design implements |
| Software Test Plan (STP) | 1.0 | Verifies the requirements and the design decisions described here |
| Requirements Traceability Matrix (RTM) | 1.0 (SRS §8) | Links each requirement to SAD sections, components and test cases |
| Requirements Registry | 1.0 (`docs/requirements-registry.md`) | Fixed list of all requirement and test case IDs |
