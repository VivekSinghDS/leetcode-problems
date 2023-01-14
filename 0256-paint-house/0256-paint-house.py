class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        @cache 
        def dfs(color, i):
            total_cost = costs[i][color]
            if i == len(costs) - 1:
                return costs[i][color]
            
            elif color == 0:
                total_cost += min(dfs(1, i + 1), dfs(2, i + 1))
                
            elif color == 1:
                total_cost += min(dfs(0, i + 1), dfs(2, i + 1))
                
            elif color == 2:
                total_cost += min(dfs(0, i + 1), dfs(1, i + 1))
                
            return total_cost
        
        return min(dfs(0, 0), dfs(1, 0), dfs(2, 0))
                
            
        