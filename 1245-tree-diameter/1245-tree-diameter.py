class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)
            
        diameter = 0
        
        def dfs(node, parent):
            nonlocal diameter
            m1, m2 = 0, 0 
            
            for child in graph[node]:
                if child == parent:
                    continue 
                    
                parent_height = dfs(child, node)
                if parent_height > m1:
                    m1, m2 = parent_height, m1
                    
                elif parent_height > m2:
                    m2 = parent_height
                    
            diameter = max(diameter, m1 + m2)
            return 1 + max(m1, m2)
        
        dfs(0, -1)
        return diameter
                
        