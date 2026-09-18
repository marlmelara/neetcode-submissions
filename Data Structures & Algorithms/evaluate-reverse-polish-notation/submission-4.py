class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                # Truncate toward zero without using //
                result = abs(left) // abs(right)

                if (left < 0) != (right < 0):
                    result = -result

            stack.append(result)

        return stack[0]