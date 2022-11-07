class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(remain, index):
            if remain == 0:
                return True 
            
            if remain < 0 or index == len(nums):
                return False 
            
            return dfs(remain, index + 1) or dfs(remain - nums[index], index + 1)
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        return dfs(total // 2, 0)
    