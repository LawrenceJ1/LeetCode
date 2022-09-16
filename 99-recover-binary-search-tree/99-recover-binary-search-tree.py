# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.tree = [TreeNode(-inf)]
        self.traverse(root)
        self.tree.append(TreeNode(inf))
        x = [self.tree[i].val for i in range(len(self.tree))]
        pos1, pos2 = 0, 0
        for i in range(1, len(self.tree)-1):
            if x[i] > x[i-1] and x[i] < x[i+1]:
                continue
            else:
                if not pos1:
                    pos1 = i
                else:
                    pos2 = i
        temp = self.tree[pos1].val
        self.tree[pos1].val = self.tree[pos2].val
        self.tree[pos2].val = temp
        
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.tree.append(root)
        self.traverse(root.right)
        