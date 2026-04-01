# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        #here main idea is to find the node where the split occurs
        #in other words the node where the paths diverge and bottom up where the paths converge
        while cur:
            if p.val>cur.val and q.val>cur.val:
                cur=cur.right
            elif p.val<cur.val and q.val<cur.val:
                cur=cur.left
            else:
                return cur
        
