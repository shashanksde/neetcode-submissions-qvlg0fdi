class Solution:
    def isValid(self, s: str) -> bool:
        validMap = {"}":"{",")":"(","]":"["}

        res = []
        for b in s:
            if b not in validMap:
                #its a open bracket
                res.append(b)
            else:
                validb = validMap[b] #valid open that should be on top
                if len(res)>0 and validb == res[-1]:
                    res.pop()
                else:
                    return False
        
        return True if len(res)==0 else False

