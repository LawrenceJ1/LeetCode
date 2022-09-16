"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        new_root = root
        node = dummy = Node(0)
        while new_root:
            if new_root.left:
                node.next = new_root.left
                node = new_root.left
            if new_root.right:
                node.next = new_root.right
                node = new_root.right
            new_root = new_root.next
            if not new_root:
                new_root = dummy.next
                node = dummy = Node(0)
        return root