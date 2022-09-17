"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        stack = deque()
        pointer1 = None
        dummy = pointer2 = Node()
        stack.append(head)
        
        while stack:
            pointer1 = stack.pop()
            
            if pointer1.next:
                stack.append(pointer1.next)
            
            if pointer1.child:
                stack.append(pointer1.child)
                pointer1.child = None
            
            pointer2.next = pointer1
            pointer1.prev = pointer2
            pointer2 = pointer1
        dummy.next.prev = None
        return head