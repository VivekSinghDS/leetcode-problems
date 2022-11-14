class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy = nums.copy()
        nums_copy.sort()
        l, r = len(nums), 0
        
        for i in range(len(nums)):
            if nums[i] != nums_copy[i]:
                l = min(l, i)
                r = max(r, i)
                
        return r - l + 1 if r - l >= 0 else 0
        