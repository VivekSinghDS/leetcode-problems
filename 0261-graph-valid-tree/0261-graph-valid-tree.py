class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 < len(edges):
            # print('here')
            return False
        
        graph = defaultdict(list)
        for src, tar in edges:
            graph[src].append(tar)
            graph[tar].append(src)
        
        # print(graph)
        def dfs(node, parent):
            if node in visited:
                return False 
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node):
                        return False
                
            return True 
        
        visited = set()
        return dfs(0, -1) and len(visited) == n

        
        
        