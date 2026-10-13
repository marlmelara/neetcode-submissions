class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        # create adj list for undirected graph, bc its undirected we must do
        # both forward and backword from the edges
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        # create a visited set where we keep track of all visited nodes
        visited = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False

            # add visited node to our set
            visited.add(node)

            # check our neighbors for any cycles
            for neighbor in adj[node]:
                # since its undirected, the neighbor can be our parent
                if neighbor == parent:
                    continue
                #check if a cycle is found by seeing if our dfs ever returns False
                if not dfs(neighbor, node):
                    return False

            # if nothing ever gets triggered, return True
            return True

        # check if all nodes were visited as well
        if dfs(0, -1) and len(visited) == n:
            return True
        else:
            return False