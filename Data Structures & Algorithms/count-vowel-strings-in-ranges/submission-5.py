class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # prefix[i] = number of valid words among words[0:i]
        prefix = [0]

        for word in words:
            is_vowel_string = (
                word[0] in vowels and word[-1] in vowels
            )
            prefix.append(prefix[-1] + is_vowel_string)

        result = []

        for left, right in queries:
            # prefix[right + 1] includes words[right]
            count = prefix[right + 1] - prefix[left]
            result.append(count)

        return result