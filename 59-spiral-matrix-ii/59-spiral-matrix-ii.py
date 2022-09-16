class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        row, col, count, direction = 0, 0, 0, 0
        while count < n**2:
            count += 1
            ans[row][col] = count
            if direction == 0:
                if col + 1 >= n or ans[row][col+1]:
                    direction = 1
                    row += 1
                else:
                    col += 1
            elif direction == 1:
                if row + 1 >= n or ans[row+1][col]:
                    direction = 2
                    col -= 1
                else:
                    row += 1
            elif direction == 2:
                if col-1 < 0 or ans[row][col-1]:
                    direction = 3
                    row -= 1
                else:
                    col -= 1
            else:
                if row-1 < 0 or ans[row-1][col]:
                    direction = 0
                    col += 1
                else:
                    row -= 1
        return ans
                    