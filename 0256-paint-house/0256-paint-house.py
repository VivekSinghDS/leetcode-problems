class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        @cache
        def dfs(color, n):
            total_cost = costs[n][color]
            
            if n == len(costs) - 1:
                pass 
            
            elif color == 0:
                total_cost += min(dfs(1, n + 1), dfs(2, n + 1))
                
            elif color == 1:
                total_cost += min(dfs(0, n + 1), dfs(2, n + 1))
                
            else:
                total_cost += min(dfs(0, n + 1), dfs(1, n + 1))
                
            return total_cost
        
        return min(dfs(0, 0), dfs(1, 0), dfs(2, 0))
        
        