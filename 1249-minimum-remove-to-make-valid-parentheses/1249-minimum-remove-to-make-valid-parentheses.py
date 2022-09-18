class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        closed = 0
        ans = deque()
        stack = deque()
        for i, char in enumerate(s):
            if char == ")":
                if closed == 0:
                    ans.append("")
                    continue
                ans.append(char)
                closed -= 1
                ans[stack.pop()] = "("
            elif char == "(":
                closed += 1
                ans.append("")
                stack.append(i)
            else:
                ans.append(char)
        return "".join(ans)
            