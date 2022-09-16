# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.ans = False
        def traverse(root, cur_sum, targetSum):
            if not root:
                return
            if root.left == None and root.right == None:
                if cur_sum+root.val == targetSum: 
                    self.ans = True
                    return
            traverse(root.left, cur_sum+root.val, targetSum)
            traverse(root.right, cur_sum+root.val, targetSum)
        traverse(root, 0, targetSum)
        return self.ans