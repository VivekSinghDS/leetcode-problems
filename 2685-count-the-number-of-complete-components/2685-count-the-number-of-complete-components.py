class DSU:
    def __init__(self, n):
        self.rank = [0 for i in range(n)]
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def insert(self, source, target):
        rootX = self.find(source)
        rootY = self.find(target)
        
        if rootX == rootY:
            return 
        
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = self.parent[rootY]
            
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = self.parent[rootX]
            
        else:
            self.parent[rootX] = self.parent[rootY]
            self.rank[rootY] += 1
        
        
        
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = []
        
        graph = defaultdict(list)
        
        for source, target in edges:
            dsu.insert(source, target)
            graph[source].append(target)
            graph[target].append(source)
            
        mapper = defaultdict(list)
        
        for i in range(n):
            key = dsu.find(i)
            mapper[key].append(i)
        
        count = 0
        for key in mapper:
            length = len(mapper[key])
            flag = True
            for element in mapper[key]:
                # print(length, graph[element])
                if length != len(graph[element]) + 1:
                    flag = False
                    break
            
            if flag:
                count += 1
        # print(mapper)
        # print(graph)
        return count
            
        
         
        