# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # handle if root is null
        if not root:
            return "N"

        # BFS approach
        q = deque([root])
        values = []

        while q:
            node = q.popleft()

            if not node:
                values.append("N")
                continue

            values.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        return ",".join(values)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # handle if root is null
        values = data.split(",")

        if values[0] == "N":
            return None

        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()

            # check left subtree
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1

            #check right subtree
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1

        return root