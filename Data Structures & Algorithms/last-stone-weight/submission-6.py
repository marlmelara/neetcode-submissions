class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we are smashing the two heaviest stones 
        # if they are equal, remove both, else add new stone with their diff
        if not stones:
            return 0

        maxHeap = stones
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            # we know that our heap will always have at least 2 elements
            # knowing this, we can do maxHeap[0] - minHeap[1] to get new stone
            firstStone = heapq.heappop_max(maxHeap)
            secondStone = heapq.heappop_max(maxHeap)
            newStone = firstStone - secondStone

            if newStone != 0:
                heapq.heappush_max(maxHeap, newStone)

        if len(maxHeap) == 1:
            return maxHeap[0]
        else:
            return 0