class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        cur = 0
        for n in nums:
            cur += n
            res = max(res, cur)
            if cur < 0:
                cur = 0 
                
            
            
        return res 
            