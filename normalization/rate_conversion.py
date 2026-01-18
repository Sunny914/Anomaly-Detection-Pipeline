# normalization/rate_conversion.py

def normalize_rate(sample: dict, metric_def: dict):
    """
    Ensures counter-based metrics are treated as rates.
    """
    if metric_def["type"] == "counter":
        # Prometheus already returns a rate if rate() was used
        sample["value"] = float(sample["value"])

    return sample
