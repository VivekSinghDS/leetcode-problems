class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(remaining):
            if remaining < 0:
                return -1
            
            elif remaining == 0:
                return 0 
            
            min_cost = float('inf')
            for coin in coins:
                res = dfs(remaining - coin)
                if res != -1:
                    min_cost = min(min_cost, 1 + res)
                    
            return min_cost
        
        return dfs(amount) if dfs(amount) != float('inf') else -1
                
        