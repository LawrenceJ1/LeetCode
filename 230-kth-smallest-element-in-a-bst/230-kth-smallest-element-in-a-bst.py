# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1
        self.k = k
        self.ans = None
        self.traverse(root)
        return self.ans
        
    def traverse(self, root):
        if not root:
            return 0
        if self.count > self.k:
            return
        self.traverse(root.left)
        if self.count == self.k:
            self.ans = root.val
            self.count += 1
        elif self.count > self.k:
            return
        else:
            self.count += 1
        self.traverse(root.right)
        return