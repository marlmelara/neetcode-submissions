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

            # both nodes are empty
            if not node1 and not node2:
                continue

            # either node is null and other isn't or vals are diff
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # get the children if nodes exist
            if node1 and node2:
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))

        #return true if stack gets completely popped
        return True