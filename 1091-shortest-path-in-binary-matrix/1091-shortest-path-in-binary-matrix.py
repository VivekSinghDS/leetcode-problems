class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        
        if grid[0][0] == 1:
            return -1
        
        queue.append((0, 0, 1))
        shortest = float('inf')
        seen = set()
        
        while queue:
            for _ in range(len(queue)):
                
                r, c, count = queue.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    shortest = min(shortest, count)
                    
                elif (r, c) not in seen:
                    seen.add((r, c))
                    paths = [(r + 1, c),
                            (r - 1, c),
                            (r, c + 1),
                            (r, c - 1),
                             
                            (r + 1, c + 1),
                            (r + 1, c - 1),
                            (r - 1, c - 1), 
                            (r - 1, c + 1)]
                    
                    for row, col in paths:
                        if( 0 <= row < len(grid) and 0 <= col < len(grid[0]) and 
                          grid[row][col] == 0):
                            queue.append((row, col, count + 1))
                            
        return shortest if shortest != float('inf') else -1
            
        
        
            
                        
        