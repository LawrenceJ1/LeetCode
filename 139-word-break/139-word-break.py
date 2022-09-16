class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        x = [len(word) for word in wordDict]
        y = len(wordDict)
        z = len(s)
        ans = [0]*(z+1)
        ans[0] = 1
        
        for i in range(z):
            for j in range(y):
                if i+1 >= x[j] and ans[i+1-x[j]] and s[i-x[j]+1:i+1]==wordDict[j]:
                    ans[i+1] = 1
                    break
        return ans[-1]