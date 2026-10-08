class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cur: int, total: int) -> None:
            # We found a valid combination
            if total == target:
                res.append(cur.copy())
                return None

            # No candidates left, or the sum is too large
            if i >= len(nums) or total > target:
                return None

            # Choice 1: choose nums[i]
            cur.append(nums[i])

            # Stay at i because nums[i] can be reused
            dfs(i, cur, total + nums[i])

            # Undo the choice
            cur.pop()

            # Choice 2: skip nums[i]
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res