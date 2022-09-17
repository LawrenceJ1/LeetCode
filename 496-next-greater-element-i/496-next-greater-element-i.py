class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nextGreater = dict()
        stack = []
        for i, num2 in enumerate(nums2):
            nextGreater[num2] = -1
            while stack and num2 > nums2[stack[-1]]:
                nextGreater[nums2[stack[-1]]] = num2
                stack.pop()
            stack.append(i)
            
        for num1 in nums1:
            ans.append(nextGreater[num1])
        return ans