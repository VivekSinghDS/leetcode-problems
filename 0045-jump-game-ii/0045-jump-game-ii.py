class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [float('inf') for i in range(len(nums))]
        steps[0] = 0
        for i in range(len(nums)):
            # print(steps)
            no_of_steps = nums[i]
            j = i
            # print(j, j + no_of_steps + 1)
            while j < i + no_of_steps + 1 and j < len(nums):
                # print(j)
                steps[j] = min(steps[j], 1 + steps[i])
                j += 1
                
            # print(steps)
            # print('-'*10)
                
        return steps[-1] 
                
            
                