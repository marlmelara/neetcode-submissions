class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]

        if len(cost) == 2:
            return min(cost[0], cost[1])

        N = len(cost)

        for i in range(2, N):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[N - 1], cost[N - 2])