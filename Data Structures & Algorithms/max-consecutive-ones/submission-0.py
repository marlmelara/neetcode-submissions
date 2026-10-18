class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxOnes = 0
        curOnes = 0

        for num in nums:
            if num == 1:
                curOnes += 1
            else:
                curOnes = 0

            maxOnes = max(maxOnes, curOnes)

        return maxOnes