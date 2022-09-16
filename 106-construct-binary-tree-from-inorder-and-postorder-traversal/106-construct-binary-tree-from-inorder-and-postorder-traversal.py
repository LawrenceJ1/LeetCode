# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.mapping = {}
        for x,y in enumerate(inorder): 
            self.mapping[y] = x
        def recursive(left, right):
            if left > right:
                return None
            root = TreeNode(postorder.pop())
            map_index = self.mapping[root.val]
            root.right = recursive(map_index+1, right)
            root.left = recursive(left, map_index-1)
            return root
        return recursive(0, len(postorder)-1)
