# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        root = ListNode()
        root.next = self.removeDuplicates(head)
        return root.next
    
    def removeDuplicates(self, head):
        flag = False
        if not head.next:
            return head
        while head.val == head.next.val:
            head = head.next
            flag = True
            if not head.next:
                return head.next
        if not flag:
            head.next = self.removeDuplicates(head.next)
            return head
        else:
            return self.removeDuplicates(head.next)