class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        minHeap = nums
        heapq.heapify(minHeap)

        # we get a minHeap, then we pop until we have k elements left
        # we know minHeap[0] will be our answer as that is kth largest int

        while len(minHeap) > k:
            heapq.heappop(minHeap)

        return minHeap[0]