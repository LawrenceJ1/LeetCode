class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area, stack = 0, [-1]
        heights.append(0)
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                area = max(area, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        return area