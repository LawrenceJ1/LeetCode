class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur, total, start = 0, 0, 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i+1
        return -1 if (total < 0) else start