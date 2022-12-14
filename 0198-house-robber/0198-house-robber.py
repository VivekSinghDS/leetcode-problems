class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(n):
            if n < 0:
                return 0
            
            res = 0 
            res = max(dfs(n - 1), nums[n] + dfs(n - 2))
            return res
        
        return dfs(len(nums) - 1)
            