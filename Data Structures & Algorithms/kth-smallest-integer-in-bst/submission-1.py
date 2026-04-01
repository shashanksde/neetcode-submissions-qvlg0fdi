# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #perform inorder traversal
        #of bst, go all the way left and keep a counter 
        #if counter hits k at some node return that
        cnt = k
        res = root.val
        
        def inorder(node):
            nonlocal cnt, res
            if not node:
                return

            inorder(node.left)
            cnt-=1
            if cnt==0:
                res = node.val
                return
            
            inorder(node.right)
            return
        
        inorder(root)
        return res
        
