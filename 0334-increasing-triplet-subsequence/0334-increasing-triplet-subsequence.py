class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        sub = [nums[0]]
        for i in range(1, len(nums)):
            index = bisect_left(sub, nums[i])
            if index == len(sub):
                sub.append(nums[i])
                
            else:
                sub[index] = nums[i]
                
            if len(sub) >= 3:
                return True
                
        return len(sub) >= 3
                
        
                    
        
                
                
            
         