# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        pointer1 = head.next #1 step
        pointer2 = head.next.next #2 steps
        while pointer2 != None and pointer2.next != None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2 :
                return True
        return False