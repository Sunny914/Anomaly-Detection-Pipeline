# baselines/baseline_store.py

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
