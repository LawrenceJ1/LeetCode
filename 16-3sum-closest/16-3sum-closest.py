class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = inf
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if total == target:
                    return total
                elif abs(ans-target) > abs(total-target):
                    ans = total
                if total > target:
                    k-=1
                else:
                    j += 1
        return ans
        