class MyQueue:

    def __init__(self):
        self.stack1 = deque() #this will get the input
        self.stack2 = deque() #this will reverse the input so that stack2 is like a queue
        
    def push(self, x: int) -> None:
        self.stack1.append(x)
    
    def pop(self) -> int:
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        a = self.stack2.pop()
        for j in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return a

    def peek(self) -> int:
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        a = self.stack2[-1]
        for j in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return a

    def empty(self) -> bool:
        if not self.stack1:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()