class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # Store (neighbor, edge_index)
        graph = [[] for _ in range(n + 1)]

        for i, (u, v) in enumerate(edges):
            graph[u].append((v, i))
            graph[v].append((u, i))

        visited = [False] * (n + 1)
        parent = [0] * (n + 1)
        parent_edge = [-1] * (n + 1)
        depth = [0] * (n + 1)

        cycle_edges = set()

        def dfs(node: int, incoming_edge: int) -> bool:
            visited[node] = True

            for neighbor, edge_index in graph[node]:
                # Do not immediately travel back across the same edge
                if edge_index == incoming_edge:
                    continue

                if not visited[neighbor]:
                    parent[neighbor] = node
                    parent_edge[neighbor] = edge_index
                    depth[neighbor] = depth[node] + 1

                    if dfs(neighbor, edge_index):
                        return True

                # A visited ancestor means we found the cycle
                elif depth[neighbor] < depth[node]:
                    cycle_edges.add(edge_index)

                    current = node
                    while current != neighbor:
                        cycle_edges.add(parent_edge[current])
                        current = parent[current]

                    return True

            return False

        dfs(1, -1)

        # The answer is the cycle edge appearing latest in the input
        latest_index = max(cycle_edges)
        return edges[latest_index]