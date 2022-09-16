class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(nums_list=nums[:], cur_list=[]):
            if not nums_list:
                self.ans.append(cur_list[:])
                return
            for i in range(len(nums_list)):
                cur_list.append(nums_list[i])
                if i == len(nums_list):
                    backtrack(nums_list[:i], cur_list)
                else:
                    backtrack(nums_list[:i]+nums_list[i+1:], cur_list)
                cur_list.pop()
        backtrack()
        return self.ans