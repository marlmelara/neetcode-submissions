class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set(nums)

        if len(nums) == len(unique_nums):
            return False
        else:
            return True