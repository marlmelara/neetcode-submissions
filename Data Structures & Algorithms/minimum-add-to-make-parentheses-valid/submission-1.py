class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openParentheses = 0
        additions = 0
        

        for c in s:
            if c == "(":
                openParentheses += 1
            elif openParentheses:
                openParentheses -= 1
            else:
                additions += 1

        return additions + openParentheses