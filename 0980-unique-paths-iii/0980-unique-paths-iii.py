class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_row, start_col = 0, 0
        end_row, end_col = 0, 0 
        empty_squares = 0
        m = len(grid)
        n = len(grid[0])
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    empty_squares += 1
                    
                elif grid[r][c] == 2:
                    end_row, end_col = r, c
                    
                elif grid[r][c] == 1:
                    start_row, start_col = r, c
                    
        # print(empty_squares)
        # print(start_row, start_col)
        # print(end_row, end_col)
        res = 0
        def dfs(r, c, walk):
            nonlocal res
            # print(r, c, walk)
            if (r == end_row and c == end_col):
                if (walk == empty_squares + 1 ):
                    res += 1
                return 
            
            if(0 <= r < m and 0 <= c < n and grid[r][c] != -1 and (r, c) not in seen):
                seen.add((r, c))
                paths = [(r + 1, c), 
                        (r - 1, c), 
                        (r, c + 1), 
                        (r, c - 1)
                        ]
            
                for row, col in paths:
                    
                    dfs(row, col, walk + 1)
                    
                seen.remove((r, c))
                    
            
        seen = set()
        dfs(start_row, start_col, 0)
        return res
        
        