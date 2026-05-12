class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        bramap = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c in bramap: #its a close bracket
                if stack and stack[-1] == bramap[c]:
                    stack.pop()
                else:
                    return False #we have a close left and nothing to pop
            else:
                stack.append(c)
        
        return True if not stack else False