class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0 
        cur_sum = 0
        res = float('-inf')
        for r in range(len(nums)):
            cur_sum += nums[r]
            
            while r - l + 1 >= k:
                res = max(res, cur_sum)
                cur_sum -= nums[l]
                l += 1
                
        return float(res) / k
                
        