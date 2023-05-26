class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        M = 1
        N = len(piles)
        
        @cache
        def dfs(index, state, M):
            if index >= len(piles):
                return 0 
            res = float('inf') if state == "Bob" else -1
            stones = 0
            for x in range(1, min(2 * M, N - index) + 1):
                stones += piles[index + x - 1]
                if state == "Bob":
                    res = min(res, dfs(index + x, "Alice", max(M, x))) 
                else:
                    res = max(res, stones + dfs(index + x, "Bob", max(M, x)))
            return res
        
        return dfs(0, "Alice", 1)
                
            
                
                
            
            
                
                
            
            
        