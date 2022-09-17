class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        exp = 0
        for i in range(1, n+1):
            if i == 2**(exp+1):
                exp += 1
                ans[i] = 1
            else:
                ans[i] = ans[i-2**exp]+1
        return ans
            