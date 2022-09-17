class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        if len(set(pattern)) != len(set(s)):
            return False
        pairs = {}
        for i in range(len(s)):
            try:
                if pairs[pattern[i]] != s[i]:
                    return False
            except:
                pairs[pattern[i]] = s[i]
        return True