# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [head]
        pointer = head
        while pointer.next:
            pointer = pointer.next
            nodes.append(pointer)
        if n == len(nodes):
            head = head.next
        else:
            nodes[-n-1].next = nodes[-n].next
        return head