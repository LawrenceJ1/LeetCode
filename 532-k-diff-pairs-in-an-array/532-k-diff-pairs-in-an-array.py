class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = defaultdict(int)
        for num in nums:
            ans[num] += 1
        ret = 0
        for key in ans:
            if not k:
                if ans[key] > 1:
                    ret += 1
                continue
            if ans[key-k]:
                ret += 1
            else:
                ans.pop(key-k)
        return ret