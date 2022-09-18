class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        d = deque([0])
        for i in range(1, len(nums)):
            nums[i] += nums[d[0]]
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            if i-d[0] >= k:
                d.popleft()
        return nums[-1]