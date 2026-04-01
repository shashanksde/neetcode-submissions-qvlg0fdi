class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i]=="+":
                a,b = stack.pop(), stack.pop()
                stack.append(str(int(a)+int(b)))
            elif tokens[i]=="-":
                a,b = stack.pop(), stack.pop()
                val = int(b)-int(a)
                stack.append(str(val))
            elif tokens[i]=="*":
                a,b = stack.pop(), stack.pop()
                val = int(a) * int(b)
                stack.append(str(val))
            elif tokens[i]=="/":
                a,b = stack.pop(), stack.pop()
                
                val = int(b)/int(a)
                stack.append(str(int(val)))
            else:
                stack.append(tokens[i])
                
            
        return int(stack[0]) if stack else 0
