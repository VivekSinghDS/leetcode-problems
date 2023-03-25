class DSU:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self, x):
        if x == self.root[x]:
            return self.root[x]
        
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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
            
        counter = Counter([dsu.find(i) for i in range(n)])
        frequencies = list(counter.values())
        running_sum = 0
        total = sum(frequencies)
        ans = 0
        for val in frequencies:
            running_sum += val
            ans += (val * (total - running_sum))
            
        return ans
        print(frequencies)
        
        