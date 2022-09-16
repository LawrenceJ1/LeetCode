class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or len(s)%2==1:
            return False
        stack = deque()
        combinations = {'{':'}', '[':']', '(':')'}
        flag = False
        for x in s:
            if x == "}" or x == "]" or x == ")":
                if not stack or combinations[stack.pop()] != x:
                    return False
            else:
                stack.append(x)
        if stack:
            return False
        return True