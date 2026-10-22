class Solution:
    def climbStairs(self, n: int) -> int:
        oneStepBefore = 1
        twoStepsBefore = 1

        for _ in range(n - 1):
            current = oneStepBefore + twoStepsBefore
            twoStepsBefore = oneStepBefore
            oneStepBefore = current

        return oneStepBefore