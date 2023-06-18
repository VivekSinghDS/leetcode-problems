class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        seen = set()
        @cache
        def dfs(r, c):
            
            count = 1
            seen.add((r, c))
            
            paths = [(r + 1, c), (r - 1, c), 
                    (r, c + 1), (r, c - 1)]
            
            for row, col in paths:
                if(0 <= row < len(grid)
                  and 0 <= col < len(grid[0])
                  and grid[row][col] > grid[r][c]):
                    count += dfs(row, col) % mod
            return count % mod
            
            
            
        count = 0
        # res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                seen = set()
                value = dfs(i, j) % mod
                # print(value, ' is value')
                # res.append(value)
                count += value % mod
                
        return (count) % mod