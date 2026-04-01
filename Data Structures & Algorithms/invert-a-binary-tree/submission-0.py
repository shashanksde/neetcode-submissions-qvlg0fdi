# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #at each node swap its left and right child
        if not root:
            return root
        
        root.left, root.right = root.right if root.right else None, root.left if root.left else None
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root