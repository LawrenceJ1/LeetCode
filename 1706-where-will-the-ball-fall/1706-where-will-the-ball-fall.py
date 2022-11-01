class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ret = [0 for i in range(len(grid[0]))]
        for i in range(len(grid[0])):
            row, col = 0, i
            while row < len(grid):
                if grid[row][col] == 1:
                    if col+1 < len(grid[0]) and grid[row][col+1] == 1:
                        row += 1
                        col += 1
                    else:
                        ret[i] = -1
                        break
                else:
                    if col-1 >= 0 and grid[row][col-1] == -1:
                        row += 1
                        col -= 1
                    else:
                        ret[i] = -1
                        break
            if row == len(grid):
                ret[i] = col
        return ret