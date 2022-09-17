class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                x, z = inf,inf
                if j-1 >= 0:
                    x = matrix[i-1][j-1]
                y = matrix[i-1][j]
                if j+1 < n:
                    z = matrix[i-1][j+1]
                matrix[i][j] += min(x, y, z)
        ans = inf
        for j in range(n):
            ans = min(matrix[m-1][j], ans)
        return ans