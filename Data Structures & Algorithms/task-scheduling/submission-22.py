class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # char : count of instances
        maxHeap = [cnt for cnt in count.values()]
        heapq.heapify_max(maxHeap)

        time = 0
        q = deque() # use a queue to keep track of [count, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                currentCount = heapq.heappop_max(maxHeap) - 1
                if currentCount > 0:
                    q.append((currentCount, time + n))

            if q and q[0][1] == time:
                # currentCount, currentTime = q.popleft()
                # heapq.heappush_max(maxHeap, currentCount)
                heapq.heappush_max(maxHeap, q.popleft()[0])

        return time