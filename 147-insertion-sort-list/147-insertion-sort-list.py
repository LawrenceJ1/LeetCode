# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1, head)
        cur = head
        temp, prev = None, None
        
        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                temp = cur.next
                cur.next = cur.next.next
                prev = dummy
                while prev.next and prev.next.val < temp.val:
                    prev = prev.next
                after = prev.next
                prev.next = temp
                temp.next = after
        return dummy.next
        
    