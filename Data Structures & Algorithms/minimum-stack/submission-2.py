class MinStack:

    def __init__(self):
        self.stack1 = []
        

    def push(self, val: int) -> None:
        self.stack1.append(val)

    def pop(self) -> None:
        self.stack1.pop()
        

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return min(self.stack1)
        
