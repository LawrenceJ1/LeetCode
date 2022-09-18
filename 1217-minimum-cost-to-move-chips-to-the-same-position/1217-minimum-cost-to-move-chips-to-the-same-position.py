class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        if len(position) == 1:
            return 0
        coins_1 = 0
        coins_2= 0
        for x in position:
            if x % 2 == 0:
                coins_1 += 1
            else:
                coins_2 += 1
        return min(coins_1,coins_2)