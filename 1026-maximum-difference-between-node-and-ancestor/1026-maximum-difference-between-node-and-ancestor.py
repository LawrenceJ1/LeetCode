# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode], max_val=-inf, min_val=inf) -> int:
        if not root:
            return max_val-min_val
        max_val = max(max_val, root.val)
        min_val = min(min_val, root.val)
        return max(self.maxAncestorDiff(root.left, max_val, min_val), self.maxAncestorDiff(root.right, max_val, min_val))
        
            