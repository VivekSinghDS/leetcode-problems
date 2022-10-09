class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        '''
        ROW, COL = len(grid), len(grid[0])
        mod = (10 ** 9 + 7)
        
        @lru_cache(maxsize = None)
        def dfs(r, c, current):
            current += grid[r][c]
            current %= k 
            
            if r == ROW - 1 and c == COL - 1:
                if current == 0:
                    return 1
                return 0
            
            total = 0 
            if r + 1 < ROW:
                total += dfs(r + 1, c, current)
                
            if c + 1 < COL:
                total += dfs(r, c + 1, current)
                
            return total%mod
        
        return dfs(0, 0, 0)%mod
        '''

        hm = defaultdict(list)
        
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r >= len(grid) or c >= len(grid[0]):
                return []
            if r == m - 1 and c == n - 1:
                hm[(r, c)] = {grid[r][c] : 1}
                return
            if (r, c) not in hm:
                dfs(r + 1, c)
                dfs(r, c + 1)
                it = defaultdict(int)
                if (r + 1, c) in hm:
                    for i in hm[(r + 1, c)]:
                        it[(grid[r][c] + i) % k] += hm[(r + 1, c)][i]
                if (r, c + 1) in hm:
                    for i in hm[(r, c + 1)]:
                        it[(grid[r][c] + i) % k] += hm[(r, c + 1)][i]
                hm[(r, c)] = it
            return
        dfs(0, 0)
        res = 0
        for i in hm[(0, 0)]:
            if i % k == 0:
                res += hm[(0, 0)][i]
                res %= (10 ** 9 + 7)
        return res
        
        
        
                    