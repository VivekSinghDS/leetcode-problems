class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inf = (2 ** 31) - 1
        queue = deque()
        m = len(rooms)
        n = len(rooms[0])
        inf = (2 ** 31) - 1
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        
        print(queue)
        while queue:
            x, y = queue.popleft()
            paths = [(x + 1, y), (x - 1, y), 
                    (x, y + 1), (x, y - 1)]
            
            for new_x, new_y in paths:
                
                if (0 <= new_x < m) and (0 <= new_y < n) and rooms[new_x][new_y] == inf:
            
                    rooms[new_x][new_y] = 1 + rooms[x][y]
                    queue.append((new_x, new_y))
                
        
                    
        