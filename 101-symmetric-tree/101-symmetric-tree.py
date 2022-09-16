# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue1 = deque()
        queue2 = deque()
        def traverse(root, queue, flag):
            if not root:
                queue.append(None)
                return
            if flag:
                traverse(root.left, queue, flag)
                traverse(root.right, queue, flag)
            else:
                traverse(root.right, queue, flag)
                traverse(root.left, queue, flag)
            queue.append(root.val)
        traverse(root.left, queue1, True)
        traverse(root.right, queue2, False)
        for i in range(len(queue1)):
            if queue1.pop() != queue2.pop():
                return False
        return True