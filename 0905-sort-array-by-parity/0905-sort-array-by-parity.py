class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        
        while i < j:
            v1 = nums[i] % 2
            v2 = nums[j] % 2
            
            if v1 > v2:
                nums[i], nums[j] = nums[j], nums[i]
                
            if v1 == 0:
                i += 1
                
            if v2 == 1:
                j -= 1
                
        return nums
                
            
            
        