class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for char in ops:
            if char == "C":
                ans.pop()
            elif char == "D":
                ans.append(ans[-1]*2)
            elif char == "+":
                ans.append(ans[-1]+ans[-2])
            else:
                ans.append(int(char))
        return sum(ans)