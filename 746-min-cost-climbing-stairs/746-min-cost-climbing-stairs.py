class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x = len(cost)
        p1, p2 = cost[1], cost[0]
        for i in range(2, x):
            temp = p1
            p1 = min(p2, p1) + cost[i]
            p2 = temp
        return min(p1, p2)