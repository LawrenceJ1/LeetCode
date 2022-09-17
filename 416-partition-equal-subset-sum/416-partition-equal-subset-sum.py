class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        total_sum = total_sum/2
        nums.sort()
        dp = {x:{} for x in range(len(nums))}
        dp[0][nums[0]] = 1
        for i in range(1, len(nums)):
            for j in dp[i-1]:
                if j+nums[i] <= total_sum:
                    dp[i][j+nums[i]] = 1
                dp[i][j] = 1
                if j+nums[i] == total_sum or j == total_sum:
                    return True
        return False