# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.mapping = {x:y for y,x in enumerate(inorder)}
        self.counter = 0
        def recursive(left,right):
            if left > right:
                return None
            root = TreeNode(preorder[self.counter])
            self.counter += 1
            map_index = self.mapping[root.val]
            root.left = recursive(left, map_index-1)
            root.right = recursive(map_index+1, right)
            return root
        return recursive(0, len(preorder)-1)