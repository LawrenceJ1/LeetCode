class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        return int((x*(x+1)/2)-sum(nums))