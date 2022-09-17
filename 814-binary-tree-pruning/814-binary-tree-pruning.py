# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        if root.val == -1:
            return None
        self.pruning(root)
        return root
        
    def traverse(self, node):
        if node.left:
            self.traverse(node.left)
        if node.right:
            self.traverse(node.right)
        if node.val == 0:
            if (not node.right or node.right.val == -1) and (not node.left or node.left.val == -1):
                node.val = -1
                return
    
    def pruning(self, node):
        if node.left:
            if node.left.val == -1:
                node.left = None
            else:
                self.pruning(node.left)
        if node.right:
            if node.right.val == -1:
                node.right = None
            else:
                self.pruning(node.right)