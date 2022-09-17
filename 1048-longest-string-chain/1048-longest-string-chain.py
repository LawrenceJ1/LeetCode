class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ans = {}
        largest = 1
        words.sort(key=lambda x: len(x))
        for word in words:
            ans[word] = 1
        for word in words:
            for k in range(len(word)-1):
                if word[:k] + word[k+1:] in ans:
                    ans[word] = max(ans[word[:k]+word[k+1:]]+1, ans[word])
                    largest = max(largest, ans[word])
            if word[:-1] in ans:
                ans[word] = max(ans[word[:-1]]+1, ans[word])
                largest = max(largest, ans[word])
        return largest