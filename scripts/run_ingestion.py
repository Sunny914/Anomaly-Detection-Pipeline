# scripts/run_ingestion.py


import time
from ingestion.metric_registry import METRIC_REGISTRY
from ingestion.promql_client import query_prometheus
from ingestion.ingestion_validator import validate_sample

def run_ingestion():
    """
    Runs Stage 1 ingestion:
    - Fetch metrics from Prometheus
    - Validate raw samples
    - Return raw samples
    """
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