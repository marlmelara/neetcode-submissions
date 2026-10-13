class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # The transformation is impossible if endWord is unavailable
        if endWord not in wordList:
            return 0

        lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
        
        wordSet = set(wordList)

        # Queue stores: (current word, number of words in the sequence)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            # Try changing each character to every lowercase letter
            for i in range(len(word)):
                for char in lowercaseAlphabet:
                    nextWord = word[:i] + char + word[i + 1:]

                    if nextWord in wordSet and nextWord not in visited:
                        visited.add(nextWord)
                        queue.append((nextWord, length + 1))

        return 0