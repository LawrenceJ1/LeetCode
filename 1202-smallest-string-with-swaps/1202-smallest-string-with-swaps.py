class DisjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1 
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        ans = ''
        disjoint = DisjointSet(n)
        for i in pairs:
            disjoint.union(i[0], i[1])
        for i in range(n):
            disjoint.find(i)
        parent = disjoint.root
        d = defaultdict(deque)
        for i in range(n):
            d[parent[i]].append(s[i])
        for key in d:
            d[key]=deque(sorted(d[key]))
        for i in range(n):
            key = parent[i]
            ans += (d[key].popleft())
        return ans