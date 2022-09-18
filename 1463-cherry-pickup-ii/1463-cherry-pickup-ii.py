class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        
        @lru_cache(None)
        def traverse(pos1=0, pos2=cols-1, row=0):
            if pos1 < 0 or pos2 < 0 or pos1 >= cols or pos2 >= cols:
                return 0
            cherries = 0
            cherries+=grid[row][pos1]
            if pos1 != pos2:
                cherries+=grid[row][pos2]
            if row!=rows-1:
                cherries += max(traverse(new_pos1, new_pos2, row+1) 
                                for new_pos1 in [pos1, pos1+1, pos1-1] 
                                for new_pos2 in [pos2, pos2+1, pos2-1])
            return cherries
        return traverse()