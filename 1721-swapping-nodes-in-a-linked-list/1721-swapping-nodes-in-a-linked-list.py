# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodesList = []
        dummy = head
        while head:
            nodesList.append(head)
            head = head.next
        temp = nodesList[k-1].val
        nodesList[k-1].val = nodesList[-k].val
        nodesList[-k].val = temp
        return dummy