class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # base case if either board or board[0] empty
        if not board or not board[0]:
            return None

        # dealing with strings
        rows, cols = len(board), len(board[0])

        # dfs approach to search border cells then mark its connecting region 
        # as safe by changing it to S
        def markSafe(row: int, col: int) -> None:
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != "O"
            ):
                return None

            board[row][col] = "S"

            # search its connecting regions and mark 'S'
            markSafe(row + 1, col)
            markSafe(row - 1, col)
            markSafe(row, col + 1)
            markSafe(row, col - 1)
            
        # run our dfs approach on border cells
        for row in range(rows):
            markSafe(row, 0)
            markSafe(row, cols - 1)

        for col in range(cols):
            markSafe(0, col)
            markSafe(rows - 1, col)

        # iterate through our board and convert all safe 'S' cells
        # to 'O' and turn everything else to 'X'
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "S":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"
