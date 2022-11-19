class UF:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
            
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return False 
        
        else:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                
                
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
                
            return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF(len(edges))
        
        for src, tar in edges:
            if not uf.union(src - 1, tar - 1):
                return [src, tar]
        