class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans = defaultdict(int)
        for char in ransomNote:
            ans[char] += 1
        for char in magazine:
            if char in ans and ans[char] > 0:
                ans[char] -= 1
        return True if sum(ans.values()) == 0 else False