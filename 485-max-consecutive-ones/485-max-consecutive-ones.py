class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        max_one = 0
        for x in nums:
            if x == 1:
                max_one += 1
            else:
                if max_one > max_ones:
                    max_ones = max_one
                max_one = 0
        if max_one > max_ones:
            max_ones = max_one
        return max_ones