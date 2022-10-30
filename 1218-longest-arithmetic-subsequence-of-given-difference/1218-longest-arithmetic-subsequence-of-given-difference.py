class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        '''
        if len(arr) <= 2:
            return len(arr)
        

        def solve(i):
            if i < 0:
                return 0 
            
            ans = 0
            for j in range(i - 1, -1, -1):
                if arr[i] - arr[j] == difference:
                    ans = max(ans, 1 + solve(j))
                    
            return ans
        
        res = 1
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] - arr[i] == difference:
                    res = max(res, 2 + solve(i))
                
        return res
        
        '''
        
        dp = {}
        max_val = 1
        for n in arr:
            if n - difference in dp:
                dp[n] = 1 + dp[n - difference]
                
            else:
                dp[n] = 1
                
            max_val = max(dp[n], max_val)
            
        return max_val
                
            
        
                
                
            