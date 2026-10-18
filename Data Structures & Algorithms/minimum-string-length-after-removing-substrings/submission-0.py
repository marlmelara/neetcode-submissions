class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        subStrings = [("A", "B"), ("C", "D")]

        for c in s:
            if stack and (stack[-1], c) in subStrings:
                stack.pop()
            else:
                stack.append(c)

        return len(stack)