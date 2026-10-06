class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # use a minHeap and only store len(k) so minHeap[0] will be our answer
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        #lets check if number we added makes our heap be bigger than k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]