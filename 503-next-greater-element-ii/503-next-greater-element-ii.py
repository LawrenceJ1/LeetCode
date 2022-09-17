class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        stack = []
        circular = [*nums, *nums]
        for i, num in enumerate(circular):
            while stack and num > circular[stack[-1]]:
                try:
                    ans[stack[-1]] = num
                except:
                    ans[stack[-1]-len(nums)] = num
                stack.pop()
            stack.append(i)
        return ans