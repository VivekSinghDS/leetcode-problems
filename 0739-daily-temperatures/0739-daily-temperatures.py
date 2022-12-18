class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        
        ans = [0]*n
        
        for current_day in range(n - 1, -1, -1):
            current_temp = temperatures[current_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue 
                
            days = 1
            
            while temperatures[current_day + days] <= current_temp:
                days += ans[current_day + days]
                
            ans[current_day] = days
            
        return ans
        
        