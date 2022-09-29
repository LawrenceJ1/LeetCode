class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        queue = deque()
        for i in range(len(arr)):
            if len(queue) < k:
                queue.append(arr[i])
            else:
                if abs(queue[-1] - x) > abs(arr[i] - x) and abs(queue[-1] - x) >= abs(queue[0] - x):
                    queue.pop()
                    queue.append(arr[i])
                elif abs(queue[0] - x) > abs(arr[i] - x):
                    queue.popleft()
                    queue.append(arr[i])
        return queue