class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        combinations = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res = []

        def dfs(index: int, subString: list) -> None:
            if index == len(digits):
                res.append("".join(subString.copy()))
                return None

            for char in combinations[digits[index]]:
                subString.append(char)
                dfs(index + 1, subString)
                # undo that choice if index full
                subString.pop()

        dfs(0, [])

        return res




