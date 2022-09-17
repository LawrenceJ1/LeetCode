class Solution:
    def numSquares(self, n: int) -> int:
        for x in range(100):
            if x**2 > n:
                upperbound = x
                break
        steps = 0
        queue = deque([x**2 for x in range(1, upperbound)])
        check = set()
        check.add(n)
        while check:
            steps += 1
            temp = set()
            for x in check:
                for y in queue:
                    if x == y:
                        return steps
                    elif y > x:
                        break
                    temp.add(x-y)
            check = temp
        return steps