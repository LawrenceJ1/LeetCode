# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        self.dummy = ListNode(-1, head)
        def recursive(head):
            if not head.next:
                self.dummy.next = head
                return head
            recursive(head.next).next = head
            return head
        head = recursive(head)
        head.next = None
        return self.dummy.next