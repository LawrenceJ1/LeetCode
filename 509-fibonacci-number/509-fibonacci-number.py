class Solution:
    def fib(self, n: int) -> int:
        self.cache = {}
        def recursive(n):
            if n in self.cache:
                return self.cache[n]
            if n < 2:
                result = n
            else:
                result = recursive(n-2) + recursive(n-1)
            
            self.cache[n] = result
            return result
        return recursive(n)