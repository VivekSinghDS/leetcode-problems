class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0]*length
        
        for start, end, value in updates:
            nums[start] += value 
            if end < length - 1:
                nums[end + 1] -= value 
            
        
        running_sum = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            nums[i] = running_sum
            
        return(nums)
            
        