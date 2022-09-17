class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = sum(nums)
        s = 0
        for i in range(len(nums)):
            if a - s - nums[i] == s:
                return i
            s += nums[i]
        return -1