class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        z = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[a] = nums[i]
                a += 1
            else:
                z += 1
        for j in range(1,z+1):
            nums[-j] = 0