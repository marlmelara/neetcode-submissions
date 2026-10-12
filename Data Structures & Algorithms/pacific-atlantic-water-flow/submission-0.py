class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            reachable = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in reachable
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        reachable.add((nr, nc))
                        queue.append((nr, nc))

            return reachable

        pacific_starts = []

        # Top row and left column
        for c in range(cols):
            pacific_starts.append((0, c))
        for r in range(rows):
            pacific_starts.append((r, 0))

        atlantic_starts = []

        # Bottom row and right column
        for c in range(cols):
            atlantic_starts.append((rows - 1, c))
        for r in range(rows):
            atlantic_starts.append((r, cols - 1))

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if (r, c) in pacific and (r, c) in atlantic
        ]