class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        def dfs(room):
            if room not in seen:
                seen.add(room)
                
                for keys in rooms[room]:
                    dfs(keys)
        
        dfs(0)
        
        return len(seen) == len(rooms)
        