# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == root or q == root:
            return root
        queue = deque()
        queue.append(root)
        pointer_p, pointer_q = 0, 0
        index = 0
        memo = {0:[root]}
        
        while queue:
            queue_len = len(queue)
            if pointer_p and pointer_q:
                break
            index += 1
            memo[index] = deque()
            for i in range(queue_len):
                node = queue.popleft()
                if node.left:
                    if p == node.left:
                        pointer_p = node.left
                    elif q == node.left:
                        pointer_q = node.left
                    memo[index].append(node.left)
                    queue.append(node.left)
                if node.right:
                    if p == node.right:
                        pointer_p = node.right
                    elif q == node.right:
                        pointer_q = node.right
                    memo[index].append(node.right)
                    queue.append(node.right)
        
        index -= 1
        while index >= 0:
            for i in range(len(memo[index])):
                if pointer_p == pointer_q:
                    return pointer_p
                if memo[index][i].left:
                    if memo[index][i].left == pointer_p:
                        pointer_p = memo[index][i]
                    if memo[index][i].left == pointer_q:
                        pointer_q = memo[index][i]
                if memo[index][i].right:
                    if memo[index][i].right == pointer_p:
                        pointer_p = memo[index][i]
                    if memo[index][i].right == pointer_q:
                        pointer_q = memo[index][i]
            index -= 1
        return root
        