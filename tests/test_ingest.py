"""Tests for ingestion module."""
from src.ingest import ingest_from_api


def test_ingest_from_api_returns_list():
    result = ingest_from_api("https://example.com", "key")
    assert isinstance(result, list)
    assert len(result) > 0


def test_ingest_records_have_id():
    result = ingest_from_api("https://example.com", "key")
    for record in result:
        assert "id" in record
