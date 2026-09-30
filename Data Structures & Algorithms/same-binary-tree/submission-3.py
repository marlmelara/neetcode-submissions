# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            # Both are empty: this pair matches
            if not node1 and not node2:
                continue

            # Exactly one is empty, or values differ
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # Compare corresponding children
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True