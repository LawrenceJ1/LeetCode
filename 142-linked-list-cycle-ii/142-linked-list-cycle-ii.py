# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        pointer1 = head
        pointer2 = head
        entry = head
        while pointer2 != None and pointer2.next != None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                while pointer1 != entry:
                    entry = entry.next
                    pointer1 = pointer1.next
                return entry
        return