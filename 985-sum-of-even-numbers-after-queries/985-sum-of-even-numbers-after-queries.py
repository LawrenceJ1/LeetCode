class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = 0
        ans = []
        for num in nums:
            if not num % 2:
                even += num
        for i in range(len(queries)):
            val, index = queries[i]
            if not nums[index] % 2:
                even -= nums[index]
            nums[index] += val
            if not nums[index] % 2:
                even += nums[index]
            ans.append(even)
        return ans