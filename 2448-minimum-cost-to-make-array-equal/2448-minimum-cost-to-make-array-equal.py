class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        combined = [(n, c) for n, c in zip(nums, cost)]
        combined.sort()
        
        total = sum([c for _, c in combined])
        current_sum = 0
        i = 0
        # print(combined)
        # print((total + 1) // 2)
        while current_sum < (total + 1) // 2 and i < len(nums):
            
            current_sum += combined[i][1]
            median = combined[i][0]
            i += 1
        # print(median)
        
        ans = 0
        for i in range(len(nums)):
            ans += (abs(nums[i] - median)*cost[i])
        return ans
        
        