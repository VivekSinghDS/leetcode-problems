class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or c >=len(grid[0])
                or (r, c) in seen or grid[r][c] == 0):
                return 0
            
            area = 1
            paths = [(r + 1, c), 
                    (r - 1, c), 
                    (r, c + 1), 
                    (r, c - 1)]
            
            seen.add((r, c))
            for row, col in paths:
                area += dfs(row, col)
                
            return area
        
        seen = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c, border):
            visited.add((r, c))
            paths = [(r + 1, c), (r - 1, c),
                        (r, c + 1), (r, c - 1)]
            if border:
                grid[r][c] = 0

                for row, col in paths:
                    if (0 <= row < len(grid) and 0 <= col < len(grid[0]) 
                        and grid[row][col] == 1 and (row, col) not in visited):
                        dfs(row, col, border)
                        
                return grid[r][c]
                        
            elif not border:
                cur_area_count = 1
                
                for row, col in paths:
                    if (0 <= row < len(grid) and 0 <= col < len(grid[0]) 
                        and grid[row][col] == 1 and (row, col) not in visited):
                        cur_area_count += dfs(row, col, border)
                        
                return cur_area_count

        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if (r in [0, ROW - 1] or c in [0, COL - 1]) and grid[r][c] == 1:
                    dfs(r, c, True)
                    
        for r in range(ROW):
            for c in range(COL):    
                if grid[r][c] == 1:
                    cur_area = dfs(r, c, False)
                    max_area = max(max_area, cur_area)
                    
        return max_area
           

'''
                
        
        
            
            
            
            
            
        