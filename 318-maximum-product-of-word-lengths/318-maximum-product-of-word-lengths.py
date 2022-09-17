class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = defaultdict(int)
        ans = 0
        for char in words:
            d[char] = 0
            for c in char:
                d[char] = d[char] | 1 << ord(c)-97
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (d[words[i]] & d[words[j]]):
                    ans = max(len(words[i])*len(words[j]), ans)
        return ans
                    