class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()
        components = 0

        # explore adj list fully and add node to visited set
        def dfs(node: int) -> int:
            if node in visited:
                return

            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)

        # go through each node and dfs explore each component
        # then iterate by one on each seperate component
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components