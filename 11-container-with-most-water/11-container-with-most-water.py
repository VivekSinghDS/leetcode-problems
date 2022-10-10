class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        area = 0
        while l <= r:
            distance = r - l 
            width = min(height[l], height[r])

            area = distance * width
            res = max(res, area)
            
            if(height[l] > height[r]):
                r -= 1
                
            else:
                l += 1
                
        return res
        