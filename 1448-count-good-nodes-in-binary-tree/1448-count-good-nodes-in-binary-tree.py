# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.traverse(-inf, root)
        return self.ans
        
    def traverse(self, val, root):
        if root.val >= val:
            val = root.val
            self.ans += 1
        if root.left:
            self.traverse(val, root.left)
        if root.right:
            self.traverse(val, root.right)