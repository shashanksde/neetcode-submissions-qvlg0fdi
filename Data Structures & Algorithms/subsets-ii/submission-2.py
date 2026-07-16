class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #this is necessary whenver you see duplicates in a backtracking problem
        res = []
        def dfs(i, sub):
            if i==len(nums):
                if sub not in res: #make list act like a set
                    res.append(sub.copy()) #every time I find a valid subset I just add it
                return
            
            #decision where we add the current value
            sub.append(nums[i])
            dfs(i+1, sub)
            sub.pop()

            #decision where we skip and move forward
            dfs(i+1, sub)
            
        dfs(0, [])
        return res