class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        ans = Counter(nums)
        return heapq.nlargest(k, ans.keys(), key=ans.get)