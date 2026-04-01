# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node): #this function will return height not diameter
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left) #calculate left and right height
            right = dfs(node.right)
            res = max(res, left+right) #calculate diameter at this node
            return 1+max(left, right) #return to the function calls inside here with max left or right tree
        
        dfs(root)
        return res