class Solution:
    def countSubstrings(self, s: str) -> int:
        totalPalindromes = 0

        # we want to calculate for odd and even length 

        for i in range(len(s)):
            # for odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                totalPalindromes += 1

                l -= 1
                r += 1

            # for even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                totalPalindromes += 1

                l -= 1
                r += 1

        return totalPalindromes