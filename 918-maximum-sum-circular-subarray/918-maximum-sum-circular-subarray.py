class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_sum, min_total, max_sum, max_total, total = 0, float(inf), 0, float(-inf), 0
        for i in range(len(nums)):
            max_sum = max(nums[i], max_sum+nums[i])
            max_total = max(max_total, max_sum)
            
            min_sum = min(nums[i], min_sum+nums[i])
            min_total = min(min_sum, min_total)
            
            total += nums[i]
        if total-min_total == 0:
            return max_total
        return max(total-min_total, max_total)