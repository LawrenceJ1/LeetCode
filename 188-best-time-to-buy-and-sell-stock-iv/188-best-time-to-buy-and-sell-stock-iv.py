class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        x = len(prices)
        
        @lru_cache(None)
        def dp(day=0, transactions=k, cur=0):
            if day == x or not transactions:
                return 0
            if not cur:
                return max(-prices[day]+dp(day+1, transactions, 1),dp(day+1, transactions, 0))
            else:
                return max(prices[day]+dp(day+1, transactions-1, 0),dp(day+1, transactions, 1))
        return dp()
