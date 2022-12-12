class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        '''
        # simple top-down approach 
        counter = {"0" : zero, "1" : one}
        
        @cache
        def backtrack(current_string):
            if len(current_string) > high:
                return 0
            
            total = 0
            if low <= len(current_string) <= high:
                total += 1% (10 ** 9 + 7)
                
            for key in counter:
                total += backtrack(current_string + key * counter[key])% (10 ** 9 + 7)
                
            return total % (10 ** 9 + 7)
                
        return backtrack("") 

        '''
        dp = defaultdict(int)
        mod = 10 ** 9 + 7
        
        dp[0] = 1
        
        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
                
            if i - one >= 0:
                dp[i] += dp[i - one]
                
            dp[i] %= mod
        ans = 0   
        for i in range(low, high + 1):
            ans += dp[i]
            
        return ans % mod
            
        
        
        
        
                
                
        