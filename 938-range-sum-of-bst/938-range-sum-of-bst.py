# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total_sum = 0
        def recursive(root):
            if not root:
                return
            if root.left:
                recursive(root.left)
            if root.right:
                recursive(root.right)
            if root.val >= low and root.val <= high:
                self.total_sum += root.val
        recursive(root)
        return self.total_sum