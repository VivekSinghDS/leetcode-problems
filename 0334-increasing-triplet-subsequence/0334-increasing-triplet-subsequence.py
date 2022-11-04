class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        sub = [nums[0]]
        for i in range(1, len(nums)):
            if sub[-1] < nums[i]:
                sub.append(nums[i])
                
            else:
                j = 0

                while sub[j] < nums[i]:
                    j += 1
                    
                sub[j] = nums[i]
                
        return len(sub) >= 3
                
        
                    
        
                
                
            
         