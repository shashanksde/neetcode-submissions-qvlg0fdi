class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inmap = {}
        #map where each element is at in inorder map val: idx
        for i, val in enumerate(inorder):
            if val not in inmap:
                inmap[val] = i
            else:
                continue #not needed here
        
        pre_idx = 0
        def helper(left_in, right_in):
            nonlocal inmap, pre_idx
            if left_in > right_in:
                return None
            
            val = preorder[pre_idx]
            node = TreeNode(val)
            pre_idx += 1
            
            #now get where the index of this value is in inmap
            idx = inmap[val]
            node.left = helper(left_in, idx - 1)
            node.right = helper(idx + 1, right_in)

            return node
        
        return helper(0, len(inorder) - 1)