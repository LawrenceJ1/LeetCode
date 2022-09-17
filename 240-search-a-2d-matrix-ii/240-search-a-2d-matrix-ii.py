class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def dac(row, left, right, top, bottom):
            if len(matrix)<=row or len(matrix)<=top or len(matrix[0])<=left:
                return False
            if top==bottom and left==right:
                if matrix[top][left]==target:
                    return True
                return False
            if top==bottom:
                for i in range(left, right):
                    if matrix[top][i]==target:
                        return True
                return False
            if left==right:
                for i in range(top, bottom):
                    if matrix[i][left]==target:
                        return True
                return False
            i=left
            flag=False
            for i in range(left, right):
                if matrix[row][i] == target:
                    return True
                if matrix[row][i] > target:
                    flag=True
                    break
            if not flag:
                for j in range(top, bottom):
                    if matrix[j][i] == target:
                        return True
            return (dac((row+1+bottom)//2, left, i, row+1, bottom) or dac((top+row)//2, i, right, top, row))
        return dac(len(matrix)//2, 0, len(matrix[0]), 0, len(matrix))
