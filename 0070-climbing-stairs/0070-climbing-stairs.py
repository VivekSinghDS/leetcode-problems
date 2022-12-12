class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dfs(n):
            if n == 0:
                return 1
            
            elif n < 0:
                return 0 
            
            total = 0
            total = dfs(n - 1) + dfs(n - 2)
            return total
        
        return dfs(n)
        