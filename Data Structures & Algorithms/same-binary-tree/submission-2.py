# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both empty → same
        if not p and not q:
            return True
        # One empty, the other not → different
        if not p or not q:
            return False
        # Values must match AND subtrees must both match
        return (p.val == q.val 
                and self.isSameTree(p.left, q.left) 
                and self.isSameTree(p.right, q.right))