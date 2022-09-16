class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = deque()
        islands = 0
        a = len(grid[0])
        for i in range(len(grid)):
            for j in range(a):
                if grid[i][j] == "1":
                    islands += 1
                    stack.append((i, j))
                    self.dfs(grid, i, j, stack)
        return islands
    
    def dfs(self, grid, i, j, stack):
        if i + 1 < len(grid) and grid[i+1][j] == "1":
            grid[i+1][j] = "0"
            stack.append((i+1, j))
            self.dfs(grid, i+1, j, stack)
        elif i - 1 >= 0 and grid[i-1][j] == "1":
            grid[i-1][j] = "0"
            stack.append((i-1, j))
            self.dfs(grid, i-1, j, stack)
        elif j + 1 < len(grid[0]) and grid[i][j+1] == "1":
            grid[i][j+1] = "0"
            stack.append((i, j+1))
            self.dfs(grid, i, j+1, stack)
        elif j - 1 >= 0 and grid[i][j-1] == "1":
            grid[i][j-1] = "0"
            stack.append((i, j-1))
            self.dfs(grid, i, j-1, stack)
        else:
            stack.pop()
            if not stack:
                return None
            self.dfs(grid, stack[-1][0], stack[-1][1], stack)
            