class Solution:
    def fib(self, n: int) -> int:
        
        @cache
        def dfs(n):
            if n == 1 or n == 0:
                return n
            
            if n < 0:
                return 0
            
            ans = dfs(n - 2) + dfs(n - 1)
            
            return ans
        return dfs(n)
            
            
        