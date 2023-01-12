class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)
        
        res = [None]*n

        def dfs(node, parent):
            current_f = [0]*26
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    f = dfs(neighbor, node)
                    
                    for i in range(26):
                        current_f[i] += f[i]
                        
            current_f[ ord(labels[node]) - ord('a') ] += 1
            res[node] = current_f[ ord(labels[node]) - ord('a') ]
            return current_f
        
        dfs(0, -1)
        return res
                    
                
        