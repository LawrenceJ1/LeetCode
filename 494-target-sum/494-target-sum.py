class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i=0, s=0):
            if (i, s) not in memo:
                ans = 0
                if i==self.x:
                    if s==target:
                        ans = 1
                else:
                    ans = dfs(i+1, s-nums[i]) + dfs(i+1, s+nums[i])
                memo[(i, s)] = ans
            return memo[(i, s)]
        memo = {}
        self.x = len(nums)
        return dfs()