class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid and not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row: int, col: int) -> None:
            if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                grid[row][col] == 0 or 
                (row, col) in visited
            ):
                return 0

            # If valid "1" then add to visited
            visited.add((row, col))

            return (
                1 + dfs(row + 1, col) + dfs(row - 1, col) + 
                dfs(row, col + 1) + dfs(row, col - 1)
                )


        maxArea = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(maxArea, dfs(row, col))

        return maxArea