class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float(inf)
        left = 0
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            while total_sum >= target:
                ans = min(ans, i + 1 - left)
                total_sum -= nums[left]
                left += 1
        if ans == float(inf):
            return 0
        return ans