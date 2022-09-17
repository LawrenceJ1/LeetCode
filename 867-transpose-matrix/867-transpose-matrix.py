class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        row = []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            ans.append(row)
            row = []
        return ans