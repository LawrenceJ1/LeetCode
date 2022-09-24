# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append([root, [root.val], root.val])
        ans = []
        while queue:
            length = len(queue)
            for i in range(length):
                node, cur, val = queue.popleft()
                if not node.left and not node.right:
                    if val == targetSum:
                        ans.append(cur)
                if node.left:
                    new_val = val+node.left.val
                    queue.append([node.left, cur+[node.left.val], new_val])
                if node.right:
                    new_val = val+node.right.val
                    queue.append([node.right, cur+[node.right.val], new_val])
        return ans