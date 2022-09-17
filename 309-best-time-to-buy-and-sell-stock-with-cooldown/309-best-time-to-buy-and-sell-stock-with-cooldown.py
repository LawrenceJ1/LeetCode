class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = len(prices)
        
        @lru_cache(None)
        def dp(day=0, holding=0):
            if day >= x:
                return 0
            if holding:
                return max(dp(day+1, 1), prices[day]+dp(day+2, 0))
            else:
                return max(dp(day+1, 0), -prices[day]+dp(day+1, 1))
        return dp()