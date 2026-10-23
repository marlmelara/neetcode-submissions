class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # prefix[i] = number of valid words among words[0:i]
        prefix = [0] * (len(words) + 1)

        prev = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prev += 1

            prefix[i + 1] = prev

        result = [0] * len(queries)

        for i, query in enumerate(queries):
            l, r = query
            result[i] = prefix[r + 1] - prefix[l]

        return result