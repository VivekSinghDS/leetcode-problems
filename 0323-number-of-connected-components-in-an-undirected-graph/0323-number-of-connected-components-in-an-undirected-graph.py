class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for src, tar in edges:
            graph[src].append(tar)
            graph[tar].append(src)
            
        visited = set()
        ans = 0
        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
                
        for i in range(n):
            # print(visited)
            if i not in visited:
                dfs(i)
                ans += 1
                
        return ans 
        