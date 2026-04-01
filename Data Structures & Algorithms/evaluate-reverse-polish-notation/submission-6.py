class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c=="+":
                stack.append(stack.pop()+stack.pop())
            elif c=="-":
                #32- means 3-2 thus a=2, b=3
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif c=="*":
                stack.append(stack.pop()*stack.pop())
            elif c=="/":
                #here similar to subtraction
                #32/ means 3/2 a=2, b=3 when we pop i.e b/a

                a,b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                #simply add value to the stack
                stack.append(int(c))
        return stack[0]