class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t=="+":
                a, b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif t=="-":
                b, a = stack.pop(), stack.pop()
                stack.append(a-b)
            elif t=="*":
                a,b = stack.pop(), stack.pop()
                stack.append(a*b)
            elif t=="/":
                b,a = stack.pop(), stack.pop()
                if b!=0:
                    stack.append(int(a/b)) 
                else:
                    stack.append(0)
            else:
                stack.append(int(t))
        
        return stack[-1]