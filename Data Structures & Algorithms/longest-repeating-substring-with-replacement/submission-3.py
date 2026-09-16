class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        window_size = 0

        if not s:
            return 0

        for r in range(len(s)):
            count[s[r]] += 1
            window_size = r - l + 1
            minCharReplacement = window_size - max(count.values())

            if minCharReplacement > k:
                count[s[l]] -= 1
                l += 1

            else:
                res = max(res, window_size)
        
        return res