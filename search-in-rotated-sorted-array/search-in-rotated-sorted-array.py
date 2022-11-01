class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[0] < nums[mid]:
                left = mid+1
            elif target >= nums[0] > nums[mid]:
                right = mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid
        return -1