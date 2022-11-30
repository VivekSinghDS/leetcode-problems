class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def backtrack(node, cur_comb):
            nonlocal res
            if node == len(graph) - 1:
                res.append(cur_comb[:])
                return 
            
            for neighbor in graph[node]:
                backtrack(neighbor, cur_comb + [neighbor])
                
        backtrack(0, [0])
        return res
        
                
            
            
        