class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        d = [0, 0, 1, 0] #left up right down
        c = 1
        e = len(matrix)*len(matrix[0])
        f = [matrix[i][j]]
        g = [1, 0, len(matrix)-1, len(matrix[0])-1] #top bound, left bound, right bound, bottom bound
        while True:
            if i == g[2] and d[3]:
                d[3] = 0
                d[0] = 1
                g[2] -= 1
            elif j == g[3] and d[2]:
                d[2] = 0
                d[3] = 1
                g[3] -= 1
            elif i == g[0] and d[1]:
                d[1] = 0
                d[2] = 1
                g[0] += 1
            elif j == g[1] and d[0]:
                d[0] = 0
                d[1] = 1
                g[1] += 1
            if d[0]:
                j -= 1
            elif d[1]:
                i -= 1
            elif d[2]:
                j += 1
            else:
                i += 1
            if c == e:
                break
            else:
                c += 1
            f.append(matrix[i][j])
        return f