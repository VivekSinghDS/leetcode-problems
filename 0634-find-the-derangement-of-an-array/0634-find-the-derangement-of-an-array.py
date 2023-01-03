class Solution:
    def findDerangement(self, n: int) -> int:
        mod = 10**9 + 7
        '''
        @lru_cache(None)
        def dp(n):
            if n == 0:
                return 1
            if n == 1:
                return 0
            
            if n == 2:
                return 1
            
            total = 0 
            
            total = ((n - 1)%mod)*((dp(n - 1)%mod) + (dp(n - 2)%mod))
            return total % mod
        
        return dp(n)
        
        '''
        if n <= 1:
            return 0
        dp = [0]*(n + 1)
        
        dp[1] = 0
        dp[2] = 1
        
        for i in range(3, n + 1):
            first = dp[i - 1] % mod
            second = dp[i - 2] % mod
            total = (first + second) % mod
            dp[i] = ((i - 1)*total)%mod
            
        return dp[n]
        