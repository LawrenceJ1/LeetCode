class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        x = len(nums)//2
        b = 0
        t = len(nums)
        if t == 1:
            return nums[x]
        while True:
            if x == len(nums)-1 or (nums[x] != nums[x+1] and nums[x] != nums[x-1]):
                return nums[x]
            if x % 2 == 0:
                if nums[x] == nums[x+1]:
                    b = x+1
                else:
                    t = x
            else:
                if nums[x] == nums[x-1]:
                    b = x+1
                else:
                    t = x
            x = (b+t)//2