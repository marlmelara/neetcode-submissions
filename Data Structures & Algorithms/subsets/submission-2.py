class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(index: int) -> None:
            if index >= len(nums):
                res.append(subset.copy())
                return None

            # first we want to explore choice nums[index]
            subset.append(nums[index])
            dfs(index + 1)

            # then we undo that choice, and explore without choosing it
            subset.pop()
            dfs(index + 1)

        dfs(0)
        
        return res