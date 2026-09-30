# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # knowing this is a BST and all node values are unique
        # if p.val and q.val is smaller than curr.val, we move left
        # same idea other way if p.val and q.val is biggger, we move right
        if not root:
            return None

        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if curr.val is in between the two or curr.val is EQUAL to -
            # either p.val or q.val then we can return that node
            else:
                return curr

        return None