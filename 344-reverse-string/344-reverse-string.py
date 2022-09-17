class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursive(s, index):
            if index == len(s):
                return
            temp = s[-index-1]
            recursive(s, index+1)
            s[index] = temp
        recursive(s, 0)