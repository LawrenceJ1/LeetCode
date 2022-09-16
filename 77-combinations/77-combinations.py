class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        def backtrack(comb=[], num=1):
            if len(comb)==k:
                self.ans.append(comb[:])
            for i in range(num, n+1):
                if i+k-len(comb)>n+1: break
                comb.append(i)
                backtrack(comb, i+1)
                comb.pop()
        backtrack()
        return self.ans