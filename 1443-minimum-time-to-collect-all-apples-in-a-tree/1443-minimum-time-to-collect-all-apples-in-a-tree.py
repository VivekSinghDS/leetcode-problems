class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for src, target in edges:
            graph[src].append(target)
            graph[target].append(src)
            
        # print(graph)
        # total = sum(hasApple)
        seen = set()
        def dfs(node, parent):
            res = 0
            
            for neighbor in graph[node]:
                if parent == neighbor:
                    continue 
                    
                res += dfs(neighbor, node)
                
            if hasApple[node] or res:
                res += 2
                
            return res 
        
        return max(dfs(0, -1) - 2, 0)
            
            
        