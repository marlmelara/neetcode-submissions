"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {} # hashmap to map old node : new node

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node in oldToNew:
                return oldToNew[node] # returns copy

            # otherwise if not, then we initialize it and make a copy
            oldToNew[node] = Node(node.val)
            copy = oldToNew[node]

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor)) # adds node neighbors to copy

            return copy

        return dfs(node)


            