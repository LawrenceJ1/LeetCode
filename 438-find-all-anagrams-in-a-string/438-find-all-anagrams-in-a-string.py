class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        letters = [0]*26
        anagram = [0]*26
        ans = []
        x = len(p)
        y = len(s)
        for char in p:
            letters[ord(char)-ord('a')] += 1
        for char in s[:x]:
            anagram[ord(char)-ord('a')] += 1
        for i in range(y-x+1):
            if letters == anagram:
                ans.append(i)
            anagram[ord(s[i])-ord('a')] -= 1
            if i+x < y:
                anagram[ord(s[i+x])-ord('a')] += 1
        return ans