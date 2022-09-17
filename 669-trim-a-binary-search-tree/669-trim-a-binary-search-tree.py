# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        self.low = low
        self.high = high
        return self.traverse(root)
        
    def traverse(self, root):
        if not root:
            return None
        if self.low <= root.val and root.val <= self.high:
            root.left = self.traverse(root.left)
            root.right = self.traverse(root.right)
            return root
        elif self.low > root.val:
            return self.traverse(root.right)
        else:
            return self.traverse(root.left)