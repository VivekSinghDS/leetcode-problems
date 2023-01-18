class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max, global_min = nums[0], nums[0]
        cur_max, cur_min = 0, 0
        total = 0 
        
        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)
            total += n 
            
            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)
            
        return max(total - global_min, global_max) if global_max > 0 else global_max
        
        