class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, comb):
            nonlocal res
            if i==len(nums):
                res.append(comb.copy())
                return
            
            #with num at i
            comb.append(nums[i])
            backtrack(i+1, comb)
            comb.pop()

            #without num at i
            backtrack(i+1, comb)
            
            
        backtrack(0,[])
        return res
