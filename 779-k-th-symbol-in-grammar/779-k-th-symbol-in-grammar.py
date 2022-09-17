class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        self.ans = 1
        def recursive(n, k):
            if n == 1:
                return
            if k%2 == 0:
                self.ans = -self.ans
                k/=2
            else:
                k=(k+1)/2
            recursive(n-1, k)
        recursive(n, k)
        return 0 if self.ans == 1 else 1