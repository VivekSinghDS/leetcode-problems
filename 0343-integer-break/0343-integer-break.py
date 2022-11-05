class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None, 1]
        
        for m in range(2, n + 1):
            j = m - 1
            i = 1
            
            max_product = 0 
            while i <= j:
                
                max_product = max(max_product, max(dp[i], i) * max(dp[j], j))
                
                i += 1
                j -= 1
                
            dp.append(max_product)
            
        return dp[n]
                
        