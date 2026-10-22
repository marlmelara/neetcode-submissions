class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        twoStepsBefore = 1 # ways(1)
        oneStepBefore = 2 # ways(2)

        for step in range(3, n + 1):
            current = oneStepBefore + twoStepsBefore
            twoStepsBefore = oneStepBefore
            oneStepBefore = current

        return oneStepBefore