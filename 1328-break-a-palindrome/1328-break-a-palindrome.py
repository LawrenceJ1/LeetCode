class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)):
            if palindrome[i] != "a" and i*2+1 != len(palindrome):
                return palindrome[:i]+"a"+palindrome[i+1:]
        return palindrome[:len(palindrome)-1]+"b"