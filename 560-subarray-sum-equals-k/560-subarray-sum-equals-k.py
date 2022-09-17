class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        ans = 0
        sweep = defaultdict(int)
        sweep[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            if sweep[total-k]:
                ans += sweep[total-k]
            else:
                sweep.pop(total-k)
            sweep[total] += 1
        return ans