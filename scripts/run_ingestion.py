# scripts/run_ingestion.py

import time
from ingestion.metric_registry import METRIC_REGISTRY
from ingestion.promql_client import query_prometheus_range
from ingestion.ingestion_validator import validate_sample

# Range query parameters
RANGE_SECONDS = 900     # 15 minutes (supports long windows)
STEP_SECONDS = "5s"


def run_ingestion(debug=False):
    """
    Stage 1 — Ingestion
    - Fetch range data from Prometheus
    - Preserve real timestamps
    - Return dense time-series samples
    """

    samples = []

    end = time.time()
    start = end - RANGE_SECONDS

    for metric_name, metric_def in METRIC_REGISTRY.items():
        try:
            results = query_prometheus_range(
                metric_def["promql"],
                start=start,
                end=end,
                step=STEP_SECONDS
            )
        except Exception as e:
            if debug:
                print(f"[INGESTION ERROR] {metric_name}: {e}")
            continue

        for series in results:
            labels = series.get("metric", {})

            for ts, value in series.get("values", []):
                sample = {
                    "metric": metric_name,
                    "timestamp": float(ts),
                    "value": float(value),
                    "labels": labels
                }

                validate_sample(sample)
                samples.append(sample)

    if debug:
        print(f"[INGESTION] Collected {len(samples)} samples")

    return samples


if __name__ == "__main__":
    run_ingestion(debug=True)






"""
import time
from ingestion.metric_registry import METRIC_REGISTRY
from ingestion.promql_client import query_prometheus_range
from ingestion.ingestion_validator import validate_sample

# Range query parameters
RANGE_SECONDS = 300    # last 5 minutes
STEP_SECONDS = "5s" 

def run_ingestion():
    
    # Stage 1 — Ingestion (correct for Stage 5)
    # - Fetch range data from Prometheus
    # - Preserve real timestamps
    # - Return dense time-series samples
    
    samples = []

    end = time.time()
    start = end - RANGE_SECONDS

    for metric_name, metric_def in METRIC_REGISTRY.items():
        results = query_prometheus_range(
            metric_def["promql"],
            start=start,
            end=end,
            step=STEP_SECONDS
        )

        for series in results:
            labels = series["metric"]

            # Prometheus range query returns many points
            for ts, value in series["values"]:
                sample = {
                    "metric": metric_name,
                    "timestamp": float(ts),   # ✅ REAL timestamp
                    "value": float(value),
                    "labels": labels
                }

                validate_sample(sample)
                samples.append(sample)

    return samples


if __name__ == "__main__":
    run_ingestion()

"""









"""
import time
from ingestion.metric_registry import METRIC_REGISTRY
from ingestion.promql_client import query_prometheus, query_prometheus_range
from ingestion.ingestion_validator import validate_sample

def run_ingestion():
    
    # Runs Stage 1 ingestion:
    # - Fetch metrics from Prometheus
    # - Validate raw samples
    # - Return raw samples
    
    samples = []   # ✅ NEW

    for metric_name, metric_def in METRIC_REGISTRY.items():
        results = query_prometheus(metric_def["promql"])

        for series in results:
            sample = {
                "metric": metric_name,
                "timestamp": time.time(),
                "value": float(series["value"][1]),
                "labels": series["metric"]
            }

            validate_sample(sample)
            samples.append(sample)   # ✅ NEW
            print(sample)            # keep visibility

    return samples   # ✅ CRITICAL

if __name__ == "__main__":
    run_ingestion()
"""




"""
import time
from ingestion.metric_registry import METRIC_REGISTRY
from ingestion.promql_client import query_prometheus
from ingestion.ingestion_validator import validate_sample

def run_ingestion():

    #Runs Stage 1 ingestion:
    #- Fetch metrics from Prometheus
    #- Validate raw samples
    #- Emit raw evidence

    for metric_name, metric_def in METRIC_REGISTRY.items():
        results = query_prometheus(metric_def["promql"])

        for series in results:
            sample = {
                "metric": metric_name,
                "timestamp": time.time(),
                "value": float(series["value"][1]),
                "labels": series["metric"]
            }

            validate_sample(sample)

            # Stage 1 output (stdout for now)
            print(sample)

if __name__ == "__main__":
    run_ingestion()

"""    