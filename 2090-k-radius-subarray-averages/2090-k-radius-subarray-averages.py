class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        res = [-1]*len(nums)
        current_sum = 0
        for r in range(len(nums)):
            current_sum += nums[r]
            if r - 2*k < 0:
                continue 
            else:
                res[r - k] = floor(current_sum/(r - l + 1))
                current_sum -= nums[l]
                l += 1
        return res
                
                
                
                
                
            
        