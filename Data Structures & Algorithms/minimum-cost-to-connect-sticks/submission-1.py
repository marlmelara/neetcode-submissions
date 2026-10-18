class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0

        heapq.heapify(sticks)
        totalCost = 0

        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            newStick = (first + second)
            totalCost += newStick

            # append the newStick to minHeap
            heapq.heappush(sticks, newStick)

        return totalCost