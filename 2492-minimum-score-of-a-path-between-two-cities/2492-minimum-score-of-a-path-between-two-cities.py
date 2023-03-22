class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # roads.sort(key = lambda x : x[2])
        graph = defaultdict(list)
        
        for source, destination, price in roads:
            graph[source].append((destination, price))
            graph[destination].append((source, price))
            
        # print(graph)
        res = float('inf')
        
        def dfs(node):
            nonlocal res
            if node in seen:
                return 
            seen.add(node)
            
            for neighbor, cost in graph[node]:
                res = min(res, cost)
                dfs(neighbor)
                
        seen = set()
        dfs(1)
        # print(res)
            
        return res