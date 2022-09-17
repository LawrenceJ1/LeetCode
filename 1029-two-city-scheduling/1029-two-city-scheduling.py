class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        cost = 0
        for i in range(int(len(costs)/2)):
            cost += costs[i][0]
        for i in range(int(len(costs)/2), len(costs)):
            cost += costs[i][1]
        return cost