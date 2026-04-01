# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #start from root
        def valid(node,left,right):
            if not node:
                return True
            if not (node.val<right and node.val>left):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))
        #check if left child is in the range (-inf, root not includive)
        #and right child is in the range(root not inclusive to +inf)
        #for nodes in the next level this range will get updated until we hit a null node
        # if all of them return True then its valid BST.
        #if one of them return false then break and immediately return false
