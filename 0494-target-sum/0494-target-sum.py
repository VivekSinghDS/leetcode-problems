class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = 0
        n = len(nums)
        
        memo = {}
        def backtrack(index, remain):
            nonlocal total
            if index == n:
                if remain == 0:
                    return 1
                    
                return 0
            
            elif (index, remain) in memo:
                return memo[(index, remain)]
            
            
            total = (backtrack(index + 1, remain - nums[index]) + 
            backtrack(index + 1, remain + nums[index]))
            memo[(index, remain)] = total
            return total
            
        return backtrack(0, target)
        # return total
                