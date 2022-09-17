class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get(self, index: int) -> int:
        print(self.head)
        if index >= self.length:
            return -1
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val
            
    def addAtHead(self, val: int) -> None:
        new_head = Node(val, self.head)
        self.head = new_head
        if not self.tail:
            self.tail = new_head
        self.length += 1
        
    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.tail = Node(val)
            self.head = self.tail
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            pass
        elif index == 0:
            self.head = Node(val, self.head)
            self.length += 1
        elif index == self.length:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.length += 1
        else:
            temp = Node(0, self.head)
            for i in range(index):
                temp = temp.next
            next_node = temp.next
            temp.next = Node(val, next_node)
            self.length += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            pass
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        elif index == self.length-1:
            temp = Node(0, self.head)
            for i in range(index):
                temp = temp.next
            self.tail = temp
            self.tail.next = None
            self.length -= 1
        else:
            temp = Node(0, self.head)
            for i in range(index):
                temp = temp.next
            next_node = temp.next.next
            temp.next = next_node
            self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)