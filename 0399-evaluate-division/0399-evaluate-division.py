class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for i, (numerator, denominator) in enumerate(equations):
            graph[numerator][denominator] = values[i]
            graph[denominator][numerator] = 1/values[i]
            
        # print(graph)
        def dfs(numerator, denominator):
            if numerator not in graph or denominator not in graph:
                return -1
            
            elif denominator in graph[numerator]:
                return graph[numerator][denominator]
            
            for potential_denominator in graph[numerator]:
                if potential_denominator not in seen:
                    seen.add(potential_denominator)
                    temp = dfs(potential_denominator, denominator)
                    if temp == -1:
                        continue
                    else:
                        return temp * graph[numerator][potential_denominator]
            return -1
        
        res = []
        for numerator, denominator in queries:
            seen = set()
            res.append(dfs(numerator, denominator))
        return res 
            
        
        