class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums = [num for num, _ in itertools.groupby(nums)]
        if len(nums) == 1:
            return 1
        for i in range(len(nums)-1):
            nums[i] = nums[i+1]-nums[i]
        length = 1
        positive = True if nums[0] >= 0 else False
        for i in range(1, len(nums)-1):
            if positive:
                if nums[i] < 0:
                    length += 1
                    positive = False
            else:
                if nums[i] > 0:
                    length += 1
                    positive = True
        return length+1