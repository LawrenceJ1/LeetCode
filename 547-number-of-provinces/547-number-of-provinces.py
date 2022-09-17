class DisjointSet:
    def __init__(self, size):
        self.rank = [1]*size
        self.root = [i for i in range(size)]
        self.count = size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
            self.count -= 1
            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = DisjointSet(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected[i])):
                if isConnected[i][j]:
                    provinces.union(i, j)
        return provinces.count