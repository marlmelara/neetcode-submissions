class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        keys = []
        nums_count_sorted = dict(sorted(nums_count.items(), key = lambda item: item[1], reverse = True))

        for key in nums_count_sorted.keys():
            keys.append(key)

        while len(keys) > k:
            keys.pop() # pop smallest elements until we reach our desired k

        return keys