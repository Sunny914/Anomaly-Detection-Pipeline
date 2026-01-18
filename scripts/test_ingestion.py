# scripts/test_ingestion.py

from ingestion.promql_client import query_prometheus

if __name__ == "__main__":
    result = query_prometheus("rate(node_cpu_seconds_total[1m])")
    print(result[:2])
