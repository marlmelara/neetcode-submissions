class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []

        res = []

        def dfs(index: int, current: list[str]) -> None:
            # We have chosen one character for every digit
            if index == len(digits):
                res.append("".join(current))
                return

            # Try every character mapped to the current digit
            for char in combinations[digits[index]]:
                current.append(char)
                dfs(index + 1, current)
                current.pop()  # undo the choice

        dfs(0, [])
        return res