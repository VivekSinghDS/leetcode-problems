class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [float('inf') for i in range(len(nums))]
        steps[0] = 0
        
        for i in range(len(nums)):
            no_of_steps = nums[i]
            
            for j in range(i + 1, min(i + no_of_steps + 1, len(nums))):
                steps[j] = min(steps[j], 1 + steps[i])
        
        # print(steps)
        return steps[-1]