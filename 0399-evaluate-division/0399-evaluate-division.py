class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)
        
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]
        
        def dfs(x, y, visited):
            if (x not in graph or y not in graph):
                return -1
            
            if y in graph[x]:
                return graph[x][y]
            
            for dependent in graph[x]:
                if dependent not in visited:
                    visited.add(dependent)
                    temp = dfs(dependent, y, visited)
                    if temp == -1:
                        continue 
                        
                    else:
                        return temp * graph[x][dependent]
                    
            return -1
        
        output = []
        for a, b in queries:
            output.append(dfs(a, b, set()))
        return output
            
        