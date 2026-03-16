"""ETL transformation logic."""
import logging
from typing import Any

logger = logging.getLogger(__name__)


def clean_records(records: list[dict]) -> list[dict]:
    """Remove null values and normalize keys."""
    cleaned = []
    for record in records:
        cleaned.append({k.lower(): v for k, v in record.items() if v is not None})
    return cleaned


def aggregate_by_key(records: list[dict], key: str) -> dict[str, list[Any]]:
    """Group records by a given key."""
    result: dict[str, list] = {}
    for record in records:
        k = record.get(key, "unknown")
        result.setdefault(k, []).append(record)
    return result
