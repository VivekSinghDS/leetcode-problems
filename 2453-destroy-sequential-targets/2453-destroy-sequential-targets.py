class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        high, low = float('-inf'), float('inf')
        mapper = {}
        for i in range(len(nums)):
            mapper[nums[i] % space] = 1 + mapper.get(nums[i] % space, 0)
            high = max(high, mapper[nums[i] % space])
        
        
        for i in range(len(nums)):
            if mapper[nums[i] % space] == high:
                low = min(low, nums[i])
                
        return low