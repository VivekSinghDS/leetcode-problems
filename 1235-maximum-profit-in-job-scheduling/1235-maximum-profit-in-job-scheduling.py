class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit)) # combine all of them and sort 
        
        # print(jobs)
        
        n = len(startTime)
        dp = [0]*(n + 1)
        
        for i in reversed(range(n)):
            k = bisect_left(jobs, jobs[i][1], key = lambda j : j[0]) # find the place where you can start the next schedule
            dp[i] = max(jobs[i][2] + dp[k], dp[i + 1])
            
        return dp[0]
        
        