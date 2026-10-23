class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0 # one house before
        rob2 = 0 # two houses before

        for money in nums:
            current = max(rob1, rob2 + money)
            rob2 = rob1
            rob1 = current

        return rob1