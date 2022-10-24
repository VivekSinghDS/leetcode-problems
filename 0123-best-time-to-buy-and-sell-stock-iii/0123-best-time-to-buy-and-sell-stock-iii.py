class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_profits = [0]*(len(prices) + 1)
        right_profits = [0]*(len(prices) + 1)
        
        max_profit = 0 
        left_min, right_max = prices[0], prices[-1]
        
        for l in range(1, len(prices)):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])
            
            r = len(prices) - l - 1
            
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])
            
        for i in range(len(prices)):
            max_profit = max(max_profit, right_profits[i + 1] + left_profits[i])
            
        return max_profit
        