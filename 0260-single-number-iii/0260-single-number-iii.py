class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = 0 
        
        for n in nums:
            total ^= n
            
        diff = (total & - total)
        x = 0
        for n in nums:
            if diff & n:
                x ^= n

                
        return [x, total ^ x]
                
        
        