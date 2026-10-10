import sys
from datetime import datetime
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.scheduling import generate_slots, has_patient_conflict, overlaps  # noqa: E402


def t(hour, minute=0):
    return datetime(2026, 10, 19, hour, minute)


def test_monday_morning_gives_twelve_15_minute_slots():
    slots = generate_slots(t(9), t(12), 15)
    assert len(slots) == 12
    assert slots[0] == (t(9), t(9, 15))
    assert slots[-1] == (t(11, 45), t(12))


def test_trailing_partial_slot_is_dropped():
    assert len(generate_slots(t(9), t(9, 50), 20)) == 2


def test_invalid_slot_duration_is_rejected():
    with pytest.raises(ValueError):
        generate_slots(t(9), t(12), 25)


def test_end_before_start_is_rejected():
    with pytest.raises(ValueError):
        generate_slots(t(12), t(9), 15)


def test_touching_intervals_do_not_overlap():
    assert not overlaps(t(9), t(9, 15), t(9, 15), t(9, 30))


def test_patient_with_overlapping_appointment_is_detected():
    existing = [(t(10), t(10, 15))]
    assert has_patient_conflict((t(10, 5), t(10, 20)), existing)
    assert not has_patient_conflict((t(10, 15), t(10, 30)), existing)
