class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        x = len(s)
        index = 0
        for char in t:
            if s[index] == char:
                index += 1
                if index == x:
                    return True
        return False