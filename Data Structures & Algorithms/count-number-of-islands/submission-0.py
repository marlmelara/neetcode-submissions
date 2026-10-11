class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        countIslands = 0

        def dfs(row: int, col: int) -> None:
            # Stop at invalid cells, water, or visited
            if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                grid[row][col] == "0" or
                (row, col) in visited
            ):
                return None

            visited.add((row, col))

            # Explore up, down, left, and right
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    countIslands += 1
                    dfs(row, col)

        return countIslands