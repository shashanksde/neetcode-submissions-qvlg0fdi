class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n<=0:return res

        def backtrack(open_, close, comb):
            if (len(comb)==2*n) and (open_ - close) == 0:
                st = "".join(comb.copy())
                res.append(st)
                return
            
            if len(comb)>2*n or open_-close<0:
                return
            
            #includes open
            comb.append("(")
            backtrack(open_+1, close, comb)
            comb.pop()

            #include close
            comb.append(")")
            backtrack(open_, close+1, comb)
            comb.pop()

        backtrack(0,0,[])
        return res


        #i need to start with open bracket 
        #if the number of open is greater than close I can include a close
        #if I see there is more closed than open its a invalid one I shouldnt include it.
        #base case is if num_open == num_close and is a valid paranthesis 
        # we can check by having open = +1 close = -1
        #if it ever becomes negative we dont proceed
        # then we can return all collected paranthesis