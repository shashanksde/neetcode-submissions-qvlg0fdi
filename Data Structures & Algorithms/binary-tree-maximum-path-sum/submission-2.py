# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #max path can be just the left tree or the right tree
        #or it can be the path that goes through the root.
        #pass the max from max(leftsum, rightsum, leftsum+rightsum)
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
        # res = float('-inf')
        # def dfs(root):
        #     nonlocal res
        #     if not root:
        #         return 0
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     res = max(res, left+right+root.val)

        #     return root.val+ max(left, right)
        
        # dfs(root)
        # return res
