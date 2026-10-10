class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # will have (row, col)

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or
             r >= ROWS or c >= COLS or 
             word[i] != board[r][c]
             or (r, c) in path):
                return False

            # add (r, c) as it has word[i]
            path.add((r, c))

            # check surrounding from word[i]
            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))

            # if we can't find anything then we want to remove the (r,c) from
            # set as it is not valid
            path.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                found = dfs(r, c, 0)
                if found == True:
                    return True
        
        return False