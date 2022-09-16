class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        prev = []
        x = []
        for row in matrix:
            if row[0] == target:
                return True
            elif row[0] > target:
                x = prev
                break
            prev = row
        if not x:
            x = row
        for i in x:
            if i == target:
                return True
        return False