class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curSubset = []

        # im thinking we do a while loop of some kind to pass over
        # any duplicate values. 
        def dfs(index:int) -> None:
            if index >= len(nums):
                res.append(curSubset.copy())
                return None

            # make a choice with nums[index]
            curSubset.append(nums[index])
            dfs(index + 1)

            curSubset.pop()

            # iterate over any potential duplicate values
            while (
                index + 1 < len(nums) and nums[index] == nums[index + 1]
            ):
                index += 1
            
            dfs(index + 1)

        dfs(0)

        return res