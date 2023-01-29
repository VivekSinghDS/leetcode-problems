class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max, global_min = nums[0], nums[0]
        current_max, current_min = 0, 0
        total = 0
        for i in range(len(nums)):
            current_max = max(current_max + nums[i], nums[i])
            current_min = min(current_min + nums[i], nums[i])
            
            
            total += nums[i]
            
            global_max = max(global_max, current_max)
            global_min = min(current_min, global_min)
            
        return max(sum(nums) - global_min, global_max) if global_max > 0 else global_max
        
        
        