# scripts/test_ingestion.py

import time
from ingestion.promql_client import query_prometheus_range

if __name__ == "__main__":
    end = time.time()
    start = end - 300  # last 5 minutes

    result = query_prometheus_range(
        promql="rate(node_cpu_seconds_total[1m])",
        start=start,
        end=end,
        step="5s"
    )

    print(f"Returned {len(result)} series")

    # Print first series + first 3 points for sanity
    if result:
        series = result[0]
        print("Labels:", series["metric"])
        print("First points:", series["values"][:3])







"""
from ingestion.promql_client import query_prometheus

if __name__ == "__main__":
    result = query_prometheus("rate(node_cpu_seconds_total[1m])")
    print(result[:2])
"""