class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def dfs(cur_node, path):
            nonlocal res
            if cur_node == n - 1:
                res.append(path + [cur_node])
                return 
            
            
            for neighbor in graph[cur_node]:
                dfs(neighbor, path + [cur_node])
                
        dfs(0, [])
        return res
                
            
            
        