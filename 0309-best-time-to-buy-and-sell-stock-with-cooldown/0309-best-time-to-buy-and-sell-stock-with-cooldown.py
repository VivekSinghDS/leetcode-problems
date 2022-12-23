class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        
        dp = {}
        def dfs(index, buying):
            if index >= len(prices):
                return 0 
            
            if (index, buying) in dp:
                return dp[(index, buying)]
            
            if buying:
                buy = dfs(index + 1, not buying) - prices[index]
                cooldown = dfs(index + 1, buying)
                
                dp[(index, buying)] = max(buy, cooldown)
                
            else:
                sell = dfs(index + 2, not buying) + prices[index]
                cooldown = dfs(index + 1, buying)
                
                dp[(index, buying)] = max(sell, cooldown)
                
            return dp[(index, buying)]
        return dfs(0, True)
                
            
                
            
            
        