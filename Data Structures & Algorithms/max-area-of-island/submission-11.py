class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row: int, col: int) -> int:
            if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                grid[row][col] == 0 or
                (row, col) in visited
            ):
                return 0

            # if int is 1 and valid cell, then add
            visited.add((row, col))

            # then return 1 + dfs of all the cells around it (up, down, left, right)
            return (
                1 + dfs(row + 1, col) + dfs(row - 1, col) + 
                dfs(row, col + 1) + dfs(row, col - 1)
            )

        # We can run this dfs for all cells and have a running maxArea
        maxArea = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(maxArea, dfs(row, col))

        return maxArea