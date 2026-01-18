# ingestion/promql_client.py

import requests
import time

PROMETHEUS_URL = "http://localhost:9090"

def query_prometheus_range(
    promql: str,
    lookback_seconds: int = 300,
    step_seconds: int = 15
):
    """
    Executes a PromQL RANGE query and returns time-series samples.
    """

    end = int(time.time())
    start = end - lookback_seconds

    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query_range",
        params={
            "query": promql,
            "start": start,
            "end": end,
            "step": step_seconds,
        },
        timeout=5,
    )

    response.raise_for_status()
    return response.json()["data"]["result"]








"""
import requests

PROMETHEUS_URL = "http://localhost:9090"

def query_prometheus(promql: str):
    
    # Executes a PromQL query against Prometheus
    # and returns raw time-series results.
    
    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query",
        params={"query": promql}
    )

    # Fail fast if Prometheus is unreachable or query is bad
    response.raise_for_status()

    return response.json()["data"]["result"]

"""