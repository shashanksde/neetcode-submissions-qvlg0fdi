class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(comb, total, i):
            if total>target or i>=len(nums):
                return
            
            if total==target:
                res.append(comb.copy())
                return
            
            comb.append(nums[i])
            dfs(comb, total+nums[i],i) #i was incrementing i
            comb.pop()
            dfs(comb, total, i+1) #here I was doing it right
        
        dfs([],0,0)
        return res