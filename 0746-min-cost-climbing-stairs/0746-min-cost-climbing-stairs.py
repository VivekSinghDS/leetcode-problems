class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        @cache
        def dfs(i):
            if i >= n:
                return 0
            
            total = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return total
        
        return min(dfs(0), dfs(1))
        