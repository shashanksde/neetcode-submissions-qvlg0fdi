class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        if not root:
            return self.diameter

        def helper(node):
            if not node:
                return 0
            
            leftheight = helper(node.left)
            rightheight = helper(node.right)

            self.diameter = max(self.diameter, leftheight + rightheight)
            return max(leftheight, rightheight) + 1
        
        helper(root)
        return self.diameter