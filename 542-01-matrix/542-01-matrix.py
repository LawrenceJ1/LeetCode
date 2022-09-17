class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        row_len = len(mat)
        col_len = len(mat[0])
        
        for i in range(row_len):
            for j in range(col_len):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
        
        while queue:
            row, col = queue.popleft()
            if row+1 < row_len and mat[row+1][col] == -1:
                mat[row+1][col] = mat[row][col] + 1
                queue.append((row+1,col))
            if row-1 > -1 and mat[row-1][col] == -1:
                mat[row-1][col] = mat[row][col] + 1
                queue.append((row-1,col))
            if col+1 < col_len and mat[row][col+1] == -1:
                mat[row][col+1] = mat[row][col]+1
                queue.append((row, col+1))
            if col-1 > -1 and mat[row][col-1] == -1:
                mat[row][col-1] = mat[row][col]+1
                queue.append((row,col-1))
        return mat
                    