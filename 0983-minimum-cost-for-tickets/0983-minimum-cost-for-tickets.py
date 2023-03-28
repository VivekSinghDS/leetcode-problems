class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1, 7, 30]
        
        @cache
        def dfs(i):
            if i >= len(days):
                return 0
            
            j = i
            res = float('inf')
            for cost, duration in zip(costs, durations):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                    
                res = min(res, dfs(j) + cost)
                
            return res 
        
        return dfs(0)
         
        