class TimeMap:

    def __init__(self):
        self.timestampDict = {} # key : timestamp, value

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestampDict:
            self.timestampDict[key] = []
        
        self.timestampDict[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestampDict:
            return ""

        result = ""
        values = self.timestampDict[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            mTimestamp, mValue = values[m]
            #if timestamp is greater than or equal to mTimestamp
            if mTimestamp <= timestamp:
                result = mValue
                l = m + 1
            else:
                #mTimestamp is too large
                r = m - 1
        
        return result