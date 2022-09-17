class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        ans = {0: 0}
        sol = 0
        for i in range(len(nums)):
            if nums[i]:
                count += 1
            else:
                count -= 1
            if count in ans:
                sol = max(i+1-ans[count], sol)
            else:
                ans[count] = i+1
        return sol