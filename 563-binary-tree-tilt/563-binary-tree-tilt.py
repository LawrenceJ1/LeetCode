# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def find(a):
            if not a:
                return 0
            l = find(a.left)
            r = find(a.right)
            self.sum += abs(l-r)
            return a.val+l+r
        find(root)
        return self.sum