# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.traverse(root, [0 for _ in range(9)])
        return self.ans
        
    def traverse(self, node, nodes):            
        if node.left:
            nodes[node.val-1] += 1
            self.traverse(node.left, nodes)
            nodes[node.val-1] -= 1
        if node.right:
            nodes[node.val-1] += 1
            self.traverse(node.right, nodes)
            nodes[node.val-1] -= 1
        if not node.left and not node.right:
            nodes[node.val-1] += 1
            if self.isPalindrome(nodes):
                self.ans += 1
            nodes[node.val-1] -= 1
            
    def isPalindrome(self, nodes):
        oneOdd = 0
        for num in nodes:
            if num % 2 == 1:
                oneOdd += 1
                if oneOdd == 2:
                    return False
        return True