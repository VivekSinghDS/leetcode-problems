class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        count = 0
        MOD = 10 ** 9 + 7
        @cache
        def dfs(index, current_profit, current_people):                
            if index >= len(group):
                return 0 if current_profit < minProfit else 1
            
            ways = 0
            if group[index] <= current_people:
                ways += dfs(index + 1, min(current_profit + profit[index], minProfit), current_people - group[index])
            ways += dfs(index + 1, current_profit, current_people)
            return ways 
                
        return dfs(0, 0, n) % MOD
        
                
                
        