class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = temp = start = 0
        count = defaultdict(int)
        for i in range(len(s)):
            if count[s[i]] and count[s[i]] > start:
                ans = max(temp, ans)
                temp = i+1-count[s[i]]
                start = count[s[i]]
            else:
                temp += 1
            count[s[i]] = i+1
        return max(ans, temp)