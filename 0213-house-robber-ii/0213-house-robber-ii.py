class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def dfs(nums, i):
            if i < 0:
                return 0 
            
            total = max(nums[i] + dfs(nums, i - 2), dfs(nums, i - 1))
            return total 
        
        return max( dfs(tuple(nums[1:]), len(nums[1:]) - 1), 
                  dfs(tuple(nums[:-1]), len(nums[:-1]) - 1))
        