# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.dict = defaultdict(int)
        self.k = k
        return self.traverse(root)
    
    def traverse(self, node):
        if not node:
            return False
        self.dict[node.val]+=1
        if self.k-node.val in self.dict and (self.k-node.val != node.val or (self.k-node.val == node.val and self.dict[node.val] > 1)):
                return True
        return self.traverse(node.left) or self.traverse(node.right)