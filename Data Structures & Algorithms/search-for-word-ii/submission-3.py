class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build the Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] == "#"
            ):
                return

            ch = board[r][c]

            # Current board path is not a prefix of any word
            if ch not in node.children:
                return

            next_node = node.children[ch]

            # Found a complete word
            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicates

            # Mark this cell as visited
            board[r][c] = "#"

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # Restore the cell for other paths
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result