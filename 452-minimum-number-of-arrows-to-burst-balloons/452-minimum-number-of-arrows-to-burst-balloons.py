class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        counter, upper = 0, 0
        for [start, end] in points:
            if counter == 0 or start > upper:
                counter += 1
                upper = end
        return counter