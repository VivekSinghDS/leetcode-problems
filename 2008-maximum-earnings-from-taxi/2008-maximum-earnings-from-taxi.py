class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rideStart = defaultdict(list)
        
        for start, end, tip in rides:
            rideStart[start].append((end, end - start + tip))
            
        # print(rideStart)
        dp = [0]*(n + 1)
        
        for i in range(n - 1, 0, -1):
            for e, d in rideStart[i]:
                dp[i] = max(dp[i], dp[e] + d)
                
            dp[i] = max(dp[i], dp[i + 1])
            
        # print(dp)
        return dp[1]