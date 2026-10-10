### 3.5 Chosen Architecture Pattern and Rationale

**Chosen pattern: Layered (3-tier) architecture** — Presentation (React Web Frontend) → Application / Service layer (FastAPI services) → Data layer (PostgreSQL).

Each layer talks only to the layer directly below it. Inside the application layer, each component is a separate Python package with its own router, service logic and repository code, so it can be unit-tested on its own.

**Rationale**

- **Separation of concerns:** UI code, business rules and storage are cleanly separated, so a change to a screen never touches booking logic.
- **One place for access control:** every request passes through the service layer, which is where role checks and record-level checks (HAP-SR-004) are enforced, instead of trusting the browser.
- **Safe conflict prevention:** booking needs one database transaction that locks the slot and checks the patient's other appointments. With all services sharing one database, this is a single ACID transaction.
- **Testability:** each layer and each service package can be tested separately, which supports the ≥ 70% coverage target (HAP-NF-005).
- **Fits the team:** four developers can each own a service package without stepping on each other's code.

**Rejected alternative: Microservices.** Separate deployable services with their own databases were considered and rejected. They would add service discovery, network calls between services, distributed transactions (booking would span the slot and appointment services) and much more deployment work, all of which is out of proportion for a single clinic and a four-person team. Because the service packages already have clear boundaries, the system can be split into microservices later if load ever requires it.
