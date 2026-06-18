class Solution:
    def isValid(self, s: str) -> bool:
        validMap = {"}":"{",")":"(","]":"["}
        stack = []
        for b in s:
            if b not in validMap:
                #its a open bracket
                stack.append(b)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1]==validMap[b]:
                        stack.pop()
                    else:
                        return False
        return True if not stack else False