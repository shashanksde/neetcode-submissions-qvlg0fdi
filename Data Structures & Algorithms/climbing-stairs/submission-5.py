class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(steps):
            if steps in memo: return memo[steps]
            if steps>n: #if the taken steps go over the number of steps allowed
                return 0
            if steps==n: #if the taken number of steps become exactly equal to the number of steps allowed
                return 1
            
            #choose one step + choose two steps
            memo[steps] = dfs(steps+1) + dfs(steps+2)
            
            return memo[steps]
        return dfs(0)