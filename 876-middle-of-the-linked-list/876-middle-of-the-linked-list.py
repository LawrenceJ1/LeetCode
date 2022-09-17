# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        queue = deque()
        counter = 1
        queue.append(head)
        while head.next:
            head = head.next
            queue.append(head)
            counter += 1
        return queue[counter//2]