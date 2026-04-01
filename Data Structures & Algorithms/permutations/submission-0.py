class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm,i):
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            if i>=len(nums):
                return
            
            for i in range(len(nums)):
                if nums[i] not in perm:
                    perm.append(nums[i]) #we pick 1
                    dfs(perm,i) #then explore further with the same choice
                    perm.pop() #only start popping if the max length is reached

        dfs([],0)
        return res
    
    
    
    
    #     1/    \2    \ 3. ---> choices = 3
    #     2 3  /3 \1.  1  2 ---> choice = 2
    #    3/ 2  1/  \3  2.  1 ---> choice = 1

    #i can choose from any of the number 
    #base case would be that perm length = nums

