class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
#         1 represents alive still being alive, -1 represents alive becoming dead, 2 represents dead becoming alive, 0 represents dead being dead
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                if i-1 >= 0 and (board[i-1][j] == 1 or board[i-1][j] == -1):
                    count += 1
                if i+1 < len(board) and (board[i+1][j] == 1 or board[i+1][j] == -1):
                    count += 1
                if j-1 >= 0 and (board[i][j-1] == 1 or board[i][j-1] == -1):
                    count += 1
                if j+1 < len(board[0]) and (board[i][j+1] == 1 or board[i][j+1] == -1):
                    count += 1
                if i-1 >= 0 and j-1 >= 0 and (board[i-1][j-1] == 1 or board[i-1][j-1] == -1):
                    count += 1
                if i-1 >= 0 and j+1 < len(board[0]) and (board[i-1][j+1] == 1 or board[i-1][j+1] == -1):
                    count += 1
                if i+1 < len(board) and j-1 >= 0 and (board[i+1][j-1] == 1 or board[i+1][j-1] == -1):
                    count += 1
                if i+1 < len(board) and j+1 < len(board[0]) and (board[i+1][j+1] == 1 or board[i+1][j+1] == -1):
                    count += 1
                if board[i][j]:
                    if count != 2 and count != 3:
                        board[i][j] = -1
                else:
                    if count == 3:
                        board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
        