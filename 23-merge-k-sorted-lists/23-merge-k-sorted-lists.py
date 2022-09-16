# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def dac(point1, point2):
            head = pointer = ListNode(0)
            while point1 and point2:
                if point1.val < point2.val:
                    pointer.next = point1
                    point1 = point1.next
                else:
                    pointer.next = point2
                    point2 = point2.next    
                pointer = pointer.next
            if not point1:
                pointer.next = point2
            else:
                pointer.next = point1
            return head.next
        x = len(lists)
        interval = 1
        while interval < x:
            for i in range(0, x-interval, interval*2):
                lists[i] = dac(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if x > 0 else None
    
        