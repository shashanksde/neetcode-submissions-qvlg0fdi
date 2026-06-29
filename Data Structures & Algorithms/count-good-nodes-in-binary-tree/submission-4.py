class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodnodes = 0
        if not root:
            return goodnodes
        def dfs(node, greater_val):
            nonlocal goodnodes
            if not node:
                return
            
            if node.val >= greater_val:
                goodnodes += 1
                greater_val = node.val
            
            dfs(node.left, greater_val)
            dfs(node.right, greater_val)
            return
        
        dfs(root, root.val)
        return goodnodes