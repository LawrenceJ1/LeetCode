class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:        
        # @lru_cache(None)
        # def dp(i, j):
        #     if i == -1 or j == -1:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return dp(i-1, j-1)+1
        #     else:
        #         return max(dp(i-1, j), dp(i, j-1))
        # return dp(len(text1)-1, len(text2)-1)
        n, m = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]