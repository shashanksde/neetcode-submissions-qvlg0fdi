# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return count
        maxval = root.val-1

        def dfs(node,maxval):
            nonlocal count
            if not node:
                return 
            
            if node.val>=maxval:
                maxval = node.val
                count+=1
            
            dfs(node.left, maxval)
            dfs(node.right, maxval)
        
        dfs(root,maxval)
        return count

