class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]
        if starting_pixel == newColor:
            return image
        stack = deque()
        stack.append((sr, sc))
        col_len = len(image[0])
        row_len = len(image)
        
        def dfs(stack, col_len, row_len, starting_pixel):
            if not stack: return image
            row, col = stack[-1]
            if row+1 < row_len and image[row+1][col] == starting_pixel:
                stack.append((row+1, col))
                image[row+1][col] = newColor
                dfs(stack, col_len, row_len, starting_pixel)
            elif row-1 > -1 and image[row-1][col] == starting_pixel:
                stack.append((row-1, col))
                image[row-1][col] = newColor
                dfs(stack, col_len, row_len, starting_pixel)
            elif col+1 < col_len and image[row][col+1] == starting_pixel:
                stack.append((row, col+1))
                image[row][col+1] = newColor
                dfs(stack, col_len, row_len, starting_pixel)
            elif col-1 > -1 and image[row][col-1] == starting_pixel:
                stack.append((row, col-1))
                image[row][col-1] = newColor
                dfs(stack, col_len, row_len, starting_pixel)
            else:
                stack.pop()
                image[row][col] = newColor
                dfs(stack, col_len, row_len, starting_pixel)
        dfs(stack, col_len, row_len, starting_pixel)
        return image