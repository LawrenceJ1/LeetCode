class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")
        for i in range(len(a)-1, -1, -1):
            if a[i] == "":
                a.pop(i)
        return " ".join(a[::-1])