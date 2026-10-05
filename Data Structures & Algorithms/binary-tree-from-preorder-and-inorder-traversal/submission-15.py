# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # in preorder, the first value in list is root
        # in inorder, everything on the left of the root.val is on left subtree
        # and everything on the right is the right subtree of it
        if not preorder or not inorder:
            return None

        # build hashmap for inorder where key = TreeNode.val and val = index
        inorder_index = {
            value : index
            for index, value in enumerate(inorder)
        }

        preorder_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            # declare preorder_index as a global variable 
            nonlocal preorder_index

            # no vals in subtree
            if left > right:
                return None

            # retrieve rootVal from preorder 
            rootVal = preorder[preorder_index]
            preorder_index += 1

            # now we get the starting root node from inorder and its position
            middle = inorder_index[rootVal]

            # initialize the root
            root = TreeNode(rootVal)
            
            # build out left and right subtree in that order
            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root

        return build(0, len(preorder) - 1)