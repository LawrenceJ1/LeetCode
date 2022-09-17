"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        ans = []
        queue.append(root)
        while queue:
            length = len(queue)
            cur = []
            for _ in range(length):
                temp = queue.popleft()
                for node in temp.children:
                    queue.append(node)
                cur.append(temp.val)
            ans.append(cur)
        return ans