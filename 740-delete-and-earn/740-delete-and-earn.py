class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        nums.sort()
        for num in nums:
            dp[num] += num
        ans = []
        keys = []
        for key in dp:
            keys.append(key)
        for key in keys:
            ans.append(dp[key])
            if not dp[key+1]:
                ans.append(0)
        ans[1] = max(ans[0], ans[1])
        for i in range(2, len(ans)):
            ans[i] = max(ans[i]+ans[i-2], ans[i-1])
        return ans[-1]
        
