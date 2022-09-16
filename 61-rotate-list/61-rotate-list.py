# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        pointer = head
        stack = deque()
        while pointer:
            stack.append(pointer)
            pointer = pointer.next
        k = k % len(stack)
        for i in range(k):
            temp = stack.pop()
            temp.next = head
            head = temp
        stack.pop().next = None
        return head
            