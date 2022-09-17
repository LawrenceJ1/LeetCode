class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(list)
        x = {}
        a = set()
        for i in range(len(s)):
            d[s[i]].append(i)
            a.add(s[i])
            x[i] = a.copy()
        index = -1
        cur = d[s[0]][-1]
        ans = []
        while True:
            org = cur
            m = cur
            for char in x[cur]:
                if d[char][-1] > cur:
                    m = max(d[char][-1], m)
            cur = m
            if cur == len(s)-1:
                ans.append(cur-index)
                return ans
            elif cur != d[s[org]][-1]:
                continue
            elif cur == d[s[org]][-1]:
                ans.append(cur-index)
                index = cur
                cur = d[s[cur+1]][-1]