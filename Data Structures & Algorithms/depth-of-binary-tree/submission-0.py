# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        init max depth at 0 , recursively call the dfs from root until it hits the 
        leaf node, update maxdepth at this point if more
        '''
        maxdepth = 1
        if not root:
            return 0
        elif not root.right and not root.left:
            return maxdepth
        
        def dfs(node, depth):
            nonlocal maxdepth
            if not node:
                return
            if not node.left and not node.right:
                depth = depth+1 #account for itself
                maxdepth = max(maxdepth, depth)
                return 
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root,0)
        return maxdepth

        
