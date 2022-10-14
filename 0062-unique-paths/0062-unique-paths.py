class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                if (r == 0 or c == 0):
                    # print(r, c)
                    dp[r][c] = 1
                    
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r][c - 1]+ dp[r - 1][c]
                
        return dp[-1][-1]
        