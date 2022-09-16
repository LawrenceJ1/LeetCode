# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer = l1
        counter = 0
        new_val = 0
        
        while pointer:
            new_val += (10**counter)*pointer.val
            pointer = pointer.next
            counter += 1
        pointer = l2
        counter = 0
        
        while pointer:
            new_val += (10**counter)*pointer.val
            pointer = pointer.next
            counter += 1
        
        new_val = str(new_val)
        head = node = ListNode(int(new_val[len(new_val)-1]))
        
        for i in range(len(new_val)-2, -1, -1):
            node.next = ListNode(int(new_val[i]))
            node = node.next
        
        return head