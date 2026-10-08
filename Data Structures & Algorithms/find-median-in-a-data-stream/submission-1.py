class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # first half of nums
        self.minHeap = [] # second half of nums
        heapq.heapify_max(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        # Put num in the correct half of heap
        if not self.minHeap or num <= self.minHeap[0]:
            heapq.heappush_max(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, num)

        # Rebalance if needed
        if len(self.maxHeap) > len(self.minHeap) + 1:
            value = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, value)
        
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            value = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, value)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return float(self.maxHeap[0])
        
        elif len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])

        else:
            return float((self.maxHeap[0] + self.minHeap[0]) / 2 )