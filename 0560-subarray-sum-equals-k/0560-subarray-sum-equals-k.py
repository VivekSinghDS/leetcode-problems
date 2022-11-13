class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        h = {0: 1}
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            res += h.get(diff, 0)
            h[cur_sum] = 1 + h.get(cur_sum, 0)
            
        return res
            
                
            
            
                
            
        