class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if not s:
            return False

        for char in s:
            if char == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False