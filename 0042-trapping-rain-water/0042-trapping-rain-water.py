class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_till_now = height[0]
        for i in range(1, len(height)):
            max_left[i] = max_till_now
            
            if max_till_now < height[i]:
                max_till_now = height[i]
        
        max_right = [0]*len(height)
        max_till_now = height[-1]
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max_till_now
            
            if max_till_now < height[i]:
                max_till_now = height[i]
                
        min_left_right = [0]*len(height)
        for i in range(len(height)):
            min_left_right[i] = min(max_left[i], max_right[i])
            
        
        ans = 0
        for i in range(len(height)):
            if min_left_right[i] - height[i] > 0:
                ans += (min_left_right[i] - height[i])
        return ans
        
                
        
        