class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        if not tokens:
            return 0

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
                stack.append(result)
            elif token == "-":
                result = left - right
                stack.append(result)
            elif token == "*":
                result = left * right
                stack.append(result)
            else:
                result = int(left / right)
                stack.append(result)

        return stack[0]