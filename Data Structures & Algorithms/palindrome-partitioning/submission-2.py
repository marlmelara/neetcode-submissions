class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def dfs(start: int) -> None:
            if start == len(s):
                result.append(current.copy())
                return

            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if substring == substring[::-1]:
                    current.append(substring)
                    dfs(end + 1)
                    current.pop()

        dfs(0)
        return result