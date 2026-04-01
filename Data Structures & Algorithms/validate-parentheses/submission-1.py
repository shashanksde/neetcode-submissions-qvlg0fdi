class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charmap = {"}":"{",")":"(","]":"["}
        for br in s:
            if br not in charmap: #its a opening bracket, push to stack
                stack.append(br)
            else:
                top = stack[-1] if stack else None
                if not top: return False #starts with closing
                if charmap[br]==top: #closing and opening matches
                    #pop from stack
                    stack.pop()
                else:
                    #doesnt match
                    return False
        
        return True if not stack else False