class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        result = []

        for i in range(len(nums_sorted) - 2):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue
            left = i + 1
            right = len(nums_sorted) - 1
            while left < right:
                total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                    while left < right and nums_sorted[left] == nums_sorted[left + 1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result