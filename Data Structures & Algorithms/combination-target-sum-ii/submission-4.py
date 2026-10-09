class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(index: int, currSubset: list, total: int) -> None:
            if total == target:
                res.append(currSubset.copy())
                return None
            
            # make sure index is in bounds and total isn't greater than target
            if index >= len(candidates) or total > target:
                return None

            # explore choice with candidates[index], then go to next index
            currSubset.append(candidates[index])
            dfs(index + 1, currSubset, total + candidates[index])

            # explore choice without candidates[index], then go to next index
            currSubset.pop()

            # Skip duplicate values for the "not choose" branch
            while (
                index + 1 < len(candidates)
                and candidates[index] == candidates[index + 1]
            ):
                index += 1
                
            dfs(index + 1, currSubset, total)

        dfs(0, [], 0)

        return res