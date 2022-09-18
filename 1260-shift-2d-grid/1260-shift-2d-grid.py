class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        k = k%(len(grid)*len(grid[0]))
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans.append(grid[i][j])
        ans = ans[-k:] + ans[:-k]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = ans[i*len(grid[0])+j]
        return grid