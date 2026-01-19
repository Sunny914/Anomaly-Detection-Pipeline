# incidents/anomaly_grouper.py

from typing import List, Dict

# Max time gap (seconds) allowed between anomalies in the same incident
GROUPING_GAP_SEC = 120  # 2 minutes


def _get_anomaly_time(anomaly: Dict) -> float:
    """
    Extract a comparable timestamp from an anomaly.
    Every anomaly MUST have a canonical timestamp.
    """
    ts = anomaly.get("timestamp")

    if ts is None:
        raise ValueError(
            f"Anomaly missing timestamp. Keys={list(anomaly.keys())}"
        )

    return ts


def group_anomalies(anomalies: List[Dict]) -> List[List[Dict]]:
    """
    Groups anomalies into clusters representing the same incident.

    Rules:
    - Same series
    - Time gap <= GROUPING_GAP_SEC
    """

    if not anomalies:
        return []

    # Sort anomalies by time (safe: timestamp is guaranteed)
    anomalies = sorted(anomalies, key=_get_anomaly_time)

    groups: List[List[Dict]] = []
    current_group: List[Dict] = [anomalies[0]]

    for anomaly in anomalies[1:]:
        last = current_group[-1]

        same_series = anomaly["series"] == last["series"]

        time_gap = (
            _get_anomaly_time(anomaly)
            - _get_anomaly_time(last)
        )

        close_in_time = time_gap <= GROUPING_GAP_SEC

        if same_series and close_in_time:
            current_group.append(anomaly)
        else:
            groups.append(current_group)
            current_group = [anomaly]

    # Append final group
    groups.append(current_group)

    return groups
























"""
# incidents/anomaly_grouper.py

from typing import List, Dict

# Max allowed gap (seconds) between anomalies in same group
GROUPING_GAP_SEC = 120  # 2 minutes


def group_anomalies(anomalies: List[Dict]) -> List[List[Dict]]:
    
    # Groups anomalies into clusters representing the same incident.

    # Rules:
    # - Same series
    # - Time gap between anomalies <= GROUPING_GAP_SEC
    

    if not anomalies:
        return []

    # Sort anomalies by time (start_time preferred, fallback to timestamp)
    anomalies = sorted(
        anomalies,
        key=lambda a: a.get("start_time") or a.get("timestamp")
    )

    groups = []
    current_group = [anomalies[0]]

    for anomaly in anomalies[1:]:
        last = current_group[-1]

        # Extract timestamps safely
        last_time = last.get("start_time") or last.get("timestamp")
        current_time = anomaly.get("start_time") or anomaly.get("timestamp")

        same_series = anomaly["series"] == last["series"]
        close_in_time = (current_time - last_time) <= GROUPING_GAP_SEC

        if same_series and close_in_time:
            current_group.append(anomaly)
        else:
            groups.append(current_group)
            current_group = [anomaly]

    # Append final group
    groups.append(current_group)

    return groups
"""
