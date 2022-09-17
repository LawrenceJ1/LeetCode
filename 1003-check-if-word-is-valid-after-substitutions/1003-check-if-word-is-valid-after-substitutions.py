class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3:
            return False
        while "abc" in s:
            s = s.replace("abc", "")
        return not s
                