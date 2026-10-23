class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowelCount = defaultdict(int)
        res = []

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][len(words[i]) - 1] in vowels:
                vowelCount[i] += 1
            else:
                vowelCount[i] = 0

        for start, end in queries:
            vowels = 0

            for i in range(start, end + 1):
                vowels += vowelCount[i]

            res.append(vowels)

        return res