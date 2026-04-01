# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root,subRoot): #if starting at root/ this node its the same tree we can
            #immediately return True
            return True
        #else call recursively on the left subTree and right subTree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, p, q):
        if not p and not q: #both are null then they are same
            return True
        if not p or not q or p.val!=q.val: #if one of them is null or they dont match in value
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right,q.right)) 