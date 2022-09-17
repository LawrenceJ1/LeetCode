class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.head = None
        self.tail = None
        self.length = k-1
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.tail == None:
            self.head = 0
            self.tail = 0
        elif self.tail == self.length:
            self.tail = 0
        else:
            self.tail += 1
        self.queue[self.tail] = value
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        if self.head == self.length:
            self.head = 0
        else:
            self.head += 1
        if self.queue[self.head] == None:
            self.head = None
            self.tail = None
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head == None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.head == None:
            return False
        if self.head == self.tail+1 or self.head == 0 and self.tail == self.length: 
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()