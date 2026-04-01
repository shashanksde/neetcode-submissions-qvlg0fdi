class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        use backtracking
        start with empty string 
        at every step I can choose between opening bracket and closing bracket
        if the number of open is more than closing I will add closing else if the balance is zero
        open-close then check if the n value is still pending and perform addition
        '''
        res = []
        perm = []
        def backtrack(openb, closeb):
            if openb == closeb == n:
                res.append("".join(perm))
                return             
            
            if openb<n:
                perm.append("(")
                backtrack(openb+1, closeb)
                perm.pop()
            
            if closeb<openb:
                perm.append(")")
                backtrack(openb, closeb+1)
                perm.pop()
                
        backtrack(0,0)
        return res
            