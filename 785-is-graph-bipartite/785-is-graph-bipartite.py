class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        queue = deque()
        queue.append((0, 1))
        for i in range(len(graph)):
            if i in visited:
                continue
            queue.append((i, 1))
            visited[i] = 1
            while queue:
                pos, color = queue.popleft()
                for node in graph[pos]:
                    if node in visited:
                        if visited[node] == color:
                            return False
                    else:
                        queue.append((node, -1*color))
                        visited[node] = -1*color
        return True