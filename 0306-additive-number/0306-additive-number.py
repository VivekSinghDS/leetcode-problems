class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:
        if len(nums) < 3:
            return False
        
        for i in range(len(nums) // 2):
            if nums[0] == "0" and i > 0:
                break 
                
            for j in range(i + 1, len(nums) - 1):
                if nums[i + 1] == "0" and j > i + 1:
                    break 
                    
                nums1 = int(nums[:i + 1])
                nums2 = int(nums[i + 1 : j + 1])
                
                start = j + 1 
                
                while start <= len(nums) - 1 and nums[start:].startswith(str(nums1 + nums2)):
                    nums1, nums2 = nums2, nums1 + nums2
                    start += len(str(nums2))
                    
                if start == len(nums):
                    return True 
                
        return False
                
                
        