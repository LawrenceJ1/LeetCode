class Solution:
    def numDecodings(self, s: str) -> int:
        x = len(s)
        memo = {}
        def dp(i=0):
            if i == x:
                return 1
            if i > x:
                return 0
            if s[i] == "0":
                return 0
            if i not in memo:
                memo[i] = dp(i+1)
                if int(s[i:i+2]) <= 26:
                    memo[i] += dp(i+2)
            return memo[i]
        return dp()
        