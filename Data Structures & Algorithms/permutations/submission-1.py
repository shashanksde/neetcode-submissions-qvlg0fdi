class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False]*len(nums)
        def backtrack(nums, pick, perm):
            if len(perm)==len(nums):
                res.append(perm.copy())
                return

            
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(nums, pick, perm)
                    perm.pop()
                    pick[i] = False

                    

        
        backtrack(nums,pick,[])
        return res