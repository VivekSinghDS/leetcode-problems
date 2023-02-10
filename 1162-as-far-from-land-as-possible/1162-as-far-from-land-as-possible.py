class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque()
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    q.append([r, c])
                    
        res = -1           
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            r, c = q.popleft()
            res = grid[r][c]
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                # print(newR, newC)
                if (min(newR,newC) >= 0 and max(newC, newR) < N
                   and grid[newR][newC] == 0):
                    q.append([newR,newC])
                    grid[newR][newC] = 1 + grid[r][c]
                    
        return res - 1 if res > 1 else -1
            
            
        