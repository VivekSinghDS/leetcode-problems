class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        total = 0
        
        for n in nums:
            total += abs(nums[len(nums) // 2] - n)
            
        return total
            
        