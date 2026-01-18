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
