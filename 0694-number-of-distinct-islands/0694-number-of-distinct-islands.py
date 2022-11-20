class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def current_island_unique():
            for other_island in unique_island:
                if len(other_island) != len(all_island):
                    continue 
                    
                for x, y in zip(other_island, all_island):
                    if x != y:
                        break
                        
                else:
                    return False

            return True
        def dfs(r, c):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in seen
               or grid[r][c] == 0):
                return 
            
            path = [(r + 1, c), (r - 1, c), 
                   (r, c + 1), (r, c - 1)]
            
            seen.add((r, c))
            all_island.append((r - r_origin, c - c_origin))
            
            for row, col in path:
                dfs(row, col)
                
                
        
        seen = set()
        unique_island = []
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                r_origin = r
                c_origin = c
                all_island = []
                
                dfs(r, c)
                
                if not all_island or not current_island_unique():
                    continue 
                    
                unique_island.append(all_island)
                
        return len(unique_island)
        