# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = head
        pos = 1
        while pos < left:
            head = head.next
            pos += 1
        arr = []
        temp = head
        while pos <= right:
            arr.append(temp.val)
            temp = temp.next
            pos += 1
        for val in arr[::-1]:
            head.val = val
            head = head.next
        return ans