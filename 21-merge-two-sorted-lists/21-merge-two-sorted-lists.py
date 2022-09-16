# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1
        
        node = self.dummy = ListNode(-1)
        
        def recursive(list1, list2):
            if not list1:
                self.dummy.next = list2
                return
            if not list2:
                self.dummy.next = list1
                return
            if list1.val <= list2.val:
                self.dummy.next = list1
                self.dummy = self.dummy.next
                recursive(list1.next, list2)
            else:
                self.dummy.next = list2
                self.dummy = self.dummy.next
                recursive(list1, list2.next)
        
        recursive(list1, list2)
        return node.next