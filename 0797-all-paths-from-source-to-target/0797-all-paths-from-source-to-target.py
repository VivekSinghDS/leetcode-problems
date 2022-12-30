class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        
        @cache
        def dfs(node, cur_comb):
            if node == target:
                res.append(cur_comb + (node,))
                return 
            
            for child in graph[node]:
                if child not in seen:
                    seen.add(child)
                    dfs(child, cur_comb + (node,))
                    seen.remove(child)
        
        seen = set()
        dfs(0, tuple())
        return res