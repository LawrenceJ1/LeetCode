class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            if len(str(n)) % 2 == 0: a += 1
        return a