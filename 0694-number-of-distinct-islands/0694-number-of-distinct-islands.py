class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def current_island_unique():
            for other_island in unique_island:
                if len(other_island) != len(current_island):
                    continue 
                    
                for i1, i2 in zip(other_island, current_island):
                    if i1 != i2:
                        break 
                        
                else:
                    return False 
            return True
            
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in seen or grid[r][c] == 0:
                return 
            
            grid[r][c] = 0
            cur_row_index = r - row_origin
            cur_col_index = c - col_origin 
            current_island.append((cur_row_index, cur_col_index))
            seen.add((r, c))
            
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
            
        seen = set()
        unique_island = []
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    current_island = []
                    row_origin = r
                    col_origin = c 
                    
                    dfs(r, c)
                    
                    if not current_island or not current_island_unique():
                        continue
                        
                    unique_island.append(current_island)
                    
        return len(unique_island)
        