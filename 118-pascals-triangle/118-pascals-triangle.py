class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[1]]
        for i in range(1, numRows):
            a.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    a[i].append(1)
                    continue
                a[i].append(a[i-1][j]+a[i-1][j-1])
        return a