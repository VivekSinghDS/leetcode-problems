class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        @cache 
        def solve(i):
            if i == 1:
                return k 
            
            if i == 2:
                return k ** 2
            
            return (solve(i - 1) + solve(i - 2))*(k - 1)
        
        return solve(n)
            
            
        