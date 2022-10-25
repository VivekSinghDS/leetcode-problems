class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = min_so_far = result = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            temp_max = max(curr, curr * min_so_far, curr * max_so_far)
            min_so_far = min(curr, curr * min_so_far, curr * max_so_far)
            
            max_so_far = temp_max 
            
            result = max(result, max_so_far)
            
        return result 