class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        queue = deque()
        visited = set()
        m = len(grid)
        n = len(grid[0])
        count = 1
        
        queue.append((0, 0))
        visited.add((0, 0))
        while queue:
            l = len(queue)
            for i in range(l):
                row, col = queue.popleft()
                if (row, col) == (m-1, n-1):
                    return count
                else:
                    for j in [-1, 0, 1]:
                        for k in [-1, 0, 1]:
                            if (row+j, col+k) not in visited and row+j >= 0 and row+j < m and col+k >= 0 and col+k < n and not grid[row+j][col+k]:
                                visited.add((row+j, col+k))
                                queue.append((row+j, col+k))
            count += 1
        return -1