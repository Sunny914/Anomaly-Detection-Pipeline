# ingestion/metric_registry.py

METRIC_REGISTRY = {
    "cpu_usage": {
        "promql": "rate(node_cpu_seconds_total[1m])",
        "type": "counter",
        "unit": "seconds_per_second",
        "labels": ["instance", "cpu", "mode"]
    },
    "memory_available": {
        "promql": "node_memory_MemAvailable_bytes",
        "type": "gauge",
        "unit": "bytes",
        "labels": ["instance"]
    }
}

