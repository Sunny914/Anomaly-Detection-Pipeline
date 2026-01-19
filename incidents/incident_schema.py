# incidents/incident_schema.py

from typing import Dict, List, Any


def create_incident_schema() -> Dict[str, Any]:
    """
    Defines the canonical structure of an Incident.

    This is a SCHEMA definition, not an incident instance.
    """

    return {
        # Unique identifier for the incident
        "incident_id": str,

        # Series identifier (metric + labels)
        "series": str,

        # Time boundaries (epoch seconds)
        "start_time": float,
        "end_time": float,
        "duration_sec": float,

        # Windows involved (short / medium / long)
        "window_types": List[str],

        # Overall severity and confidence
        "severity": str,        # low | medium | high | critical
        "confidence": float,    # 0.0 – 1.0

        # How many anomalies were grouped
        "anomaly_count": int,

        # Dominant detector signal
        "dominant_detector": str,

        # Overall trend direction
        "trend_direction": str,  # increasing | decreasing | mixed | unknown

        # Representative anomaly signals
        "signals": List[Dict[str, Any]],
    }
