class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        x = len(nums)
        for p1 in range(x-2):
            if p1 != 0 and nums[p1] == nums[p1-1]:
                continue
            p2 = p1+1
            p3 = x-1
            if nums[p1]>0 or nums[p3]<0:
                return ans
            while p3 > p2:
                if nums[p1]+nums[p2]+nums[p3]==0:
                    ans.append([nums[p1], nums[p2], nums[p3]])
                    p2 += 1
                    while nums[p2] == nums[p2-1] and p3>p2:
                        p2 += 1
                else:
                    if nums[p1]+nums[p2]+nums[p3]<0:
                        p2 += 1
                    else:
                        p3 -= 1
        return ans