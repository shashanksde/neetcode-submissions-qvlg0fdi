# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #remember to pass the max of left and right height to the callee node
        #but update the diameter based max(diameter, l_height+r_height)
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            #bottom up recursion
            #calculation starts from the leaf nodes
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            res = max(res, left_height+right_height) #res is updated such that it includes both left and right height
            return 1+max(left_height, right_height) #this is important because this function is returning the max of left or right height
        
        dfs(root)
        return res