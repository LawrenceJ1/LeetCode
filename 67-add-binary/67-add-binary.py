class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [i for i in str(int(a) + int(b))]
        for x in range(len(a)-1, 0, -1):
            if int(a[x]) > 1:
                a[x] = str(int(a[x])-2)
                a[x-1] = str(int(a[x-1])+1)
        if int(a[0]) > 1:
            a[0] = str(int(a[0])-2)
            a.insert(0, "1")
        return "".join(a)