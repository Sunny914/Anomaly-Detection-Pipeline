# incidents/incident_builder.py

import uuid
from typing import List, Dict
from collections import Counter


SEVERITY_ORDER = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4,
}


def _severity_value(sev: str) -> int:
    return SEVERITY_ORDER.get(sev, 0)


def _get_anomaly_time(anomaly: Dict) -> float:
    return (
        anomaly.get("start_time")
        or anomaly.get("timestamp")
        or anomaly.get("time")
    )


def build_incident(anomaly_group: List[Dict]) -> Dict:
    """
    Builds a single incident from a group of related anomalies.
    """

    if not anomaly_group:
        return None

    # --- Identity ---
    series = anomaly_group[0]["series"]

    # --- Time bounds ---
    times = [_get_anomaly_time(a) for a in anomaly_group]
    start_time = min(times)
    end_time = max(times)

    duration_sec = end_time - start_time

    # --- Window types ---
    window_types = sorted(
        {a["window_type"] for a in anomaly_group}
    )

    # --- Severity (worst wins) ---
    severity = max(
        anomaly_group,
        key=lambda a: _severity_value(a["severity"])
    )["severity"]

    # --- Confidence (average) ---
    confidence = sum(
        a["confidence"] for a in anomaly_group
    ) / len(anomaly_group)

    # --- Dominant detector ---
    detectors = []
    for a in anomaly_group:
        detectors.extend(a.get("detectors_triggered", []))

    dominant_detector = (
        Counter(detectors).most_common(1)[0][0]
        if detectors else "unknown"
    )

    # --- Trend direction ---
    directions = []
    for a in anomaly_group:
        for s in a.get("signals", []):
            if s.get("detector") == "slope_deviation":
                directions.append(s.get("direction"))

    trend_direction = (
        Counter(directions).most_common(1)[0][0]
        if directions else "unknown"
    )

    # --- Representative signals ---
    strongest = max(
        anomaly_group,
        key=lambda a: (
            _severity_value(a["severity"]),
            a["confidence"]
        )
    )

    signals = [
        anomaly_group[0],      # first
        strongest,             # strongest
        anomaly_group[-1],     # last
    ]

    # --- Incident ID ---
    incident_id = (
        f"{series}_{int(start_time)}_"
        f"{uuid.uuid4().hex[:8]}"
    )

    return {
        "incident_id": incident_id,

        "series": series,

        "start_time": start_time,
        "end_time": end_time,
        "duration_sec": duration_sec,

        "window_types": window_types,

        "severity": severity,
        "confidence": round(confidence, 2),

        "anomaly_count": len(anomaly_group),

        "dominant_detector": dominant_detector,
        "trend_direction": trend_direction,

        "signals": signals,
    }
