# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = deque()
        def traverse(root, a):
            if root:
                traverse(root.left, a)
                a.append(root.val)
                traverse(root.right, a)
                
        traverse(root, a)
        return a