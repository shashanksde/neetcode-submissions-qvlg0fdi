class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # []            
        # /.          \        \
        # [1]         [2]      [3]
        # /.   \       /
        # [1,2] [1,3] [2,3]
        # /       
        # [1,2,3]
        res = []
        subset = []
        def backtrack(idx):
            if idx>=len(nums):
                res.append(subset.copy())
                return 
            
            subset.append(nums[idx])
            backtrack(idx+1)
            
            subset.pop()
            backtrack(idx+1)

        backtrack(0)
        return res