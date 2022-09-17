# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def traverse(node=root, val=""):
            if not node:
                return 0
            if not node.right and not node.left:
                return int(val+str(node.val), 2)
            return traverse(node.right, val+str(node.val)) + traverse(node.left, val+str(node.val))
        return traverse()
        