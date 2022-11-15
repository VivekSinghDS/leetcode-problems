class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(node):
            if node not in visited:
                visited.add(node)
                
                for neighbor in rooms[node]:
                    dfs(neighbor)
                    
        dfs(0)
        return len(rooms) == len(visited)
                    
                
        