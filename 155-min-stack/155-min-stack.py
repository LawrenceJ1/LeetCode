class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val.append(min(val, self.min_val[-1]) if self.min_val else val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_val.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()