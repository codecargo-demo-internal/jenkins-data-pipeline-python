"""Data ingestion module for pulling from external sources."""
import json
import logging

logger = logging.getLogger(__name__)


def ingest_from_api(endpoint: str, api_key: str) -> list[dict]:
    """Pull data from external API endpoint."""
    logger.info(f"Ingesting data from {endpoint}")
    return [{"id": 1, "value": "sample"}, {"id": 2, "value": "data"}]


def ingest_from_s3(bucket: str, prefix: str) -> list[dict]:
    """Pull data from S3 bucket."""
    logger.info(f"Ingesting from s3://{bucket}/{prefix}")
    return []


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = ingest_from_api("https://api.example.com/data", "fake-key")
    print(json.dumps(data, indent=2))
