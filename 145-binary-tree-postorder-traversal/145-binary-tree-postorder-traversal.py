# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = deque()
        def traverse(root, a):
            if root:
                traverse(root.left, a)
                traverse(root.right, a)
                a.append(root.val)
        traverse(root, a)
        return a