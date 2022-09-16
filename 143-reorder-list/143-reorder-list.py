# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque()
        pointer = head
        while pointer:
            queue.append(pointer)
            pointer = pointer.next
            
        if len(queue) == 1:
            return head
        
        first = queue.popleft()
        last = queue.pop()
        first.next = last
        
        while queue:
            first = queue.popleft()
            last.next = first
            if len(queue):
                last = queue.pop()
                first.next = last
                last.next = None
            else:
                first.next = None
        return head