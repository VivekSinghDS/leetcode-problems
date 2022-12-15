class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        seen = set()
        res = float('-inf')
        m = len(grid)
        n = len(grid[0])
        def dfs(r, c, running_sum):
            nonlocal res
            running_sum += grid[r][c]
            res = max(res, running_sum)
            paths = [(r + 1, c), 
                    (r - 1, c), 
                    (r, c + 1), 
                    (r, c - 1)]
            seen.add((r, c))
            for row, col in paths:
                if (0 <= row < m and 0 <= col < n
                   and grid[row][col] != 0 and 
                   (row, col) not in seen):
                    
                    dfs(row, col, running_sum)
                    
            running_sum -= grid[r][c]
            seen.remove((r, c))
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0)
                    
        return res if res != float('-inf') else 0
                    
        
        