class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        ans = [0]*1001
        for stone in stones:
            ans[stone] += 1
        greatest = 0
        while sum(ans) > 1:
            for i in range(1000, -1, -1):
                if not greatest:
                    if ans[i] % 2:
                        greatest = i
                        ans[i] = 1
                    else:
                        ans[i] = 0
                else:
                    if ans[i]:
                        ans[greatest-i] += 1
                        ans[i] -= 1
                        ans[greatest] -= 1
                        if greatest-i > i:
                            greatest = greatest-i
                        else:
                            greatest = 0
                        while greatest > i and ans[i]:
                            ans[greatest-i] += 1
                            ans[greatest] -= 1
                            ans[i] -= 1
                            if i < greatest-i:
                                greatest = greatest-i
                            else:
                                greatest = 0
                                break
                        if ans[i] % 2:
                            greatest = i
                            ans[i] = 1
                        else:
                            ans[i] = 0
        return greatest