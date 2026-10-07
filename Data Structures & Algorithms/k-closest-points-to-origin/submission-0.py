class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # im thinking do a hashmap where we store tuple(point1, point2) : distance
        # i want to calculate the distance at each point and add the distances -
        # to a minHeap, then we can just pop k amounts 
        minHeap = []

        for x, y in points:
            distance = x * x + y * y
            minHeap.append((distance, x, y))
        
        heapq.heapify(minHeap)

        result = []

        for _ in range(k):
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])

        return result