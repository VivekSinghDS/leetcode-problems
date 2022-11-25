class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        
        for i in range(len(nums) + 1):
            
            while stack and (i == len(nums) or nums[stack[-1]] >= nums[i]):
                mid = stack.pop()
                left_boundary = stack[-1] if stack else -1
                right_boundary = i
                
                count = (mid - left_boundary) * (right_boundary - mid)
                ans -= (count * nums[mid])
                
            stack.append(i)
            
        stack = []
            
        for i in range(len(nums) + 1):
            while stack and (i == len(nums) or nums[stack[-1]] <= nums[i]):
                mid = stack.pop()
                left_boundary = stack[-1] if stack else -1
                right_boundary = i
                
                count = (mid - left_boundary) * (right_boundary - mid)
                ans += (count * nums[mid])
                
            stack.append(i)
                
        return ans
        