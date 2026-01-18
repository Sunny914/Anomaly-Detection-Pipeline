# normalization/unit_normalization.py

def normalize_units(sample: dict, metric_def: dict):
    """
    Converts metric values into canonical units.
    """
    unit = metric_def["unit"]

    if unit == "bytes":
        # Convert bytes → megabytes
        sample["value"] = sample["value"] / (1024 * 1024)
        sample["unit"] = "MB"
    else:
        sample["unit"] = unit

    return sample
