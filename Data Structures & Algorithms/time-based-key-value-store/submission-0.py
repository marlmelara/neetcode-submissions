class TimeMap:

    def __init__(self):
        self.timestampDict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestampDict:
            self.timestampDict[key] = []
        
        self.timestampDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestampDict:
            return ""

        values = self.timestampDict[key]

        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            stored_timestamp, stored_value = values[mid]

            if stored_timestamp <= timestamp:
                # This value is valid, but there may be a newer valid one.
                result = stored_value
                left = mid + 1
            else:
                # This timestamp is too large.
                right = mid - 1

        return result