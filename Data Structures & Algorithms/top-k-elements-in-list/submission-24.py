class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # Index represents frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            buckets[frequency].append(num)

        result = []

        # Start with the highest possible frequency
        for frequency in range(len(nums), 0, -1):
            for num in buckets[frequency]:
                result.append(num)

                if len(result) == k:
                    return result