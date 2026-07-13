class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #we can make a decision to include a number always and skip a number always
        res = []

        def dfs(i, sum, comb):
            nonlocal res
            if i>=len(nums) or sum>target:
                return
            if sum==target:
                res.append(comb.copy())
                return

            #always include the current number
            comb.append(nums[i])
            sum+=nums[i]
            dfs(i, sum, comb)
            comb.pop()
            sum-=nums[i]
            
            #always skip the current number
            dfs(i+1, sum, comb)
            return
        
        dfs(0,0,[])
        return res