# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = 0
        def traverse(tree):
            if not tree:
                return
            if tree.val == target.val:
                self.ans=tree
                return
            if self.ans:
                return
            traverse(tree.left)
            traverse(tree.right)
        traverse(cloned)
        return self.ans