class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = float(-inf)
        max2 = float(-inf)
        max3 = float(-inf)
        f = False
        for x in nums:
            if x > max1: max1 = x
        for x in nums:
            if x > max2 and x != max1: max2 = x
        for x in nums:
            if x > max3 and x != max1 and x != max2: 
                max3 = x
                f = True
        if f:
            return max3
        else:
            return max1