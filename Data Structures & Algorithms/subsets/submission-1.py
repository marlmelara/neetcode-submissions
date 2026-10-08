class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[index]
            subset.append(nums[index])
            dfs(index + 1)

            # decision to not include nums[index]
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return res