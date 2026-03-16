"""Tests for transformation module."""
from src.transform import clean_records, aggregate_by_key


def test_clean_records_removes_none():
    records = [{"Name": "test", "Value": None}]
    result = clean_records(records)
    assert result == [{"name": "test"}]


def test_aggregate_by_key():
    records = [{"type": "a", "val": 1}, {"type": "b", "val": 2}, {"type": "a", "val": 3}]
    result = aggregate_by_key(records, "type")
    assert len(result["a"]) == 2
    assert len(result["b"]) == 1
