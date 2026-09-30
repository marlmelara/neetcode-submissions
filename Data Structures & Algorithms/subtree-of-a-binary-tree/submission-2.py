# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()

            # if current node is empty
            if not node:
                continue

            if node.val == subRoot.val:
                flag = True
                substack = [(node, subRoot)]
                while substack:
                    subNode1, subNode2 = substack.pop()

                    if not subNode1 and not subNode2:
                        continue
                    
                    if not subNode1 or not subNode2 or subNode1.val != subNode2.val:
                        # reset substack for future matches
                        substack = []
                        flag = False
                        break
                    # if both nodes and vals match, append children nodes to compare
                    substack.append((subNode1.right, subNode2.right))
                    substack.append((subNode1.left, subNode2.left))

                if not substack and flag == True:
                    return True

            stack.append(node.right)
            stack.append(node.left)

        return False