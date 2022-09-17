class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x = sorted(heights)
        a = 0
        for i in range(len(heights)):
            if heights[i] != x[i]:
                a += 1
        return a