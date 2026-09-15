class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_count = defaultdict(int)

        if len(nums) == 0:
            return 0

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num
                nums_count[num] += 1
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    nums_count[num] += 1
            else:
                continue
        
        return max(nums_count.values())