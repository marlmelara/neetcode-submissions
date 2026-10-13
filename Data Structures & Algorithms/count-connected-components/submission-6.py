class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adj list
        adj = [[] for _ in range(n)]

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        # create visited set and create dfs function to explore a component
        visited = set()

        def dfs(node: int) -> None:
            if node in visited:
                return None

            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)

        componentCount = 0

        for node in range(n):
            if node not in visited:
                componentCount += 1
                dfs(node)

        # after iterating through each node and exploring if new component
        # we return the total componentCount
        return componentCount 