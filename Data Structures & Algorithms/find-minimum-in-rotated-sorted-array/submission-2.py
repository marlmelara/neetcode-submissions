class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                res = min(res, nums[m])
                r = m - 1

        return res