class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n + 1)
        dp[0] = 0
        
        squares = [i ** 2 for i in range(n + 1) if i**2 <= n]
        for target in range(1, n + 1):
            for square in squares:
                # square = s ** 2 
                
                if target - square < 0:
                    break 
                
                if 1 + dp[target - square] < dp[target]:
                    dp[target] = 1 + dp[target - square]
                
    
        return(dp[n])
        
        
                
        