class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        visited = deque()
        
        def remove_queen(row, col):
            counter = 1
            for i in range(row+1, n):
                visited.pop()
                if col+counter < n:
                    visited.pop()
                if col-counter >= 0:
                    visited.pop()
                counter += 1
        
        def backtrack(row=0):
            for col in range(n):
                if (row, col) not in visited:
                    if row+1==n:
                        self.count+=1
                    else:
                        counter = 1
                        for i in range(row+1, n):
                            visited.append((i, col))
                            if col+counter < n:
                                visited.append((i, col+counter))
                            if col-counter >= 0:
                                visited.append((i, col-counter))
                            counter += 1
                        backtrack(row+1)
                        remove_queen(row, col)
        
        backtrack()
        return self.count