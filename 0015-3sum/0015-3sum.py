class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                b = nums[start]
                c = nums[end]
                
                if a + b + c == 0:
                    res.append([a, b, c])
                    start += 1
                    
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    
                if a + b + c > 0:
                    end -= 1
                    
                if a + b + c < 0:
                    start += 1
                    
        return res
                    
                
        