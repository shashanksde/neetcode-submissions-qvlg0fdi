# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        stack = []
        cur = root
        while cur or stack:
            if cur: #move until we have a root to process
                res.append(cur.val) #keep adding the root nodes that come in the path
                stack.append(cur.right) #add right subtrees to process next
                cur = cur.left #move towards left after processing the root
            else:
                cur = stack.pop() #once it reaches a null node pop back up to move right
        return res