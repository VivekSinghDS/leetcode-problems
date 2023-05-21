class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        seen = set()
        
        paths = [(1, 0), [-1, 0], [0, 1], [0, -1]]
        def invalid(r, c):
            return r < 0 or c < 0 or c >= N or r >= N
        
        def dfs(r, c):
            if (r, c) in seen or invalid(r, c) or grid[r][c] == 0:
                return 
            seen.add((r, c))
            for dr, dy in paths:
                dfs(r + dr, c + dy)
        
        def bfs():
            queue = deque(seen)
            res = 0
            
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in paths:
                        cur_row, cur_col = r + dr, c + dc
                        if invalid(cur_row, cur_col) or (cur_row, cur_col) in seen:
                            continue 
                            
                        if grid[cur_row][cur_col]:
                            return res
                        
                        queue.append((cur_row, cur_col))
                        seen.add((cur_row, cur_col))
                res += 1
            return res
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()
                    
                
                
        