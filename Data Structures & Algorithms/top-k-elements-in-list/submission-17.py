class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        keys = []
        result = []
        nums_count_sorted = dict(sorted(nums_count.items(), key = lambda item: item[1], reverse = True))

        for key in nums_count_sorted.keys():
            keys.append(key)

        for i in range(k):
            result.append(keys[i])

        return result