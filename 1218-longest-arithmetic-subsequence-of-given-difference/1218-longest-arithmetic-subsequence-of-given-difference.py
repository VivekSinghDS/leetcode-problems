class Solution:
    def longestSubsequence(self, nums: List[int], difference: int) -> int:
        dp = defaultdict(int)
        
        for n in nums:
            dp[n] = 1 + dp[n - difference]
            
        return max(dp.values())
            
        
                
                
            