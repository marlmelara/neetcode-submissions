class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False # cycle found

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                
                if not dfs(neighbor, node):
                    return False

            return True

        # Start DFS from node 0 and ensure all nodes reached
        return dfs(0, -1) and len(visited) == n