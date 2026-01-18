# ingestion/ingestion_validator.py

def validate_sample(sample: dict):
    """
    Validates the structure of a raw metric sample.
    """
    required_fields = ["metric", "timestamp", "value", "labels"]

    for field in required_fields:
        if field not in sample:
            raise ValueError(f"Missing required field: {field}")

    if not isinstance(sample["value"], (int, float)):
        raise ValueError("Metric value must be numeric")

    if sample["timestamp"] <= 0:
        raise ValueError("Invalid timestamp")

    return True

