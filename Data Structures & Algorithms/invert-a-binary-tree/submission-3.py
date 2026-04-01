# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        #top down approach
        #starting from the root, start swapping the left and right links.
        root.left, root.right = root.right, root.left
        
        #recursively call the function on the left sub tree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root