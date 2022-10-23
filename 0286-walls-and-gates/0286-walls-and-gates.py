class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inf = (2 ** 31) - 1
        queue = deque()
        m = len(rooms)
        n = len(rooms[0])
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        

        while queue:
            
            x, y = queue.popleft()
                
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                total_x = dx 
                total_y = dy 
                    
                if (total_x < 0 or total_x >= len(rooms) 
                    or total_y < 0 or total_y >= len(rooms[0]) 
                    or rooms[total_x][total_y] != inf):
                    continue 
                        
                rooms[total_x][total_y] = rooms[x][y] + 1
                    
                queue.append((total_x, total_y))
                    
        