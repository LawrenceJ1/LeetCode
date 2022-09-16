class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        x = len(nums)
        s = [0]*x
        s[0] = nums[0]
        s[1] = max(nums[0], nums[1])
        for i in range(2, x):
            s[i] = max(nums[i]+s[i-2], s[i-1])
        return s[x-1]