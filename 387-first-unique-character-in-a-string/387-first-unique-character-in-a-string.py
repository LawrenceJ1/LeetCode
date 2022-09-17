class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = inf
            else:
                d[s[i]] = i
        ans = min(d.values())
        return ans if ans != inf else -1