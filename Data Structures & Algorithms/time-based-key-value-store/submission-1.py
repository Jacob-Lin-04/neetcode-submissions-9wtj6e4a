class TimeMap:

    def __init__(self):
        # Hash table
        self.store = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Binary Search to find target since list is sorted
        values = self.store.get(key, [])
        low, high = 0, len(values) -1
        result = ""

        while low <= high:
            mid = (low + high) // 2

            # check timestamp of [value, time] pair
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                low = mid + 1

            else:
                high = mid -1
            

        return result

        
