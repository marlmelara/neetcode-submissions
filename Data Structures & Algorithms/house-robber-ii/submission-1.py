class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # case 1: keep index 0, skip last index
        case1 = self.helper(nums[:-1])

        # case 2: skip index 0, keep last index
        case2 = self.helper(nums[1:])

        return max(case1, case2)


    def helper(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for money in nums:
            current = max(rob1, rob2 + money)
            rob2 = rob1
            rob1 = current

        return rob1