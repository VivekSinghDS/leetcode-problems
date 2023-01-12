class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i < 0:
                return 0
            
            total = max(nums[i] + dfs(i - 2), dfs(i - 1))
            return total
        
        return dfs(len(nums) - 1)
        
        
        
        
        