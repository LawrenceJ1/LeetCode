# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.traverse(root)
    
    def traverse(self, node):
        cur = str(node.val)
        if node.left and node.right:
            cur += "("+self.traverse(node.left)+")"+"("+self.traverse(node.right)+")"
        elif not node.left and node.right:
            cur += "()("+self.traverse(node.right)+")"
        elif node.left and not node.right:
            cur += "("+self.traverse(node.left)+")"
        return cur