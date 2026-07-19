class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open_, close, comb):
            nonlocal res
            if len(comb)>2*n:
                return
                
            if len(comb)==2*n:
                res.append("".join(comb.copy()))
                return
            
            #decision to include a open bracket
            if open_<n:
                comb.append("(")
                dfs(open_+1, close, comb)
                comb.pop()
            #decision to include a close bracket
            if close<open_:
                comb.append(")")
                dfs(open_, close+1, comb)
                comb.pop()
            return
        
        dfs(0,0,[])
        return res