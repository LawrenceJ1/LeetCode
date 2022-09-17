class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = 0
        prev = None
        i = 0
        while i < len(seats) and seats[i] == 0:
            i += 1
        prev = i
        dist = i
        while i < len(seats):
            if seats[i] == 1:
                dist = max((prev+i)//2 - prev, dist)
                prev = i
            i += 1
        return max(dist, len(seats)-1-prev)
        