class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [0] * (rowIndex+1)
        b = []
        for i in range(rowIndex+1):
            for j in range(1, i):
                a[j] = b[j-1] + b[j]
            a[i] = 1
            b = a[:]
        for i in range(len(a)-1, -1, -1):
            if a[i] == 0:  
                a.pop()
            else:
                break                
        return a