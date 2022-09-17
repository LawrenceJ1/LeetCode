class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        if len(nums) == 1:
            return [f"{nums[0]}"]
        left = nums[0]
        ans = []
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i]+1:
                if left == nums[i]:
                    ans.append(f"{left}")
                else:
                    ans.append(f"{left}->{nums[i]}")
                left = nums[i+1]
        if nums[-1] != nums[-2]+1:
            ans.append(f"{nums[-1]}")
        else:
            ans.append(f"{left}->{nums[-1]}")
        return ans