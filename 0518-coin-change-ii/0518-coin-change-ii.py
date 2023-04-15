class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(index, total):
            if total > amount or index >= len(coins):
                return 0 
            
            elif total == amount:
                return 1
            
            ways = dfs(index, coins[index] + total) + dfs(index + 1, total)
            return ways 
        
        return dfs(0, 0)
        