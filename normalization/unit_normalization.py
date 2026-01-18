# normalization/unit_normalization.py

# normalization/unit_normalization.py

def normalize_units(sample: dict, metric_def: dict):
    """
    Converts metric values into canonical, comparable units.
    This is CRITICAL for baseline + detector correctness.
    """

    unit = metric_def.get("unit")
    value = sample["value"]

    # Preserve raw value for debugging / audits
    sample["raw_value"] = value
    sample["raw_unit"] = unit

    # --- MEMORY ---
    if unit == "bytes":
        # bytes → MB
        sample["value"] = value / (1024 * 1024)
        sample["unit"] = "MB"

    # --- CPU ---
    elif unit == "seconds_per_second":
        # Prometheus CPU is seconds/sec per core
        # Normalize to percentage [0–100]
        sample["value"] = value * 100.0
        sample["unit"] = "percent"

    # --- DEFAULT / PASS-THROUGH ---
    else:
        sample["value"] = value
        sample["unit"] = unit

    return sample







"""
def normalize_units(sample: dict, metric_def: dict):
    
    # Converts metric values into canonical units.
    
    unit = metric_def["unit"]

    if unit == "bytes":
        # Convert bytes → megabytes
        sample["value"] = sample["value"] / (1024 * 1024)
        sample["unit"] = "MB"
    else:
        sample["unit"] = unit

    return sample
"""