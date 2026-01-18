# scripts/run_normalization.py

from ingestion.metric_registry import METRIC_REGISTRY
from normalization.rate_conversion import normalize_rate
from normalization.unit_normalization import normalize_units
from normalization.resampler import resample_timestamp
from scripts.run_ingestion import run_ingestion

def run_normalization():
    # ✅ Call Stage 1 ONCE
    raw_samples = run_ingestion()

    normalized_samples = []

    for sample in raw_samples:
        metric_def = METRIC_REGISTRY[sample["metric"]]

        sample = normalize_rate(sample, metric_def)
        sample = normalize_units(sample, metric_def)
        sample["timestamp"] = resample_timestamp(sample["timestamp"])

        normalized_samples.append(sample)

    # Optional visibility
    for s in normalized_samples:
        print(s)

    return normalized_samples   # ✅ CRITICAL

if __name__ == "__main__":
    run_normalization()








"""
from ingestion.metric_registry import METRIC_REGISTRY
from normalization.rate_conversion import normalize_rate
from normalization.unit_normalization import normalize_units
from normalization.resampler import resample_timestamp
from scripts.run_ingestion import run_ingestion

def run_normalization():
    raw_samples = []

    # Capture Stage 1 output
    for metric_name, metric_def in METRIC_REGISTRY.items():
        raw_samples.extend(run_ingestion())

    normalized_samples = []

    for sample in raw_samples:
        metric_def = METRIC_REGISTRY[sample["metric"]]

        sample = normalize_rate(sample, metric_def)
        sample = normalize_units(sample, metric_def)
        sample["timestamp"] = resample_timestamp(sample["timestamp"])

        normalized_samples.append(sample)

    for s in normalized_samples:
        print(s)

if __name__ == "__main__":
    run_normalization()
"""