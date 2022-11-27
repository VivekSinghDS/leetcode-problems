class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def bound_counting(bound):
            count = 0
            ans = 0 
            
            for n in nums:
                count = count + 1 if n <= bound else 0
                ans += count
                
            return ans
                
        return bound_counting(right) - bound_counting(left - 1)
            
        