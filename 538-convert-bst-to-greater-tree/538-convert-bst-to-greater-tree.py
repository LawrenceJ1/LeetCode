# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        self.traverse(root)
        return root
        
    def traverse(self, root):
        if not root:
            return 0
        else:
            self.traverse(root.right)
            root.val = self.total + root.val
            self.total = root.val
            self.traverse(root.left)
            return root.val
            