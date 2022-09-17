class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        x = len(graph)
        if x == 1:
            return 0
        y = (1 << x) - 1
        count = 1
        queue = deque()
        for i in range(x):
            queue.append([i, 1 << i])
        visited = set()
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                cur, seen = queue.popleft()
                for node in graph[cur]:
                    temp = seen | (1 << node)
                    if temp == y:
                        return count
                    if (node, temp) not in visited:
                        visited.add((node, temp))
                        queue.append([node, temp])
            count += 1
        return 0