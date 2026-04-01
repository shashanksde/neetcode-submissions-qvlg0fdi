class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        def dfs(target):
            nonlocal count
            if target>n:
                return
            if target==n:
                count+=1
                return 
            
            count+=1
            dfs(target+1)
            count-=1
            dfs(target+2)
        
        dfs(0)
        return count
