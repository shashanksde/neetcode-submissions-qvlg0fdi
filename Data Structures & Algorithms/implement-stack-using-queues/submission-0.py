class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        #cant do popright on the queue
        #maintain a second queue which keeps track of the elements in reverse
        for i in range(len(self.q1)-1,-1,-1):
            val = self.q1.pop(i)
            self.q2.append(val)
        
        res = self.q2.pop(0)
        for i in range(len(self.q2)-1,-1,-1):
            val = self.q2.pop(i)
            self.q1.append(val)
        return res

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return True if len(self.q1)==0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()