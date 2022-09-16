class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        cur = 0
        cur_num = 0
        
        for num in nums:
            if num-1 not in nums:
                cur = 1
                cur_num = num
                
                while cur_num+1 in nums:
                    cur += 1
                    cur_num += 1
                
                longest = max(longest, cur)
                
        return longest