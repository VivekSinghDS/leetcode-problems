class DSU:
    def __init__(self, n):
        self.rank = [0 for i in range(n)]
        self.parent = [i for i in range(n)]
        
    def union(self, rootX, rootY):
        xset = self.find(rootX)
        yset = self.find(rootY)
        
        if xset == yset:
            return 
        
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = self.parent[xset]
            
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = self.parent[yset]
            
        else:
            self.parent[xset] = self.parent[yset]
            self.rank[yset] += 1
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        '''
        graph = defaultdict(list)
        
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
        
        def dfs(node):
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        ans = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
                
        return ans 
        '''
        ds = DSU(n)
        for edge in edges:
            ds.union(edge[0], edge[1])
            
        # print(ds.rank, ds.parent)
        visited = set()
        for i in range(n):
            # if ds.find(i) not in visited:
            visited.add(ds.find(i))
                
        return len(visited)
        
        
            
            
        