class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def find_area(heights):
            stack = []
            maxArea = 0
            
            for i, h in enumerate(heights):
                start = i
                
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                    
                stack.append((start, h))
                
            for i, h in stack:
                maxArea = max(maxArea, h * (len(heights) - i))
                
            return maxArea 
        
        dp = [0]*len(matrix[0])
        area = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    dp[c] += 1
                    
                else:
                    dp[c] = 0
                    
            area = max(area, find_area(dp))
            
        return area
                    
            
        