class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = [i for i in range(len(graph)) if not graph[i]]
        # print(res)
        @cache
        def dfs(node):
            if node not in seen:
                if graph[node] == []:
                    return True
                
                seen.add(node)
                res = True
                for neighbor in graph[node]:
                    res &= dfs(neighbor)
                    
                seen.remove(node)
                return res
            return False
        
        for i in range(len(graph)):
            seen = set()
            if graph[i]:
                # print(seen)
                if dfs(i):
                    res.append(i)
                # print(seen)
        res.sort()
        return res
            
                    
                
        