class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        def backtrack(complete=[], palindrome=[], index=0):
            if index == len(s):
                self.ans.append(complete[:])
            for i in range(index, len(s)):
                palindrome.append(s[i])
                if palindrome[:] == palindrome[::-1]:
                    prev = complete[:]
                    complete.append("".join(palindrome[:]))
                    backtrack(complete, [], i+1)
                    complete = prev
        backtrack()
        return self.ans