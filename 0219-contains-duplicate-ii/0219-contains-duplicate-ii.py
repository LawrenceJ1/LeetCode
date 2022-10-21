class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ans = {}
        for i in range(n):
            if nums[i] not in ans:
                ans[nums[i]] = i
            else:
                if i-ans[nums[i]] <= k:
                    return True
                else:
                    ans[nums[i]] = i
        return False