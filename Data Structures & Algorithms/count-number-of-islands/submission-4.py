class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set() # where we store (row, col) of our "1"s we find
        islandCount = 0

        def dfs(row: int, col: int) -> None:
            if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                grid[row][col] == "0" or
                (row, col) in visited
            ):
                return None

            # If it passes all the checks, then we can add to our set
            visited.add((row, col))

            # Check up, down, left, right cells
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # That dfs solution will start with a valid "1", then add its (row, col)
        # Then check surrounding cells to add rest of potential body of island

        # Iterate through grid, and dfs when we find "1" AND its a new island

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islandCount += 1
                    dfs(row, col)

        return islandCount