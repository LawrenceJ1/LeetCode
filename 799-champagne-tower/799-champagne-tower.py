class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*(query_row+2) for _ in range(query_row+2)]
        dp[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                spill = (dp[i][j]-1.0)/2.0
                if spill > 0:
                    dp[i+1][j] += spill
                    dp[i+1][j+1] += spill
        return min(dp[query_row][query_glass], 1)