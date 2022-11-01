class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        
        @cache
        def dfs(color, num_house):
            if num_house == n - 1:
                return costs[num_house][color]
            
            cost = float('inf')
            for next_color in range(k):
                if next_color == color:
                    continue 
                cost = min(cost, dfs(next_color, num_house + 1))
                
            return cost + costs[num_house][color]
        
        res = float('inf')
        for color in range(k):
            res = min(res, dfs(color, 0))
            
        return res
            
        