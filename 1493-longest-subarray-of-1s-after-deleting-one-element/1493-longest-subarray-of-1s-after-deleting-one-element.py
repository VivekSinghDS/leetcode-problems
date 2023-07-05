class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0 
        res = 0
        zero_count = 0
        if 0 not in nums:
            return len(nums) - 1
        for r in range(len(nums)):
            # print(nums[l: r + 1])
            if nums[r] == 0:
                zero_count += 1
                
            while zero_count > 1 and l < r:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            
            # print(nums[l: r + 1])
            res = max(res, r - l + 1 if zero_count == 0 else r - l)
                    
        return res
        