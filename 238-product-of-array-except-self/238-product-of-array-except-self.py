class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        b, c = 1, 1
        a = [1]*len(nums)
        for i in range(len(nums)):
            a[i] *= b
            a[-1-i] *= c
            b *= nums[i]
            c *= nums[-1-i]
        return a