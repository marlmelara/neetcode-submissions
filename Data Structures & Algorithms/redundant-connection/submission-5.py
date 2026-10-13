class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a: int, b: int) -> bool:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False  # Adding this edge creates a cycle

            parent[root_a] = root_b
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]