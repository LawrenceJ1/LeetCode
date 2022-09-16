class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0]*len(nums)
        a[0] = nums[0]
        for i in range(1, len(nums)):
            a[i] = max(a[i-1] + nums[i], nums[i])
        return max(a)