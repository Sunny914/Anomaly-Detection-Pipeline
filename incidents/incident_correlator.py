# incidents/incident_correlator.py

from typing import List, Dict
import ast


def _parse_series(series):
    """
    Ensure series is a tuple, not a string.
    """
    if isinstance(series, str):
        try:
            return ast.literal_eval(series)
        except Exception:
            return None
    return series


def _strip_cpu_label(series_key):
    """
    Remove per-CPU label to correlate CPU-wide incidents.
    """
    parsed = _parse_series(series_key)
    if not parsed:
        return series_key

    metric, labels = parsed

    filtered_labels = tuple(
        (k, v) for k, v in labels
        if k != "cpu"
    )

    return (metric, filtered_labels)


def correlate_incidents(incidents: List[Dict]) -> List[Dict]:
    """
    Correlates incidents across CPU cores and windows.
    """

    buckets = {}

    for inc in incidents:
        agg_key = _strip_cpu_label(inc["series"])

        if agg_key not in buckets:
            buckets[agg_key] = []

        buckets[agg_key].append(inc)

    correlated = []

    for agg_key, incs in buckets.items():
        if len(incs) == 1:
            correlated.append(incs[0])
            continue

        severity_order = {"low": 0, "medium": 1, "high": 2}

        final = {
            "series": agg_key,
            "incident_type": "cpu_saturation",
            "severity": max(incs, key=lambda i: severity_order[i["severity"]])["severity"],
            "confidence": round(
                sum(i["confidence"] for i in incs) / len(incs), 2
            ),
            "duration_sec": max(i["duration_sec"] for i in incs),
            "anomaly_count": sum(i["anomaly_count"] for i in incs),
            "window_types": sorted(
                set(w for i in incs for w in i["window_types"])
            ),
            "dominant_detector": incs[0]["dominant_detector"],
            "trend_direction": incs[0]["trend_direction"],
        }

        correlated.append(final)

    return correlated













"""
# incidents/incident_correlator.py

from collections import defaultdict
from incidents.correlation_rules import (
    passes_persistence_rule,
    infer_incident_type
)


def _strip_cpu_label(series_key):
    
    # Removes cpu label to aggregate per-host.
    
    metric, labels = series_key
    labels = tuple(
        (k, v) for k, v in labels if k != "cpu"
    )
    return (metric, labels)


def correlate_incidents(incidents):
    
    # Applies correlation rules to raw incidents.
    
    grouped = defaultdict(list)

    for inc in incidents:
        agg_key = _strip_cpu_label(inc["series"])
        grouped[agg_key].append(inc)

    final_incidents = []

    for _, group in grouped.items():
        merged = group[0]

        # Merge anomalies
        merged["anomalies"] = []
        for g in group:
            merged["anomalies"].extend(g["anomalies"])

        merged["anomaly_count"] = len(merged["anomalies"])

        merged["incident_type"] = infer_incident_type(merged)

        if passes_persistence_rule(merged):
            final_incidents.append(merged)

    return final_incidents

    """