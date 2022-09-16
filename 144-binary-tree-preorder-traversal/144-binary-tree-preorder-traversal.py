# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        a = deque()
        
        def traverse(root, a):
            if root:
                a.append(root.val)
                traverse(root.left, a)
                traverse(root.right, a)
            
        traverse(root, a)
        return a
