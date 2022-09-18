class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        x = len(changed)
        if x % 2:
            return []
        changed.sort()
        check = Counter(changed)
        ans = []
        for i in range(x):
            if check[changed[i]]:
                check[changed[i]] -= 1
                ans.append(changed[i])
                if changed[i]*2 not in check:
                    return []
                check[changed[i]*2] -= 1
        return [] if sum(check.values()) else ans