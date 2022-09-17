# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans = []
        self.traverse(root)
        for i in range(len(self.ans)-1):
            self.ans[i].right = self.ans[i+1]
        self.ans[-1].right = None
        return self.ans[0]
        
    def traverse(self, root):
        if not root:
            return None
        self.traverse(root.left)
        root.left = None
        self.ans.append(root)
        self.traverse(root.right)
        return root