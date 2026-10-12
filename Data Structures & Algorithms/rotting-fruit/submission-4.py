class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        max_time = 0

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if grid[nr][nc] != 1:
                    continue

                grid[nr][nc] = grid[r][c] + 1
                max_time = max(max_time, grid[nr][nc] - 2)
                fresh -= 1
                queue.append((nr, nc))

        return max_time if fresh == 0 else -1