class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for src, tar in edges:
            graph[src].append(tar)
            graph[tar].append(src)
            
        seen = set()
        def dfs(node):
            if node == destination:
                return True 
            
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True 
                    
            return False
        
        return dfs(source)
        
        