# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.list_nodes = []
        while head:
            self.list_nodes.append(head.val)
            head = head.next
            
    def getRandom(self) -> int:
        choice = random.randint(0, len(self.list_nodes)-1)
        return self.list_nodes[choice]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()