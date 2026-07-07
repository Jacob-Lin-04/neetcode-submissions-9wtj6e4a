class TimeMap:
   

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        import bisect
        timestamps = self.store[key]

        idx = bisect.bisect_right(timestamps, [timestamp, '{'])

        if idx == 0:
            return ""
        
        return timestamps[idx - 1][1]
