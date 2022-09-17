class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[:] == s[::-1]:
            return True
        p1 = 0
        p2 = len(s)-1
        while p1 < p2:
            if s[p1] != s[p2]:
                if (s[:p1]+s[p1+1:])[::-1] == s[:p1]+s[p1+1:]:
                    return True
                elif (s[:p2]+s[p2+1:])[::-1] == s[:p2]+s[p2+1:]:
                    return True
                else:
                    return False
            p1 += 1
            p2 -= 1