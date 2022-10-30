class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robber(nums):
            rob1 = rob2 = temp = 0 
            
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
                
            return temp
        
        return max(robber(nums[:-1]), 
                          robber(nums[1:]))
        