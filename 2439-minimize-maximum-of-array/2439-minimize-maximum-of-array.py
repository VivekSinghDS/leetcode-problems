class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_, sum_ = 0, 0
        
        for idx, num in enumerate(nums, start = 1):
            sum_ += num
            
            average, modulo = divmod(sum_, idx)
            if modulo:
                average += 1
                
            max_ = max(max_, average)
            
        return max_
        