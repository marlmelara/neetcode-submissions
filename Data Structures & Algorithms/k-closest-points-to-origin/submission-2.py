class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distance = math.sqrt(x * x + y * y)
            minHeap.append((distance, x, y))

        heapq.heapify(minHeap)
        
        result = []

        for _ in range(k):
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])
        
        return result