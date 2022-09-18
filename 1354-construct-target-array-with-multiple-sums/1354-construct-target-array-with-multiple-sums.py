class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = []
        for num in target:
            heappush(heap, -num)
        s = sum(target)
        while True:
            cur = -heappop(heap)
            if cur == 1:
                return True
            if cur == s:
                return False
            new = (cur-1)%(s-cur)+1
            if new == cur:
                return False
            s = s - cur + new
            heappush(heap, -new)
            