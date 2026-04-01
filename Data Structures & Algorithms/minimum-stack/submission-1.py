class MinStack:

    def __init__(self):
        self.minstack = []
        self.minval = float('inf')

    def push(self, val: int) -> None:
        if val<self.minval:
            self.minval = val
        self.minstack.append([val,self.minval])
        return

    def pop(self) -> None:
        self.minstack.pop()
        if self.minstack:
            self.minval = self.minstack[-1][1] #if we pop a element the new minval is the one on top
        else:
            #if its become empty reset minval such that future push will have new minval
            self.minval = float('inf')
        return

    def top(self) -> int:
        return self.minstack[-1][0] if self.minstack else 0
        
    def getMin(self) -> int:
        return self.minval
        
