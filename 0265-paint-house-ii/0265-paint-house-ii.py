class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        
        @cache
        def dfs(index, previous):
            if index >= len(costs):
                return 0
    
            cost = float('inf')
            for i in range(len(costs[index])):
                if i == previous:
                    continue 
                cost = min(cost, costs[index][i] + dfs(index + 1, i))
            return cost 
        
        return dfs(0, None)
                
                
                
        