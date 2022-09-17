class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        b = [False]*(len(nums)+1)
        a = []
        for x in nums: b[x] = True
        for c in range(1, len(b)):
            if b[c] == False:
                a.append(c)
        return a
                