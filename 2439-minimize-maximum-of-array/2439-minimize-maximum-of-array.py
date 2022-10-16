class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def valid(mid):
            sum_ = 0 
            for i in range(len(nums)):
                sum_ += nums[i]
                if sum_ > (i + 1)*mid:
                    return False 
                
            return True
        
        left = 0 
        right = max(nums)
        
        ans = 0 
        
        while left <= right:
            mid = (left + right) // 2
            if valid(mid):
                ans = mid
                right = mid - 1
                
            else:
                left = mid + 1
        return ans 
            
    
        