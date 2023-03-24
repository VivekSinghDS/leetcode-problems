class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        g2 = defaultdict(list)
        for source, target in connections:
            graph[source].append((target, True))
            graph[target].append((source, False))
            
            
            
        # print(graph)
        count = 0
        
        def dfs(node):
            nonlocal count 
            seen.add(node)
            for neighbor, part in graph[node]:
                if neighbor not in seen:
                    
                    if not(part == False):
                        # print(node, neighbor, part)
                        count += 1
                        
                    dfs(neighbor)
                        
        seen = set()
        dfs(0)
        return count 
        