class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Start BFS from every treasure chest.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Skip cells outside the grid.
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Skip water and cells already assigned a distance.
                if grid[nr][nc] != 2147483647:
                    continue

                # Neighbor is one step farther from the nearest chest.
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))