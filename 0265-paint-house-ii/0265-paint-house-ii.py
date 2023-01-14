class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        
        @cache
        def dfs(color, i):
            total = costs[i][color]
            if i == len(costs) - 1:
                return total 
            
            cost = float('inf')
            for j in range(k):
                if j == color:
                    continue 
                    
                cost = min(cost, dfs(j, i + 1))
                
            return total + cost
        
        res = float('inf')
        for j in range(k):
            res = min(res, dfs(j, 0))
            
        return res

                
            
            
            
        