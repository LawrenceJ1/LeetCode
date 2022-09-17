class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r = True
        i = 0
        j = 0
        a = len(mat)-1
        b = len(mat[0])-1
        c = [mat[0][0]]
        while i != a or j != b:
            if r:
                if j == b:
                    i += 1
                    r = False
                elif i == 0:
                    j += 1
                    r = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == a:
                    j += 1
                    r = True
                elif j == 0:
                    i += 1
                    r = True
                else:
                    i += 1
                    j -= 1
            c.append(mat[i][j])
        return c