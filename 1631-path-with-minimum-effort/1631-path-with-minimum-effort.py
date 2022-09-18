class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [0, 1, 0, -1, 0]
        m, n = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        distance = [[inf]*n for i in range(m)]
        while heap:
            d, r, c = heappop(heap)
            if d > distance[r][c]:
                continue
            if r==m-1 and c==n-1:
                return d
            for i in range(4):
                x, y = r+directions[i], c+directions[i+1]
                if 0 <= x < m and 0 <= y < n:
                    new_distance = max(d, abs(heights[x][y]-heights[r][c]))
                    if distance[x][y] > new_distance:
                        distance[x][y] = new_distance
                        heappush(heap, (distance[x][y], x, y))
            