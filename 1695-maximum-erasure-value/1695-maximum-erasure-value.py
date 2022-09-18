class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = {}
        ans, start, m = nums[0], 0, len(nums)
        flag = False
        temp = nums[:]
        d[nums[0]] = 0
        for i in range(1, m):
            temp[i] += temp[i-1]
            if nums[i] in d and d[nums[i]] >= start:
                if not flag:
                    ans = temp[i-1]
                ans = max(temp[i-1]-temp[start], ans)
                start = d[nums[i]]
                flag = True
            d[nums[i]] = i
        if flag:
            return max(ans, temp[m-1]-temp[start])
        else:
            return temp[m-1]