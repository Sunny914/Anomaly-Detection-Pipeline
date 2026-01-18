# baselines/baseline_store.py

# baselines/baseline_store.py

import json
import os
import time
import hashlib

BASELINE_PATH = "data/baselines"
os.makedirs(BASELINE_PATH, exist_ok=True)


def _stable_series_id(series_key):
    """
    Generates a stable, reproducible ID for a series.
    """
    raw = json.dumps(series_key, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def store_baseline(series_key, window_type, stats, slope):
    """
    Stores a baseline snapshot in an append-only manner.
    """

    series_id = _stable_series_id(series_key)

    baseline = {
        "series_id": series_id,
        "series_key": series_key,
        "window_type": window_type,
        "stats": stats,
        "slope": slope,
        "timestamp": time.time()
    }

    filename = f"{BASELINE_PATH}/{series_id}_{window_type}.jsonl"

    with open(filename, "a") as f:
        f.write(json.dumps(baseline) + "\n")






"""
import json
import os

BASELINE_PATH = "data/baselines"

os.makedirs(BASELINE_PATH, exist_ok=True)

def store_baseline(key, window_type, stats, slope):
    baseline = {
        "series": str(key),
        "window": window_type,
        "stats": stats,
        "slope": slope
    }

    filename = f"{BASELINE_PATH}/{hash(str(key))}_{window_type}.json"

    with open(filename, "w") as f:
        json.dump(baseline, f, indent=2)


"""