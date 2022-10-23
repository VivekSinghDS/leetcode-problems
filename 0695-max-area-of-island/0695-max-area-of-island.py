class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0 
        m, n = len(grid), len(grid[0])
        def dfs(r, c):        
            visited.add((r, c))
            area = 1
            
            for row, col in [(r + 1, c), (r - 1, c),
                            (r, c + 1), (r, c - 1)]:
                if 0 <= row < m and 0 <= col < n and grid[row][col] == 1 and (row, col) not in visited:
                    area += dfs(row, col)
                
            return area
        
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    cur_area = dfs(r, c)
                    ans = max(ans, cur_area)
                    
        return ans
                
        
        
            
            
            
            
            
        