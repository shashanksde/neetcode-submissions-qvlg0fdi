class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, total, comb):
            if i<len(nums) and total==target:
                res.append(comb.copy())
                return

            if i>=len(nums) or total>target:
                return
            
            #choose i
            comb.append(nums[i])
            backtrack(i, total+nums[i], comb) #note that I can keep choosing the same number multiple times
            comb.pop()

            #dont choose i
            backtrack(i+1, total, comb) #note that I can skip this number and choose the next
            
        backtrack(0, 0,[])
        return res
                