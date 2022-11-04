class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
            
            
        