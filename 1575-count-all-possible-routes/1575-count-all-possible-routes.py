class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def dfs(index, remaining):
            # print(index, remaining) 
            if remaining < 0:
                return 0
        
            # seen.add(index)
            ways = 0 if index != finish else 1
            
            for i in range(len(locations)):
                if index == i:
                    continue
                    
                new_remaining = remaining - abs(locations[index] - locations[i])
                ways += dfs(i, new_remaining) % mod
                
            # seen.remove(index)
            return ways % mod
        
        return dfs(start, fuel) % mod
                    
                
        