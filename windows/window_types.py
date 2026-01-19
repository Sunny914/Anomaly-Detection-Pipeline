# windows/window_types.py

class TimeWindow:
    def __init__(self, start_ts, end_ts, samples):
        self.start_ts = start_ts
        self.end_ts = end_ts
        self.samples = samples

        # canonical timestamp for detection & incidents
        self.center_ts = (start_ts + end_ts) / 2

    def get_values(self):
        return [s["value"] for s in self.samples]

    def __len__(self):
        return len(self.samples)
















"""
# windows/window_types.py

class TimeWindow:

    # Represents a time-bounded window of samples.
    
    def __init__(self, start_ts, end_ts, samples):
        if not samples:
            raise ValueError("TimeWindow cannot be created with empty samples")

        self.start_ts = start_ts
        self.end_ts = end_ts
        self.center_ts = (start_ts + end_ts) / 2

        # Samples must already be time-sorted
        self.samples = samples

        # Convenience mapping: timestamp -> value
        self.values = {
            s["timestamp"]: s["value"] for s in samples
        }

    def __len__(self):
        return len(self.samples)


"""









"""
# windows/window_types.py

class TimeWindow:
    def __init__(self, start_ts, end_ts, samples):
        self.start_ts = start_ts
        self.end_ts = end_ts
        self.samples = samples

    def values(self):
        return [s["value"] for s in self.samples]

    def __len__(self):
        return len(self.samples)
"""