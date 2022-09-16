class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = {0: 0, 1: 1, 2: 2}
        def recursive(n):
            if n not in self.cache:
                self.cache[n] = recursive(n-2) + recursive(n-1)
            return self.cache[n]
        return recursive(n)