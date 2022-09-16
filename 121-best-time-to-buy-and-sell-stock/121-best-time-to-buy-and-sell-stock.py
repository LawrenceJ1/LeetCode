class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = prices[0]
        s = 0
        for i in range(1, len(prices)):
            if prices[i] > a:
                s = max(s, prices[i]-a)
            else:
                a = prices[i]
        return s