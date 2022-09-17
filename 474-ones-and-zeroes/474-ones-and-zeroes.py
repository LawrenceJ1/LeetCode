class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.ans = 0
        self.strs = strs
        self.len = len(strs)
        self.dp(0, m, n, 0)
        return self.ans
        
    @lru_cache(None)
    def dp(self, index: int, m: int, n: int, length: int):
        self.ans = max(self.ans, length)
        if index == self.len:
            return
        if m == 0 and n == 0:
            return
        x=self.strs[index]
        temp_n = n
        temp_m = m
        for char in x:
            if char == "1":
                temp_n -= 1
            else:
                temp_m -= 1
        if temp_m >= 0 and temp_n >= 0:
            self.dp(index+1, temp_m, temp_n, length+1)
        self.dp(index+1, m, n, length)