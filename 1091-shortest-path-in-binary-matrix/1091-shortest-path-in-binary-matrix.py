class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        res = float('inf')
        queue.append((0, 0, 1))
        seen = set()
        while queue:
            for _ in range(len(queue)):
                row, col, count = queue.popleft()
                
                if (not(0 <= row < len(grid)) 
                   or not(0 <= col < len(grid[0])) or (grid[row][col] == 1)) or (row, col) in seen:
                    
                    continue
                # print(row, col)
                seen.add((row, col))
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    res = min(res, count)
                    
                path = [(row + 1, col), (row - 1, col), 
                       (row, col + 1), (row, col - 1), 
                       (row + 1, col + 1), (row - 1, col - 1), 
                       (row - 1, col + 1), (row + 1, col - 1)]
                
                for r, c in path:
                    queue.append((r, c, count + 1))
        return res if res != float('inf') else -1
                
                    
                
                    
                
                
        