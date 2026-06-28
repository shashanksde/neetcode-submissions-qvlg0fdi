class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        #if the above check failed lets search again in our left subtree and right subtree for possible candidates 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

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