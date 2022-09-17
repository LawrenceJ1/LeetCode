class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
#         m, n = len(matrix), len(matrix[0])
#         self.ans = 0
        
#         @lru_cache(None)
#         def dp(i, j):
#             if i == m or j == n:
#                 return 0
#             x = min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1))+1
#             if matrix[i][j] == '0':
#                 return 0
#             self.ans = max(self.ans, x)
#             return x
#         dp(0, 0)
#         return self.ans**2
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])+1
                    ans = max(ans, dp[i][j])
        return ans**2