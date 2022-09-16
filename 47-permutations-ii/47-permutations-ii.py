class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.visited = set()
        self.dp(nums, [])
        return self.ans
        
    def dp(self, nums, array):
        if tuple(array) not in self.visited:
            if not nums:
                self.visited.add(tuple(array))
                self.ans.append(array)
            else:
                for i in range(len(nums)):
                     self.dp(nums[:i]+nums[i+1:], array+[nums[i]])
                    
            