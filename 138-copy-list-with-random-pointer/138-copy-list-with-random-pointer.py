"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        new_head = node = Node(head.val)
        random_dict = {head: new_head}
        while head.next:
            node.next = Node(head.next.val)
            random_dict[head.next] = node.next
            node = node.next
            head = head.next
        for key in random_dict.keys():
            if not key.random:
                random_dict[key].random = None
            else:
                random_dict[key].random = random_dict[key.random]
        return new_head