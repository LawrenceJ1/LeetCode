class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans, counter = 0, [0]*60
        for i in time:
            counter[i%60] += 1
        for i in range(1, 30):
            ans += counter[i]*counter[60-i]
        return ans + counter[0]*(counter[0]-1)//2 + counter[30]*(counter[30]-1)//2