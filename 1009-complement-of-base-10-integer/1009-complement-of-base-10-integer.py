class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if not n: return 1
        i = 1
        while i <= n:
            i = i << 1
        return (i-1)^n