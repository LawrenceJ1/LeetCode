# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.answer = 1
        def traverse(root, depth):
            if not root:
                return 
            if root.left == None and root.right == None:
                self.answer = max(self.answer, depth)
                return
            traverse(root.left, depth+1)
            traverse(root.right, depth+1)
        traverse(root, 1)
        return self.answer