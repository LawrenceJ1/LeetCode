class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(dest, pos, val=1.0):
            if pos == dest:
                self.flag = True
                self.val = val
                return
            for i in self.pairs[pos]:
                if i[0] not in self.visited:
                    if self.flag:
                        return
                    self.visited.add(i[0])
                    dfs(dest, i[0], i[1]*val)
                         
        self.pairs = defaultdict(list)
        self.visited = set()
        self.flag = False
        self.val = 0.0
        ans = [-1]*len(queries)
        for i, num in enumerate(equations):
            self.pairs[num[0]].append((num[1], values[i]))
            self.pairs[num[1]].append((num[0], 1.0/values[i]))
        for j, i in enumerate(queries):
            if not self.pairs[i[0]]:
                continue
            dfs(i[1], i[0])
            if self.val:
                ans[j] = self.val
                self.val = 0.0
            self.visited = set()
            self.flag = False
        return ans