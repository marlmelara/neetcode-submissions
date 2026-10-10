class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        # Track columns and diagonals that already contain queens
        used_cols = set()
        used_pos_diagonals = set()  # row + col
        used_neg_diagonals = set()  # row - col

        board = [["."] * n for _ in range(n)]

        def backtrack(row: int) -> None:
            # Successfully placed a queen in every row
            if row == n:
                result.append(["".join(r) for r in board])
                return

            # Try placing a queen in each column of this row
            for col in range(n):
                pos_diagonal = row + col
                neg_diagonal = row - col

                # Position is attacked
                if (
                    col in used_cols
                    or pos_diagonal in used_pos_diagonals
                    or neg_diagonal in used_neg_diagonals
                ):
                    continue

                # Place the queen
                board[row][col] = "Q"
                used_cols.add(col)
                used_pos_diagonals.add(pos_diagonal)
                used_neg_diagonals.add(neg_diagonal)

                # Try to place a queen in the next row
                backtrack(row + 1)

                # Backtrack: undo the placement
                board[row][col] = "."
                used_cols.remove(col)
                used_pos_diagonals.remove(pos_diagonal)
                used_neg_diagonals.remove(neg_diagonal)

        backtrack(0)
        return result