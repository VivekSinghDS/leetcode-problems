class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
        @cache
        def dfs(r, c):
            if invalid(r, c):
                return 0
            
            count = 1 
            moves = 0
            paths = [(r - 1, c + 1), (r, c + 1), (r + 1, c + 1)]
            for row, col in paths:
                if not invalid(row, col) and grid[row][col] > grid[r][c] and (row, col) not in seen:
                    seen.add((row, col))
                    moves = max(moves, dfs(row, col))
                    seen.remove((row, col))
            
            return count + moves
        
        
        res = 0
        for i in range(len(grid)):
            seen = set()
            res = max(res, dfs(i, 0) - 1)
        return res
                
                
            
            
        