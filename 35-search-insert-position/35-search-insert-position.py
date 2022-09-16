class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        u = len(nums) - 1
        l = 0
        if nums[u]<target:
            return u+1
        elif nums[l]>target:
            return l
        while l<u:
            if nums[(u+l)//2] > target:
                u = (u+l)//2
            elif nums[(u+l)//2] < target:
                l = (u+l)//2+1
            else:
                return (u+l)//2
        if nums[l] < target and nums[u] > target:
            return u
        elif nums[l]>target:
            return l
        else:
            return (u+l)//2