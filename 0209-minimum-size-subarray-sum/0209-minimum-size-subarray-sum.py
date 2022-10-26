class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        max_sum = float('inf')
        cur_sum = 0
        for r in range(len(nums)):
            
            cur_sum += nums[r]    
            while cur_sum >= target:
                max_sum = min(r - l + 1, max_sum)
                cur_sum -= nums[l]
                l += 1
            
            
        return max_sum if max_sum != float('inf') else 0
        