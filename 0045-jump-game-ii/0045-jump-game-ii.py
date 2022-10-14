class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
                
            l = r + 1
            r = farthest
            res += 1
            
        return res
        # dp = [float('inf')]*len(nums)
        # dp[0] = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, min(nums[i] + i + 1, len(nums))):
        #         dp[j] = min(dp[j], dp[i] + 1)
        # return dp[len(nums) - 1]
        