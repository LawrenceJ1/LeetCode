class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)):
            if nums[a] < nums[i]:
                a = i
        for j in range(len(nums)):
            if nums[j]*2 > nums[a]:
                if j != a:
                    return -1
        return a