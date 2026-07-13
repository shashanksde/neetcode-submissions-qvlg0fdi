class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, perm):
            nonlocal res

            if len(perm)==len(nums): #if our current permutation reaches the length of nums, then we have formed our permutation
                res.append(perm.copy())
                return
            
            #make a choice out of all nums 
            for j in range(len(nums)):
                if nums[j] not in perm: #skip the ones already included
                    perm.append(nums[j])
                    dfs(i+1, perm)
                    perm.pop()
            
            return
        
        dfs(0, [])
        return res