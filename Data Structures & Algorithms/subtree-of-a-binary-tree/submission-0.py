# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True #there can be null subroot 
        if not root:
            return False #if there is a subroot and no root given this is not valid

        if self.sameTree(root, subRoot): #we check if the given root and subroot is same trees if yes we can return True
            return True
        return (self.isSubtree(root.left, subRoot) or #last we can check if t is the left subroot 
               self.isSubtree(root.right, subRoot))  #or check if its in the right subroot

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                   self.sameTree(root.right, subRoot.right))
        return False
        #find ptr2 of subRoot
        # def findsecond(node):
        #     if not node:
        #         return 
        #     if node.val == subRoot.val:
        #         return node
            
        #     left = findsecond(node.left)
        #     right = findsecond(node.right)
        #     if left: return left
        #     elif right: return right
        #     else:return None

        # ptr1 = findsecond(root) 
        
        # if not ptr1: return False
        # ptr2 = subRoot
        # def isValid(ptr1, ptr2):
        #     if ptr1 and not ptr2: return True
        #     if not ptr1 and ptr2: return False
        #     if ptr1.val!=ptr2.val:
        #         return False
        #     if ptr1.left!=ptr2.left or ptr1.right!=ptr2.right:
        #         return False
        #     if ptr1.val == ptr2.val:
        #         return True
            
        #     left = isValid(ptr1.left, ptr2.left)
        #     right = isValid(ptr1.right, ptr2.right)
        #     return left and right
        # return isValid(ptr1, ptr2)



            
