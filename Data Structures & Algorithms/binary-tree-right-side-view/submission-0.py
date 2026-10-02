# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # I'm thinking we do a BFS approach, where we get the last valid node
        # if any, is there and we return it. if there is only one then we get that

        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            right_visible_node = len(q) - 1

            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                # check if we are at right_visible_node yet
                if i == right_visible_node:
                    res.append(node.val)

        return res