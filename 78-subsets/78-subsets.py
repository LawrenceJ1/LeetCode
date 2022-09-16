class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]        
        for num in nums:
            ans += [n + [num] for n in ans]
        return ans