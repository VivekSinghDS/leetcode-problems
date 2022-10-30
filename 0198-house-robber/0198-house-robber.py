class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2, 1, 1, 3
        @cache
        def dfs(i):
            if i >= len(nums):
                return 0 
            
            return max(dfs(i + 2) + nums[i], dfs(i + 1))
        
        return dfs(0)