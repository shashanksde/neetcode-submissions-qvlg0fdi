# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: #in case there is no node itself
            return TreeNode(val)

        cur = root #else if there is a root we assign the cur
        while True: 
            if val > cur.val: #if the val is higher than the current
                if not cur.right: #if there is not a right node
                    cur.right = TreeNode(val) #create a node to its right and return
                    return root
                cur = cur.right #else keep moving right
            else:
                if not cur.left: #opposite of above but logic is the same
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left

            
