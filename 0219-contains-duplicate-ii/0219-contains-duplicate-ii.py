class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ans = defaultdict(int)
        for i in range(n):
            ans[nums[i]] += 1
            if i > k:
                ans[nums[i-k-1]] -= 1
            if ans[nums[i]] > 1:
                return True
        return False