'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:        
        @cache
        def dfs(index, previous):
            if index >= len(prices):
                return 0 
            
            profit = float('-inf')
            include = float('-inf')
            exclude = float('-inf')
            
            if previous is None:
                include = dfs(index + 1, prices[index])
                exclude = dfs(index + 1, None)
                
            elif previous > prices[index]:
                exclude = dfs(index + 1, previous)
                
            else:
                value = prices[index] - previous - fee 
                if value > 0:
                    include = value + dfs(index + 1, None)
                exclude = dfs(index + 1, previous)
            profit = max(profit, include, exclude)
            return profit
        return max(dfs(0, prices[0]), dfs(0, None))
                
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = [0] * n, [0] * n
        
        # In order to hold a stock on day 0, we have no other choice but to buy it for prices[0].
        hold[0] = -prices[0]
        
        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)
        
        return free[-1]
                    