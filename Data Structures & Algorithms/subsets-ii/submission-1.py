class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #to skip duplicates

        res = []
        def backtrack(i, subset):
            if i>=len(nums):
                res.append(subset.copy())
                return

            #choose
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            
            #dont choose
            while i<len(nums)-1 and nums[i+1]==nums[i]:
                i+=1
            backtrack(i+1, subset)
        
        backtrack(0,[])
        return res