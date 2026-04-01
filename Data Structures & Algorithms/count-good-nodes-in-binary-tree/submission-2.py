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

        def dfs(node, pathmax):
            nonlocal count
            if not node:
                return 

            if node.val >= pathmax:
                pathmax = node.val
                count+=1
            
            dfs(node.left, pathmax)
            dfs(node.right, pathmax)
        
        dfs(root, maxval)
        return count