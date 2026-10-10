### 4.5 UX Design

**Principles:** few steps, plain language, safe defaults, and the same layout on desktop and phone (screens ≥ 360 px, HAP-NF-004).

**Patient booking flow (≤ 4 screens, target ≤ 3 minutes):**

1. **Find a doctor** – search box plus specialization chips (General Medicine, Cardiology, Paediatrics …).
2. **Choose a date and slot** – a 7-day strip and a grid of time buttons. Free slots are solid teal buttons; unavailable times are grey and not clickable; a legend explains the colours, and the state is also shown as text ("Free", "Taken") so colour is never the only cue.
3. **Confirm** – doctor, date, time and a reason box; one "Book appointment" button.
4. **Done** – confirmation with "Add to calendar" and "View my appointments".

If the slot was taken meanwhile (`409 SLOT_TAKEN`) the patient stays on screen 2 with the message "Someone just booked this time. Please pick another slot." and the grid refreshes.

**Doctor screens:** today's schedule as a list (time, patient, status chip) with the next patient highlighted; the chart opens with an allergy banner at the top; consultation and prescription forms sit side by side on desktop and stack on phones; prescription rows can be added with one click.

**Receptionist screens:** a single search bar (name, MRN or phone) on the home screen; today's arrivals list with a large Check-in button per row; "Book for patient" reuses the patient booking screens.

**Admin screens:** dashboard cards (today's appointments, no-show rate, utilisation), staff account table, doctor profiles, report export with a date-range picker.

**Accessibility:** WCAG 2.1 AA contrast, visible keyboard focus, labelled form fields, error messages placed next to the field and announced to screen readers, body text ≥ 16 px, touch targets ≥ 44 × 44 px.

**Language:** English in version 1.0; all UI text is kept in one resource file so Kannada and Hindi can be added later.
