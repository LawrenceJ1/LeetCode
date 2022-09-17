class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.top_val = x

    def pop(self) -> int:
        queue_len = len(self.queue)
        for i in range(queue_len-1):
            self.top_val = self.queue.popleft()
            self.queue.append(self.top_val)
        return self.queue.popleft()

    def top(self) -> int:
        return self.top_val
        
    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()