class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, u = 1, max(piles)
        while l < u:
            mid = (l+u)//2
            s = 0
            for i in piles:
                s += math.ceil(i/mid)
            if s <= h:
                u = mid
            else:
                l = mid+1
        return u