# incidents/correlation_rules.py

MIN_ANOMALIES_PER_INCIDENT = 2
MIN_DURATION_SEC = 30


def passes_persistence_rule(incident):
    """
    Filters out short-lived noise incidents.
    """
    if incident["anomaly_count"] >= MIN_ANOMALIES_PER_INCIDENT:
        return True

    if incident["duration_sec"] >= MIN_DURATION_SEC:
        return True

    return False


def infer_incident_type(incident):
    """
    Infers root cause from signals.
    """
    modes = set()

    for a in incident["anomalies"]:
        for s in a["signals"]:
            series = s["series"]
            if "mode" in series:
                modes.add(series)

    if any("iowait" in m for m in modes):
        return "disk_pressure"

    if any("softirq" in m for m in modes):
        return "network_pressure"

    if any("user" in m or "system" in m for m in modes):
        return "cpu_saturation"

    return "unknown"
