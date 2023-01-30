class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def dfs(n):
            if n == 0:
                return 0 
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            
            total = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)
            return total
        
        return dfs(n)
        