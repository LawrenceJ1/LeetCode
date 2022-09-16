# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        prev_node = head
        while prev_node.next:
            if prev_node.next.val == val:
                prev_node.next = prev_node.next.next
            else:
                prev_node = prev_node.next
        return head