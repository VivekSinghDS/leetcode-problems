class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache 
        def dfs(i):
            if i <= 1:
                return 0 
            
            down_one = cost[i - 1] + dfs(i - 1)
            down_two = cost[i - 2] + dfs(i - 2)
            return min(down_one, down_two)
        
        return dfs(len(cost))