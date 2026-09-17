class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_count = Counter(s1) # char : count
        s2_count = defaultdict(int)

        if len(s2) < len(s1):
            return False
        
        for i in range(len(s1)):
            s2_count[s2[i]] += 1

        if s1_count == s2_count:
            return True

        for r in range(len(s1), len(s2)):
            s2_count[s2[l]] -= 1
            s2_count[s2[r]] += 1
            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]
            l += 1

            if s1_count == s2_count:
                return True

        return False