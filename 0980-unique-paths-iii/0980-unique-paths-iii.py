class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_row, start_col = 0, 0
        end_row, end_col = 0, 0
        empty = 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        seen = set()
        
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_row, start_col = r, c
                    
                elif grid[r][c] == 0:
                    empty += 1
                    
                elif grid[r][c] == 2:
                    end_row, end_col = r, c
        # print(start_row, start_col)
        # print(end_row, end_col)
        # print(empty)
        def dfs(r, c, seen, walk):
            nonlocal res
            if (r == end_row and c == end_col):
                if walk == empty + 1:
                    res += 1
                    
                return 

            
            if(0 <= r < m and 0 <= c < n and grid[r][c] != -1 and (r, c) not in seen):
                seen.add((r, c))
                            
                paths = [(r + 1, c),
                        (r - 1, c),
                        (r, c + 1),
                        (r, c - 1)]
                for x, y in paths:
                    dfs(x, y, seen, walk + 1)
                    
                seen.remove((r, c))
                
        dfs(start_row, start_col, seen, 0)
        return res
                    
                    
        