"""Slot generation and appointment-conflict helpers (HAP-F-021, HAP-F-032)."""
from datetime import datetime, timedelta

ALLOWED_SLOT_MINUTES = (10, 15, 20, 30)


def generate_slots(day_start: datetime, day_end: datetime, slot_minutes: int = 15):
    """Split one availability range into (start, end) slots of slot_minutes.

    A trailing piece shorter than one slot is dropped.
    """
    if slot_minutes not in ALLOWED_SLOT_MINUTES:
        raise ValueError(f"slot duration must be one of {ALLOWED_SLOT_MINUTES}")
    if day_end <= day_start:
        raise ValueError("end time must be after start time")
    step = timedelta(minutes=slot_minutes)
    slots = []
    start = day_start
    while start + step <= day_end:
        slots.append((start, start + step))
        start += step
    return slots


def overlaps(a_start: datetime, a_end: datetime, b_start: datetime, b_end: datetime) -> bool:
    """True when two time intervals overlap (touching end-to-start is not an overlap)."""
    return a_start < b_end and b_start < a_end


def has_patient_conflict(new_slot, active_appointments) -> bool:
    """True if new_slot (start, end) overlaps any of the patient's active (start, end) appointments."""
    new_start, new_end = new_slot
    return any(overlaps(new_start, new_end, s, e) for s, e in active_appointments)
