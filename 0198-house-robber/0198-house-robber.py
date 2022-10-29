class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2, 1, 1, 3
        @cache
        def dfs(index):
            if index >= len(nums):
                return 0 
            
            ans = max(dfs(index + 2) + nums[index], dfs(index + 1))
            return ans 
            
        return dfs(0) 